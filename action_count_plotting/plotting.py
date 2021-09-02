import pandas as pd
import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from matplotlib import ticker


def _plot_percentage(df: pd.DataFrame, category_names: List[str], figsize: Tuple[float]) -> None:
    """
    Internal function for plotting percentages of actions spent between different categories in
    category_names.
    :param df: data read from Counts.csv in pandas DataFrame
    :param category_names: categories of actions being considered and plotted
    :param figsize: (Optional) specified figure size in (width, height)
    :return: a plot is shown
    """
    data = df[category_names].to_numpy(dtype=float)
    user_labels = df["File Name"].to_numpy(dtype=str)
    data_labels = df[category_names].to_numpy(dtype=int)
    for i in range(len(data)):
        temp_sum = sum(data[i])
        for j in range(6):
            data[i][j] /= temp_sum

    fig, ax = plt.subplots(figsize=figsize)
    category_colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, data.shape[1]))  # Set colour

    ax.invert_yaxis()
    ax.set_xlim(0, 1)
    ax.set_ylabel("Users")
    data_cum = data.cumsum(axis=1)
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(user_labels, widths, left=starts, label=colname, color=color)
        ax.bar_label(rects, labels=data_labels[:, i], label_type='center', color="black")

    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1), loc='lower left')
    ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))

    plt.tight_layout()
    plt.show()


def design_space_percentage(df: pd.DataFrame, figsize=(10.5, 8)) -> None:
    """
    Visualize the percentage of actions spent in different design spaces
    :param df: data read from Counts.csv in pandas DataFrame
    :param figsize: (Optional) specified figure size in (width, height)
    :return: a plot is shown
    """
    category_names = ["Sketching", "3D Features", "Mating", "Visualizing", "Browsing",
                      "Other Organizing"]
    _plot_percentage(df, category_names, figsize)


def action_type_percentage(df: pd.DataFrame, figsize=(9, 8)) -> None:
    """
    Visualize the percentage of actions spent in different action types
    :param df: data read from Counts.csv in pandas DataFrame
    :param figsize: (Optional) specified figure size in (width, height)
    :return: a plot is shown
    """
    category_names = ["Creating", "Editing", "Deleting", "Reversing", "Viewing", "Other"]
    _plot_percentage(df, category_names, figsize)


def cr_ratio(df: pd.DataFrame, figsize=(6, 5)) -> None:
    """
    Visualize the creation/revision ratio of every individual user
    :param df: data read from Counts.csv in pandas DataFrame
    :param figsize: (Optional) specified figure size in (width, height)
    :return: a plot is shown
    """
    data = pd.DataFrame(df)
    data["cr"] = df["Creating"] / (df["Editing"] + df["Deleting"] + df["Reversing"])
    cr = df["cr"].to_numpy()
    user_labels = df["File Name"].to_numpy(dtype=str)

    fig, ax = plt.subplots(figsize=figsize)

    ind = np.arange(len(user_labels))
    p = ax.bar(ind, cr)
    ax.set_ylabel('Ratio of Creation/Revision')
    ax.set_xticks(ind)
    ax.set_xticklabels(user_labels)
    ax.set_xlabel("Users")
    ax.bar_label(p, fmt="%.2f", label_type='edge', padding=2)

    plt.tight_layout()
    plt.show()
