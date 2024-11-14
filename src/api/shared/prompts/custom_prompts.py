"""Chatbot Custom Prompts for ChatGPT."""
# https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/prompts/chat_prompts.py

from llama_index.core.base.llms.types import ChatMessage, MessageRole
from llama_index.core.prompts.base import ChatPromptTemplate

# text qa prompt
PT_TEXT_QA_SYSTEM_PROMPT = ChatMessage(
    content=(
        "Your name is João. You are an employee assisting a client with questions about their documents.\n"
        "Always be professional and polite.\n"
        "You are a globally trusted question-and-answer system specializing in reliable responses.\n"
        "Always answer the query using the provided context information, not prior knowledge.\n"
        "Some rules to follow:\n"
        "1. Never directly reference the provided context in your answer.\n"
        "2. Avoid statements like 'Based on the context, ...' or "
        "'The context information ...' or anything along these lines."
    ),
    role=MessageRole.SYSTEM,
)

PT_TEXT_QA_PROMPT_TMPL_MSGS = [
    PT_TEXT_QA_SYSTEM_PROMPT,
    ChatMessage(
        content=(
            "The context information is below.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Given the context information, and not prior knowledge, "
            "answer the query.\n"
            "Query: {query_str}\n"
            "Answer: "
        ),
        role=MessageRole.USER,
    ),
]

PT_CHAT_TEXT_QA_PROMPT = ChatPromptTemplate(
    message_templates=PT_TEXT_QA_PROMPT_TMPL_MSGS)
