import streamlit as st

from navigation import make_sidebar

import utils

utils.init_page_configuration()

authenticator, auth_config = utils.import_authentication_config()
authenticator.login()

make_sidebar(authenticator)

if st.session_state["authentication_status"]:
    # Markdown
    st.markdown(
        f"""
        ## Olá, {st.session_state["name"]}!
        ## Bem-vindo ao Hotmart Insights!

        Esta aplicação web é uma poderosa ferramenta que utiliza técnicas avançadas de inteligência artificial para analisar e extrair informações estratégicas do site da Hotmart. 

        Com o poder da IA, você pode:

        - **Análise instantânea**: Obtenha insights rápidos sobre métricas-chave da Hotmart.
        - **Otimização de processos**: Simplifique e agilize a análise de dados, economizando tempo e recursos.
        - **Decisões estratégicas**: Baseie suas decisões de negócios em informações precisas sobre tendências e performance da Hotmart.

        Explore as funcionalidades no menu lateral e descubra como essa ferramenta pode transformar sua abordagem na análise de dados da Hotmart!
        """
    )

elif st.session_state["authentication_status"] is False:
    st.error('Usuário e/ou senha incorretos')
elif st.session_state["authentication_status"] is None:
    st.warning('Por favor, faça login para acessar o sistema.')
