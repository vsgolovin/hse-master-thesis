import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mplstyle import change_mpl_defaults


df = pd.read_csv("data/guest_sweep.csv")
df_paper = pd.read_csv("data/guest_sweep_paper.csv")

change_mpl_defaults()

plt.figure()
plt.plot(df["K"], df["acc"], label="полученный результат")
plt.plot(df_paper["K"], df_paper["acc"], label="Seurin et al.")
plt.legend()
plt.xlabel(r"Количество дикторов $K$")
plt.ylabel(r"Точность Guesser ($T = 3$)")
plt.ylim(0.2, 1.0)
plt.yticks(np.arange(0.2, 1.01, 0.1))
plt.savefig("plots/guest_sweep.pdf")
