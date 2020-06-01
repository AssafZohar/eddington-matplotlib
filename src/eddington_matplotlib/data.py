"""Plot fitting data."""
from eddington_core import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
    get_figure,
    label_axes,
    errorbar,
    show_or_export,
    grid,
    title,
)


def plot_data(data: FitData, plot_configuration: PlotConfiguration, output_path=None):
    """
    Plot fitting data.

    :param data: Fitting data
    :param plot_configuration: Plot configuration
    :param output_path: Path or None. output path to save the plot.
    """
    fig = get_figure()
    title(fig=fig, title_name=plot_configuration.data_title)
    label_axes(
        fig=fig, xlabel=plot_configuration.xlabel, ylabel=plot_configuration.ylabel
    )
    grid(fig=fig, is_grid=plot_configuration.grid)
    errorbar(fig=fig, x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr)
    show_or_export(fig=fig, output_path=output_path)
