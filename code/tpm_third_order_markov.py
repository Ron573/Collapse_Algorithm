import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import nltk
from nltk.util import ngrams

# Load tokenized text from FPDS-cleaned contract corpora (2015–2025)
years = ['2015', '2025']
data = {}
for y in years:
    with open(f'data/fpds_{y}.txt', 'r') as f:
        data[y] = nltk.word_tokenize(f.read().lower())

# Build third-order transition matrix
def build_third_order_matrix(tokens):
    transitions = defaultdict(lambda: defaultdict(int))
    trigrams = list(ngrams(tokens, 3))
    for w1, w2, w3 in trigrams:
        transitions[(w1, w2)][w3] += 1
    # Normalize
    tpm = {}
    for prev, following in transitions.items():
        total = sum(following.values())
        tpm[prev] = {w3: count / total for w3, count in following.items()}
    return tpm

tpm_2025 = build_third_order_matrix(data['2025'])

# Heatmap visualization (optional flattening)
pairs = list(tpm_2025.keys())[:15]
labels = list(set(w3 for v in tpm_2025.values() for w3 in v.keys()))[:15]

matrix = np.zeros((len(pairs), len(labels)))
for i, p in enumerate(pairs):
    for j, l in enumerate(labels):
        matrix[i, j] = tpm_2025[p].get(l, 0)

plt.figure(figsize=(12, 8))
sns.heatmap(matrix, xticklabels=labels, yticklabels=[f"{a} {b}" for a,b in pairs], cmap='rocket', cbar=True)
plt.title("Third-Order TPM – FPDS 2025")
plt.tight_layout()
plt.savefig("assets/figures/third_order_TPM_generated.png")

