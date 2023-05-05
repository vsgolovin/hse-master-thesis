import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mplstyle import change_mpl_defaults


df_e = pd.read_csv("data/guest_sweep_enq_ee.csv")
df_g = pd.read_csv("data/guest_sweep.csv")

change_mpl_defaults()

plt.figure()
plt.plot(df_e["K"], df_e["acc"], label="Enquirer")
plt.plot(df_g["K"], df_g["acc"], label="random agent")
plt.legend()
plt.xlabel(r"Количество дикторов $K$")
plt.ylabel(r"Точность SR Module ($T = 3$)")
plt.ylim(0.5, 1.0)
plt.yticks(np.arange(0.5, 1.01, 0.1))
plt.savefig("plots/guest_sweep_enq.pdf")
