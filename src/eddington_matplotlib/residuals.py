"""Plot residuals of a fitting."""
from pathlib import Path

import numpy as np
from eddington_core import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
    get_figure,
    title,
    label_axes,
    horizontal_line,
    errorbar,
    show_or_export,
    grid,
)


def plot_residuals(
    func,
    data: FitData,
    plot_configuration: PlotConfiguration,
    a: np.ndarray,
    output_path: Path = None,
):
    """
    Plot residuals plot.

    :param func: Fitting function.
    :param data: Fitting data
    :param plot_configuration: Plot configuration
    :param a: The parameters result
    :param output_path: Path or None. output path to save the plot.
    """
    fig = get_figure()
    title(fig=fig, title_name=plot_configuration.residuals_title)
    label_axes(
        xlabel=plot_configuration.xlabel, ylabel=plot_configuration.ylabel, fig=fig
    )
    grid(fig=fig, is_grid=plot_configuration.grid)
    y_residuals = data.y - func(a, data.x)
    horizontal_line(fig=fig, xmin=plot_configuration.xmin, xmax=plot_configuration.xmax)
    errorbar(fig=fig, x=data.x, y=y_residuals, xerr=data.xerr, yerr=data.yerr)
    show_or_export(fig=fig, output_path=output_path)
