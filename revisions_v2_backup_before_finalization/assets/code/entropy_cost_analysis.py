
import numpy as np
import math
from collections import Counter
from scipy.stats import entropy as scipy_entropy, chi2_contingency
from sklearn.metrics import mutual_info_score

# ---------- 1. Shannon Entropy ----------
def shannon_entropy(text):
    frequency = Counter(text)
    total = len(text)
    probabilities = [freq / total for freq in frequency.values()]
    return -sum(p * math.log2(p) for p in probabilities)

# ---------- 2. Huffman Compression ----------
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    nodes = [Node(c, f) for c, f in freq.items()]
    while len(nodes) > 1:
        nodes = sorted(nodes)
        left, right = nodes.pop(0), nodes.pop(0)
        merged = Node(freq=left.freq + right.freq)
        merged.left, merged.right = left, right
        nodes.append(merged)
    return nodes[0]

def build_huffman_codes(tree, prefix="", codebook={}):
    if tree:
        if tree.char:
            codebook[tree.char] = prefix
        build_huffman_codes(tree.left, prefix + "0", codebook)
        build_huffman_codes(tree.right, prefix + "1", codebook)
    return codebook

def huffman_compression_ratio(text):
    tree = build_huffman_tree(text)
    codes = build_huffman_codes(tree)
    encoded_length = sum(len(codes[char]) for char in text)
    original_bits = len(text) * 8
    return encoded_length / original_bits

# ---------- 3. Markov Matrix ----------
def markov_matrix(text):
    matrix = {}
    for a, b in zip(text, text[1:]):
        if a not in matrix:
            matrix[a] = Counter()
        matrix[a][b] += 1
    states = sorted(matrix.keys())
    size = len(states)
    prob_matrix = np.zeros((size, size))
    for i, row in enumerate(states):
        total = sum(matrix[row].values())
        for j, col in enumerate(states):
            prob_matrix[i][j] = matrix[row][col] / total if total > 0 else 0
    return states, prob_matrix

# ---------- 4. Chi-squared ----------
def chi_squared_test(text1, text2):
    freq1 = np.array(list(Counter(text1).values()))
    freq2 = np.array(list(Counter(text2).values()))
    min_len = min(len(freq1), len(freq2))
    freq1, freq2 = freq1[:min_len], freq2[:min_len]
    stat, p, _, _ = chi2_contingency([freq1, freq2])
    return stat, p

# ---------- 5. KL Divergence ----------
def kl_divergence(text_p, text_q):
    p = Counter(text_p)
    q = Counter(text_q)
    all_keys = set(p.keys()).union(q.keys())
    p_dist = np.array([p[k] for k in all_keys], dtype=float)
    q_dist = np.array([q[k] for k in all_keys], dtype=float)
    p_dist /= p_dist.sum()
    q_dist /= q_dist.sum()
    return scipy_entropy(p_dist, q_dist)

# ---------- 6. Landauer Thermodynamic Cost ----------
def landauer_cost(bits, temp_K=300):
    k = 1.380649e-23  # Boltzmann constant (J/K)
    return bits * k * temp_K * math.log(2)

# ---------- Example Execution ----------
if __name__ == "__main__":
    with open("sample.txt", "r", encoding="utf-8") as f:
        text = f.read().replace("\n", "")

    print("Entropy:", shannon_entropy(text))
    print("Huffman Compression Ratio:", huffman_compression_ratio(text))
    states, matrix = markov_matrix(text)
    print("Markov Matrix (first 5 states):", states[:5], matrix[:5, :5])
    print("Landauer Cost (room temp):", landauer_cost(len(text)))
