import matplotlib as mpl


MPL_RCPARAMS = {
    "figure.figsize": [3.5, 2.2],
    "figure.subplot.bottom": 0.2,
    "figure.subplot.left": 0.15,
    "figure.subplot.right": 0.85,
    "figure.subplot.top": 0.9,
    "figure.dpi": 300,
    "legend.frameon": False,
    "lines.linewidth": 1.0,
    "lines.markersize": 3.0,
    "font.size": 8.0,
    "text.usetex": False,
    "xtick.direction": "in",
    "xtick.major.size": 2.0,
    "xtick.minor.size": 1.0,
    "xtick.top": True,
    "ytick.direction": "in",
    "ytick.major.size": 2.0,
    "ytick.minor.size": 1.0,
    "ytick.right": True
}


def change_mpl_defaults():
    mpl.rcParams.update(MPL_RCPARAMS)
