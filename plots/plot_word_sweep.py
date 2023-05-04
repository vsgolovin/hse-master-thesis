import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mplstyle import change_mpl_defaults


df = pd.read_csv("data/word_sweep.csv")
df_paper = pd.read_csv("data/word_sweep_paper.csv")

change_mpl_defaults()

plt.figure()
plt.plot(df["T"], df["acc"], label="полученный результат")
plt.plot(df_paper["T"], df_paper["acc"], label="Seurin et al.")
plt.legend()
plt.xlabel(r"Количество запрашиваемых слов $T$")
plt.xlim(-1, 21)
plt.xticks(np.arange(0, 21, 5))
plt.ylabel(r"Точность Guesser ($K = 5$)")
plt.ylim(0.48, 1.02)
plt.yticks(np.arange(0.5, 1.01, 0.1))
plt.savefig("plots/word_sweep.pdf")
