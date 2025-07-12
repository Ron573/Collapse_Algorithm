import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from scipy.stats import entropy
import nltk

# Load data
with open('data/fpds_2015.txt') as f1, open('data/fpds_2025.txt') as f2:
    tokens_2015 = nltk.word_tokenize(f1.read().lower())
    tokens_2025 = nltk.word_tokenize(f2.read().lower())

# Build distributions
def get_dist(tokens):
    counts = Counter(tokens)
    total = sum(counts.values())
    return {k: v / total for k, v in counts.items()}

dist_15 = get_dist(tokens_2015)
dist_25 = get_dist(tokens_2025)

# Align vocab
vocab = list(set(dist_15.keys()).union(dist_25.keys()))
p = np.array([dist_15.get(w, 1e-10) for w in vocab])
q = np.array([dist_25.get(w, 1e-10) for w in vocab])

# KL divergence
kl_values = p * np.log2(p / q)
plt.figure(figsize=(12,6))
plt.bar(vocab[:30], kl_values[:30])
plt.xticks(rotation=45, ha='right')
plt.title("Top KL Divergence Terms (2015 → 2025)")
plt.tight_layout()
plt.savefig("assets/figures/kl_divergence_fpds_plot.png")

# Entropy
entropy_2015 = entropy(p, base=2)
entropy_2025 = entropy(q, base=2)
plt.figure()
plt.bar(['2015', '2025'], [entropy_2015, entropy_2025], color=['navy', 'crimson'])
plt.ylabel("Token Entropy (bits)")
plt.title("Entropy Drift in FPDS Language")
plt.tight_layout()
plt.savefig("assets/figures/entropy_drift_fpds_plot.png")

