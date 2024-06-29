import streamlit as st
import streamlit_nested_layout


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
