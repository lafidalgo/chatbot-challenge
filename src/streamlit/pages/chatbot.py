import streamlit as st

from navigation import make_sidebar

import utils
import config

utils.init_page_configuration(add_logo=False)

make_sidebar()

test_name = utils.send_get_api_request(config.API_URLS['GET_TEST_NAME'])

# Markdown
st.markdown(
    f"""
    ## Olá, {test_name}!
    ## Bem-vindo ao Hotmart Insights!

    Esta aplicação web é uma poderosa ferramenta que utiliza técnicas avançadas de inteligência artificial para analisar e extrair informações estratégicas do site da Hotmart. 

    Com o poder da IA, você pode:

    - **Análise instantânea**: Obtenha insights rápidos sobre métricas-chave da Hotmart.
    - **Otimização de processos**: Simplifique e agilize a análise de dados, economizando tempo e recursos.
    - **Decisões estratégicas**: Baseie suas decisões de negócios em informações precisas sobre tendências e performance da Hotmart.

    Explore as funcionalidades no menu lateral e descubra como essa ferramenta pode transformar sua abordagem na análise de dados da Hotmart!
    """
)
