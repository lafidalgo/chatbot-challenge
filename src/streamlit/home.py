import streamlit as st

import page_formatting

import utils

page_formatting.init_page_configuration()

authenticator, auth_config = utils.import_authentication_config()
authenticator.login()

page_formatting.make_sidebar(authenticator)

if st.session_state["authentication_status"]:
    # Markdown
    st.markdown(
        f"""
        ## Olá, {st.session_state["name"]}!
        ## Bem-vindo ao Context Chatbot!

        Esta aplicação web é uma poderosa ferramenta que utiliza técnicas avançadas de inteligência artificial para analisar e extrair informações de documentos. 

        Com o poder da IA, você pode:

        - **Análise instantânea**: Obtenha insights rápidos sobre seus documentos.
        - **Otimização de processos**: Simplifique e agilize a análise de dados, economizando tempo e recursos.
        - **Decisões estratégicas**: Baseie suas decisões de negócios em informações precisas sobre tendências e performance.

        Explore as funcionalidades no menu lateral e descubra como essa ferramenta pode transformar sua abordagem na análise dos seus documentos!
        """
    )

elif st.session_state["authentication_status"] is False:
    st.error('Usuário e/ou senha incorretos')
elif st.session_state["authentication_status"] is None:
    st.warning('Por favor, faça login para acessar o sistema.')
