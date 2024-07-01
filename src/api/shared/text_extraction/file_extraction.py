from llama_index.core import SimpleDirectoryReader


def extract_documents_from_file(file_path: str):
    reader = SimpleDirectoryReader(
        input_files=[file_path]
    )

    documents = reader.load_data(show_progress=True)

    return documents
