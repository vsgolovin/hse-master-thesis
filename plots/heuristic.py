import matplotlib.pyplot as plt
import pandas as pd
from mplstyle import change_mpl_defaults


df = pd.read_csv("data/heuristic.csv")
change_mpl_defaults()
plt.figure()
plt.plot(df["w"], df["acc_nonuni"], marker=".", label="неравномерное")
plt.plot(df["w"], df["acc_uni"], marker=".", label="равномерное")
plt.axhline(0.937, color="k", linestyle="dotted")
yshift = 0.001
plt.text(2, 0.937 + yshift, "Guesser")
plt.axhline(0.975, color="k", linestyle="dotted")
plt.text(12, 0.975 + yshift, "Guesser + Enquirer")
plt.text(15.7, 0.96, "nonuniform", color="tab:blue")
plt.text(10.2, 0.951, "uniform", color="tab:orange")
plt.xlabel("Размер словаря")
plt.xlim(1, 22)
plt.xticks([3] + list(range(5, 21, 5)))
plt.ylabel(r"Точность ($K = 5$, $T = 3$)")
plt.savefig("plots/heuristic.pdf")
