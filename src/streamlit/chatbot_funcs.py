import streamlit as st
import streamlit_nested_layout

import utils


def response_generator():
    import random
    import time

    response = random.choice(
        [
            "Olá! Como posso ajudar você hoje?",
            "Oi, humano! Existe alguma coisa com a qual eu possa te ajudar?",
            "Você precisa de ajuda?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def display_response_references(query_references):
    # Display references
    with st.expander("Ver referências"):
        # Sort query references by score
        sorted_references = sorted(
            query_references, key=lambda x: x['score'], reverse=True)

        for index, reference in enumerate(sorted_references):
            with st.expander(f"**Referência {index+1}**"):
                st.text(reference['text'])


def llm_model_selectbox(llms_infos):
    # Get the companies of the models
    models_companies = [model_info["company"]
                        for model_info in llms_infos.values()]
    # Unique ordered values
    models_companies = list(dict.fromkeys(models_companies))

    # Create two columns
    company_column, model_column = st.columns(2)

    # Select the company of the language model
    dropdown_label_company = "Selecione a empresa do modelo de linguagem desejado:"
    with company_column:
        selected_llm_company = st.selectbox(
            dropdown_label_company, models_companies)

    # Select the language model
    dropdown_label_name = "Selecione o modelo de linguagem desejado:"
    # Filter the models by the selected company
    company_filtered_llms_names = [
        key for key, value in llms_infos.items() if value["company"] == selected_llm_company]
    with model_column:
        selected_llm_model_name = st.selectbox(
            dropdown_label_name, company_filtered_llms_names)

    return selected_llm_model_name
