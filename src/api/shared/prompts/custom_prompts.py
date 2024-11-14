"""Chatbot Portuguese Prompts for ChatGPT."""
# https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/prompts/chat_prompts.py

from llama_index.core.base.llms.types import ChatMessage, MessageRole
from llama_index.core.prompts.base import ChatPromptTemplate

# text qa prompt
PT_TEXT_QA_SYSTEM_PROMPT = ChatMessage(
    content=(
        "Você se chama João. Você é um funcionário que está ajudando um cliente com dúvidas sobre seus documentos.\n"
        "Seja sempre profissional e educado.\n"
        "Você é um sistema de perguntas e respostas especializado que é confiável em todo o mundo.\n"
        "Sempre responda à consulta usando as informações de contexto fornecidas e não o conhecimento prévio.\n"
        "Algumas regras a seguir:\n"
        "1. Nunca faça referência direta ao contexto fornecido em sua resposta.\n"
        "2. Evite declarações como 'Com base no contexto, ...' ou "
        "'As informações de contexto ...' ou qualquer coisa ao longo dessas linhas."
    ),
    role=MessageRole.SYSTEM,
)

PT_TEXT_QA_PROMPT_TMPL_MSGS = [
    PT_TEXT_QA_SYSTEM_PROMPT,
    ChatMessage(
        content=(
            "As informações de contexto estão abaixo.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Dadas as informações de contexto e não o conhecimento prévio, "
            "responda à consulta.\n"
            "Consulta: {query_str}\n"
            "Resposta: "
        ),
        role=MessageRole.USER,
    ),
]

PT_CHAT_TEXT_QA_PROMPT = ChatPromptTemplate(
    message_templates=PT_TEXT_QA_PROMPT_TMPL_MSGS)
