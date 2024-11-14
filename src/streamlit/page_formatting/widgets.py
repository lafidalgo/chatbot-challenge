import streamlit as st
import streamlit_nested_layout


def display_response_references(query_references):
    if not query_references:
        return

    # Display references
    with st.expander("See References"):
        # Sort query references by score
        sorted_references = sorted(
            query_references, key=lambda x: x['score'], reverse=True)

        for index, reference in enumerate(sorted_references):
            with st.expander(f"**Reference {index+1}**"):
                st.text(reference['text'])


def collection_selectbox(qdrant_collections):
    # Dropdown to select desired qdrant collection
    dropdown_label = "Select the reference document you want to query:"

    selected_collection = st.selectbox(
        dropdown_label,
        qdrant_collections)

    return selected_collection


def llm_model_selectbox(llms_infos):
    # Get the companies of the models
    models_companies = [model_info["company"]
                        for model_info in llms_infos.values()]
    # Unique ordered values
    models_companies = list(dict.fromkeys(models_companies))

    # Create two columns
    company_column, model_column = st.columns(2)

    # Select the company of the language model
    dropdown_label_company = "Select the desired LLM model provider:"
    with company_column:
        selected_llm_company = st.selectbox(
            dropdown_label_company, models_companies)

    # Select the language model
    dropdown_label_name = "Select the desired LLM model:"
    # Filter the models by the selected company
    company_filtered_llms_names = [
        key for key, value in llms_infos.items() if value["company"] == selected_llm_company]
    with model_column:
        selected_llm_model_name = st.selectbox(
            dropdown_label_name, company_filtered_llms_names)

    return selected_llm_model_name
