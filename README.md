# 🌤️ ClimaTech - Dashboard Meteorológico em Tempo Real

<p align="center">
  <a href="https://climatechnickolas.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🔴_ACESSAR_PROJETO_ONLINE-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Acessar Projeto Online">
  </a>
</p>

O **ClimaTech** é uma aplicação web interativa desenvolvida em Python que consome dados meteorológicos em tempo real através da API REST gratuita **Open-Meteo**. O sistema converte o nome de qualquer cidade do mundo em coordenadas geográficas (Geocoding) e exibe painéis de indicadores climáticos instantâneos e previsões gráficas para as próximas 24 horas.

---

## 🚀 Funcionalidades
* **Geocoding Automatizado:** Conversão dinâmica de texto (nome da cidade) em coordenadas geográficas de Latitude e Longitude via requisição HTTP.
* **Indicadores em Tempo Real (KPIs):** Exibição instantânea de Temperatura Atual, Sensação Térmica e Umidade Relativa do Ar.
* **Previsão em Gráfico Interativo:** Geração de gráfico de linhas contínuo utilizando **Plotly Express**, mapeando a variação térmica hora a hora no formato de 24h.
* **Navegação de Dados Não-Estruturados:** Parsing e tratamento avançado de respostas em formato **JSON**, extraindo e cruzando dados de múltiplas requisições em uma única interface limpa.

## 🛠️ Tecnologias Utilizadas
| Tecnologia | Função |
| :--- | :--- |
| **Python** | Lógica de programação, backend e orquestração de APIs |
| **Requests** | Configuração de parâmetros (`params`) e consumo de APIs REST via métodos GET |
| **Streamlit** | Construção do dashboard visual e renderização reativa |
| **Pandas** | Transformação de listas JSON em DataFrames e manipulação de datas/horários |
| **Plotly Express** | Criação do gráfico de linha com marcadores dinâmicos |

## 💡 Competências em Destaque no Portfólio
Este projeto comprova habilidades essenciais em comunicação entre sistemas web:
* **Domínio de APIs RESTful:** Compreensão prática sobre como estruturar requisições HTTP programaticamente sem depender de interfaces gráficas prontas.
* **Manipulação de Estruturas JSON:** Capacidade de navegar em dicionários aninhados complexos e converter dados brutos de web services em valor analítico.
* **Tratamento de Exceções de Rede:** Implementação de verificações de status HTTP (`200 OK`) e validação de rotas para evitar quebras no sistema diante de entradas inválidas do usuário.