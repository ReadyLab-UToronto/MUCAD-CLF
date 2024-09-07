import pandas as pd
import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from matplotlib import ticker


def _plot_percentage(df: pd.DataFrame, category_names: List[str], fig_size: Tuple[float],
                     save_fig: str) -> None:
    """
    Internal function for plotting percentages of actions spent between different categories in
    category_names.
    :param df: data read from Counts.csv in pandas DataFrame
    :param category_names: categories of actions being considered and plotted
    :param fig_size: (Optional) specified figure size in (width, height)
    :param save_fig: (Optional) if not None, the plot will be saved with the specified name in png
    :return: a plot is shown and saved if specified
    """
    data = df[category_names].to_numpy(dtype=float)
    user_labels = df["File Name"].to_numpy(dtype=str)
    data_labels = df[category_names].to_numpy(dtype=int)
    for i in range(len(data)):
        temp_sum = sum(data[i])
        for j in range(6):
            data[i][j] /= temp_sum

    fig, ax = plt.subplots(figsize=fig_size)
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
    if save_fig:
        plt.savefig(save_fig + ".png")
    plt.show()


def design_space_percentage(df: pd.DataFrame, fig_size=(10.5, 8), save_fig="") -> None:
    """
    Visualize the percentage of actions spent in different design spaces
    :param df: data read from Counts.csv in pandas DataFrame
    :param fig_size: (Optional) specified figure size in (width, height)
    :param save_fig: (Optional) if not None, the plot will be saved with the specified name in png
    :return: a plot is shown and saved if specified
    """
    category_names = ["Sketching", "3D Features", "Mating", "Visualizing", "Browsing",
                      "Other Organizing"]
    _plot_percentage(df, category_names, fig_size, save_fig)


def action_type_percentage(df: pd.DataFrame, fig_size=(9, 8), save_fig="") -> None:
    """
    Visualize the percentage of actions spent in different action types
    :param df: data read from Counts.csv in pandas DataFrame
    :param fig_size: (Optional) specified figure size in (width, height)
    :param save_fig: (Optional) if not None, the plot will be saved with the specified name in png
    :return: a plot is shown and saved if specified
    """
    category_names = ["Creating", "Editing", "Deleting", "Reversing", "Viewing", "Other"]
    _plot_percentage(df, category_names, fig_size, save_fig)


def cr_ratio(df: pd.DataFrame, fig_size=(6, 6), save_fig="") -> None:
    """
    Visualize the creation/revision ratio of every individual user
    :param df: data read from Counts.csv in pandas DataFrame
    :param fig_size: (Optional) specified figure size in (width, height)
    :param save_fig: (Optional) if not None, the plot will be saved with the specified name in png
    :return: a plot is shown and saved if specified
    """
    data = pd.DataFrame(df)
    data["cr"] = df["Creating"] / (df["Editing"] + df["Deleting"] + df["Reversing"])
    cr = data["cr"].to_numpy()
    user_labels = df["File Name"].to_numpy(dtype=str)

    fig, ax = plt.subplots(figsize=fig_size)

    ind = np.arange(len(user_labels))
    p = ax.bar(ind, cr)
    ax.set_ylabel('Ratio of Creation/Revision')
    ax.set_xticks(ind)
    ax.set_xticklabels(user_labels)
    ax.set_xlabel("Users")
    ax.bar_label(p, fmt="%.2f", label_type='edge', padding=2)

    plt.tight_layout()
    if save_fig:
        plt.savefig(save_fig + ".png")
    plt.show()


def plot_contribution(df: pd.DataFrame, analyzing_category: str, fig_size=(6, 6),
                      save_fig="") -> None:
    """
    Visualize the percentage contribution of every individual user in the specified action category.
    :param df: data read from Counts.csv in pandas DataFrame
    :param analyzing_category:
    :param fig_size: (Optional) specified figure size in (width, height)
    :param save_fig: (Optional) if not None, the plot will be saved with the specified name in png
    :return: a plot is shown and saved if specified
    """
    data = pd.DataFrame(df)
    file_total = df[analyzing_category].sum()
    data["contri"] = df[analyzing_category] / file_total
    contri = data["contri"].to_numpy()
    user_labels = df["User Name"].to_numpy(dtype=str)

    fig, ax = plt.subplots(figsize=fig_size)

    ind = np.arange(len(user_labels))
    p = ax.bar(ind, contri)
    ax.set_ylabel('Percentage ' + analyzing_category + ' Individual Contribution to File')
    ax.set_xticks(ind)
    ax.set_xticklabels(user_labels)
    ax.set_xlabel("Users")
    for rect in p:
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    plt.xticks(rotation=90)
    plt.tight_layout()
    if save_fig:
        plt.savefig(save_fig + ".png")
    plt.show()
