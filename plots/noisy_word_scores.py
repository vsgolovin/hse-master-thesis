from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mplstyle import change_mpl_defaults

INP_DIR = Path("data/wscore_vs_noise")

# noise types
noise_labels = pd.read_csv(INP_DIR / "noise_labels.csv")
# columns are [index, label], just convert to array of labels
noise_labels = noise_labels.iloc[:, 1].to_numpy()

# word ids to actual words
words = {}  # word_id -> word
with open("data/words.txt", "r") as fin:
    for line in fin:
        word, word_id = line.rstrip().split(" ")
        words[word_id] = word
word_ids = sorted(words.keys())

# read results -- word scores for different background noises
results = np.zeros((len(noise_labels), len(words)), dtype=np.float_)
for i in range(len(noise_labels)):
    wscores = pd.read_csv(INP_DIR / f"word_scores_{i}.csv", header=None)
    assert wscores.loc[:, 0].to_list() == word_ids
    results[i] = wscores.iloc[:, 1]

change_mpl_defaults()
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1, sharex=True)
fig.subplots_adjust(left=0.2, right=0.8)
fig.set_size_inches(3.5, 4.0)
ax1.bar([words[wid] for wid in word_ids], results[0])
ax1.set_ylim(0.85, 1.0)
ax1.set_ylabel("Точность (без шума)")
for i in range(1, len(noise_labels)):
    ax2.plot((results[i] - results[0]) / results[0], label=noise_labels[i])
ax2.set_ylabel("Отн. изменение точности")
ax2.tick_params(axis="x", labelrotation=90)
fig.savefig("plots/noisy_word_scores.pdf")
