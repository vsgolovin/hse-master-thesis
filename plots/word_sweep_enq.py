import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mplstyle import change_mpl_defaults


df_e = pd.read_csv("data/word_sweep_enq_ee.csv")
df_g = pd.read_csv("data/word_sweep.csv")

change_mpl_defaults()

plt.figure()
plt.plot(df_e["T"], df_e["acc"], label="Enquirer")
plt.plot(df_g["T"], df_g["acc"], label="random agent")
plt.legend()
plt.xlabel(r"Количество запрашиваемых слов $T$")
plt.xlim(-1, 16)
plt.xticks(np.arange(0, 16, 5))
plt.ylabel(r"Точность SR Module ($K = 5$)")
plt.ylim(0.72, 1.02)
plt.yticks(np.arange(0.7, 1.01, 0.05))
plt.savefig("plots/word_sweep_enq.pdf")
