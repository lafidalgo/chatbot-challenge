import streamlit as st

import utils

utils.init_page_configuration()

# Markdown
st.markdown(
    f"""
    ## Olá!
    ## Bem-vindo ao Hotmart Insights!

    Esta aplicação web é uma poderosa ferramenta que utiliza técnicas avançadas de inteligência artificial para analisar e extrair informações estratégicas do site da Hotmart. 

    Com o poder da IA, você pode:

    - **Análise instantânea**: Obtenha insights rápidos sobre métricas-chave da Hotmart.
    - **Otimização de processos**: Simplifique e agilize a análise de dados, economizando tempo e recursos.
    - **Decisões estratégicas**: Baseie suas decisões de negócios em informações precisas sobre tendências e performance da Hotmart.

    Explore as funcionalidades no menu lateral e descubra como essa ferramenta pode transformar sua abordagem na análise de dados da Hotmart!
    """
)
