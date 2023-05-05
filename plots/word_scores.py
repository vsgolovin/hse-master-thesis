import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mplstyle import change_mpl_defaults


def main():
    # read data
    scores = {}  # word_id -> score
    with open("data/word_scores.csv", "r") as fin:
        for line in fin:
            word_id, score = line.rstrip().split(",")
            scores[word_id] = float(score)
    words = {}  # word_id -> word
    with open("data/words.txt", "r") as fin:
        for line in fin:
            word, word_id = line.rstrip().split(" ")
            words[word_id] = word

    # arrays for plotting
    word_ids = sorted(words.keys())
    assert sorted(scores.keys()) == word_ids
    word_ids = word_ids[::-1]
    ticks = np.arange(len(word_ids))
    labels = [words[wid] for wid in word_ids]
    values = [scores[wid] for wid in word_ids]

    # actual plotting
    change_mpl_defaults()
    mpl.rc("ytick", left=False, right=False)
    fig = plt.figure(figsize=(2.2, 3.5))
    fig.subplots_adjust(bottom=0.15, top=0.93, left=0.22, right=0.9)
    ax = fig.gca()
    gap = 0.2
    height = 1 - gap
    ax.barh(ticks, values, height=height)
    ax.set_ylim(-height / 2 - gap, len(word_ids) - height / 2)
    ax.set_yticks(ticks)
    ax.set_yticklabels(labels)
    # w_min = min(values)
    # x_min = max(w_min - (1 - w_min) * 0.2, 0.0)
    ax.set_xlim(0.88, 1.0)
    ax.set_xticks(np.arange(0.9, 1.01, 0.05))
    ax.set_xticks(np.arange(0.88, 1.01, 0.01), minor=True)
    ax.set_xlabel("Marginal accuracy")
    fig.savefig("plots/word_scores.pdf")


if __name__ == "__main__":
    main()
