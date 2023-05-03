import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/word_sweep.csv")
df_paper = pd.read_csv("data/word_sweep_paper.csv")

plt.figure()
plt.plot(df["T"], df["acc"], label="полученный результат")
plt.plot(df_paper["T"], df_paper["acc"], label="Seurin et al.")
plt.legend()
plt.xlabel(r"Количество спрашиваемых слов $T$")
plt.ylabel("Точность Guesser")
plt.savefig("plots/word_sweep.pdf")
