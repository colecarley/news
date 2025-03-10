from sentence_transformers import SentenceTransformer
import numpy as np
from common.config import SENTENCE_TRANSFORMER_EMBEDDING_MODEL
from preprocessing import split_text_into_chunks


embedding_model = SentenceTransformer(SENTENCE_TRANSFORMER_EMBEDDING_MODEL)


def generate_embedding(text: str) -> np.ndarray:
    return embedding_model.encode(text)


def generate_chunk_embeddings(chunks: list[str]) -> list[np.ndarray]:
    return [generate_embedding(chunk) for chunk in chunks]


def compute_representative_embedding(text: str) -> np.ndarray:
    chunk_embeddings = generate_chunk_embeddings(split_text_into_chunks(text))
    return np.mean(chunk_embeddings, axis=0)
