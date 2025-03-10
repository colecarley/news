from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from embedding import compute_representative_embedding


def compute_cosine_distance_matrix(embeddings: np.ndarray) -> np.ndarray:
    similarity_matrix = cosine_similarity(embeddings)
    return 1 - similarity_matrix  # Convert similarity to distance


def perform_agglomerative_clustering(
    embeddings: np.ndarray, distance_threshold: float
) -> np.ndarray:
    distance_matrix = compute_cosine_distance_matrix(embeddings)

    clustering_model = AgglomerativeClustering(
        metric="precomputed",
        linkage="average",
        distance_threshold=distance_threshold,
        n_clusters=None,
    ).fit(distance_matrix)

    return clustering_model.labels_


def cluster_text_documents(
    texts: list[str], distance_threshold: float = 0.2
) -> list[int]:
    embeddings = np.array([compute_representative_embedding(text) for text in texts])
    return perform_agglomerative_clustering(embeddings, distance_threshold)
