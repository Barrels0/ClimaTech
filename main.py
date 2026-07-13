import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(page_title="ClimaTech", layout="centered")
st.title("🌤️ ClimaTech - Dashboard Meteorológico")
st.divider()

cidade = st.text_input("Digite o nome da cidade:")

if st.button("Buscar Clima", type="primary"):
    
    if cidade:
        url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {"name": cidade, "count": 1, "language": "pt", "format": "json"}
        reposta = requests.get(url, params=params)
        
        if reposta.status_code == 200:
            dados = reposta.json()
            
            if "results" in dados:
                lat = dados["results"][0]["latitude"]
                lon = dados["results"][0]["longitude"]
                nome_cid = dados["results"][0]["name"]
                
                url_clima = "https://api.open-meteo.com/v1/forecast"
                params_clima = {
                    "latitude": lat,
                    "longitude": lon,
                    "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature"], 
                    "hourly": "temperature_2m"
                }

                resp_clima = requests.get(url_clima, params=params_clima).json()

                temp = resp_clima["current"]["temperature_2m"]
                umidade = resp_clima["current"]["relative_humidity_2m"]
                sensacao = resp_clima["current"]["apparent_temperature"]

                st.subheader(f"📍 Clima atual em {nome_cid}")
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Temperatura Atual", f"{temp} °C")
                col2.metric("Sensação Térmica", f"{sensacao} °C") 
                col3.metric("Umidade", f"{umidade} %")

                st.divider()
                
                df_horas = pd.DataFrame({
                    "Horário": resp_clima["hourly"]["time"][:24],
                    "Temperatura (°C)": resp_clima["hourly"]["temperature_2m"][:24]
                })
                if not df_horas.empty:
                    fig = px.line(df_horas, x="Horário", y="Temperatura (°C)", title="📈 Previsão de Temperatura (Próximas 24 Horas)",markers=True)
                    fig.update_traces(line_color="#FF6C37", marker=dict(size=8))
                    
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("ℹ️ Sem informações para gerar o gráfico.")
            else:
                st.error("❌ Cidade não encontrada. Tente digitar outro nome ou verifique a ortografia.")
        else:
            st.error("Erro ao conectar com o servidor de busca de cidades.")
    else:
        st.warning("⚠️ Por favor, digite o nome de uma cidade antes de buscar!")