from collections import defaultdict
from clustering import cluster_text_documents

articles = [
    "The quick brown fox jumps over the lazy dog.",
    "The quick brown fox jumps over the lazy cat.",
    "The quick brown fox jumps over the lazy rabbit.",
    "The quick brown fox jumps over the lazy turtle.",
    "The quick brown fox jumps over the lazy hamster.",
    "The quick brown fox jumps over the lazy fish.",
    "The quick brown fox jumps over the lazy bird.",
    "The quick brown fox jumps over the lazy pigeon.",
    "The quick brown fox jumps over the lazy snake.",
    "The quick brown fox jumps over the lazy frog.",
    "The quick brown fox jumps over the lazy spider.",
    "The quick brown fox jumps over the lazy toad.",
]

cluster_labels = cluster_text_documents(articles, distance_threshold=0.2)

clusters = defaultdict(list)
for i, label in enumerate(cluster_labels):
    clusters[label].append(articles[i])

print("Clustering Results:")
for cluster_id, grouped_articles in clusters.items():
    print(f"\nCluster {cluster_id}:")
    for article in grouped_articles:
        print(f"  - {article}")
