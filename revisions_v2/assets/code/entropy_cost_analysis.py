import os
import math
import matplotlib.pyplot as plt
from collections import Counter

# ====== CONFIGURATION ======
INPUT_FILE = "english_sample.txt"  # You can change this
FIGURE_OUT = "../../figures/entropy_drift_trend.png"  # relative path from /code/
WINDOW_SIZE = 500  # Sliding window size
STEP_SIZE = 100    # Step size for drift
ALPHABET_SIZE = 128  # Assume ASCII; adjust if needed

# ====== LOAD DATA ======
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    text = f.read().replace('\n', '')

# ====== HELPER FUNCTIONS ======
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    probabilities = [count / total for count in counts.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy

# ====== SLIDING WINDOW ENTROPY (Drift) ======
positions = []
entropies = []
normalized_entropies = []

for i in range(0, len(text) - WINDOW_SIZE + 1, STEP_SIZE):
    window = text[i:i + WINDOW_SIZE]
    H = compute_entropy(window)
    H_norm = H / math.log2(ALPHABET_SIZE)  # Normalized entropy (0 to 1)

    positions.append(i)
    entropies.append(H)
    normalized_entropies.append(H_norm)

# ====== PLOT ENTROPY DRIFT ======
plt.figure(figsize=(10, 5))
plt.plot(positions, normalized_entropies, color='darkred', linewidth=2)
plt.title("Entropy Drift Over Text Window")
plt.xlabel("Character Position")
plt.ylabel("Normalized Entropy")
plt.ylim(0, 1.1)
plt.grid(True)
plt.tight_layout()

# ====== SAVE FIGURE ======
os.makedirs(os.path.dirname(FIGURE_OUT), exist_ok=True)
plt.savefig(FIGURE_OUT)
plt.close()

print(f"Entropy drift plot saved to: {FIGURE_OUT}")

