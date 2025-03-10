from langchain.text_splitter import RecursiveCharacterTextSplitter
from common.config import EMBEDDING_CHUNK_SIZE, EMBEDDING_CHUNK_OVERLAP


def clean_text(text: str) -> str:
    return text  # TODO: Implement text cleaning


def split_text_into_chunks(text: str) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=EMBEDDING_CHUNK_SIZE, chunk_overlap=EMBEDDING_CHUNK_OVERLAP
    )
    return text_splitter.split_text(clean_text(text))
