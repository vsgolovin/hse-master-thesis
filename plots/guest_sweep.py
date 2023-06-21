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
    ax.text(0.015, 0.04, "(b)", transform=ax.transAxes)
    return fig, ax


@cli.command()
def guesser():
    df = pd.read_csv("data/guest_sweep.csv")
    df_paper = pd.read_csv("data/guest_sweep_paper.csv")
    fig, ax = get_figure_axes(r"Number of speakers $K$",
                              r"Guesser accuracy ($T = 3$)")
    ax.plot(df["K"], df["acc"], label="our results")
    ax.plot(df_paper["K"], df_paper["acc"], label="Seurin et al.")
    ax.legend()
    ax.set_ylim(0.2, 1.0)
    ax.set_yticks(np.arange(0.2, 1.01, 0.1))
    fig.savefig("plots/guest_sweep.pdf")


@cli.command()
def enquirer():
    df_e = pd.read_csv("data/guest_sweep_enq_ee.csv")
    df_g = pd.read_csv("data/guest_sweep.csv")
    fig, ax = get_figure_axes(r"Number of speakers $K$",
                              r"SR Module accuracy ($T = 3$)")
    ax.plot(df_e["K"], df_e["acc"], label="Enquirer")
    ax.plot(df_g["K"], df_g["acc"], label="random agent")
    ax.legend(loc="lower center")
    ax.set_ylim(0.5, 1.0)
    ax.set_yticks(np.arange(0.5, 1.01, 0.1))
    fig.savefig("plots/guest_sweep_enq.pdf")


@cli.command()
def heuristic():
    df_e = pd.read_csv("data/guest_sweep_enq_ee.csv")
    df_g = pd.read_csv("data/guest_sweep_heuristic.csv")
    fig, ax = get_figure_axes(r"Number of speakers $K$",
                              r"SR Module accuracy ($T = 3$)")
    ax.plot(df_e["K"], df_e["acc"], label="Enquirer")
    ax.plot(df_g["K"], df_g["acc"], label="heuristic (4 words)")
    ax.legend()
    ax.set_ylim(0.75, 1.0)
    ax.set_yticks(np.arange(0.75, 1.01, 0.05))
    fig.savefig("plots/guest_sweep_heuristic.pdf")


if __name__ == "__main__":
    cli()
