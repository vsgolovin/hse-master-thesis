import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import click
from mplstyle import change_mpl_defaults


@click.group()
def cli():
    pass


def get_figure_axes(xlabel, ylabel):
    change_mpl_defaults()
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax


@cli.command()
def guesser():
    df = pd.read_csv("data/word_sweep.csv")
    df_paper = pd.read_csv("data/word_sweep_paper.csv")
    fig, ax = get_figure_axes(r"Количество запрашиваемых слов $T$",
                              r"Точность Guesser ($K = 5$)")
    ax.plot(df["T"], df["acc"], label="полученный результат")
    ax.plot(df_paper["T"], df_paper["acc"], label="Seurin et al.")
    ax.legend()
    ax.set_xlim(-1, 21)
    ax.set_xticks(np.arange(0, 21, 5))
    ax.set_ylim(0.48, 1.02)
    ax.set_yticks(np.arange(0.5, 1.01, 0.1))
    fig.savefig("plots/word_sweep.pdf")


@cli.command()
def enquirer():
    df_e = pd.read_csv("data/word_sweep_enq_ee.csv")
    df_g = pd.read_csv("data/word_sweep.csv")
    fig, ax = get_figure_axes(r"Количество запрашиваемых слов $T$",
                              r"Точность SR Module ($K = 5$)")
    ax.plot(df_e["T"], df_e["acc"], label="Enquirer")
    ax.plot(df_g["T"], df_g["acc"], label="random agent")
    ax.legend()
    ax.set_xlim(-1, 16)
    ax.set_xticks(np.arange(0, 16, 5))
    ax.set_ylim(0.73, 1.02)
    ax.set_yticks(np.arange(0.75, 1.01, 0.05))
    fig.savefig("plots/word_sweep_enq.pdf")


@cli.command()
def heuristic():
    df_e = pd.read_csv("data/word_sweep_enq_ee.csv")
    df_g = pd.read_csv("data/word_sweep_heuristic.csv")
    fig, ax = get_figure_axes(r"Количество запрашиваемых слов $T$",
                              r"Точность SR Module ($K = 5$)")
    ax.plot(df_e["T"], df_e["acc"], marker=".", label="Enquirer")
    ax.plot(df_g["T"], df_g["acc"], marker=".", label="эвристика")
    ax.legend()
    ax.set_xlim(-1, 16)
    ax.set_xticks(np.arange(0, 16, 5))
    ax.set_ylim(0.88, 1.02)
    ax.set_yticks(np.arange(0.9, 1.01, 0.05))
    fig.savefig("plots/word_sweep_heuristic.pdf")


if __name__ == "__main__":
    cli()
