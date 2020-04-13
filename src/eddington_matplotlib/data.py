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
    fig = get_figure()
    title(plot_configuration.data_title, fig=fig)
    label_axes(
        xlabel=plot_configuration.xlabel, ylabel=plot_configuration.ylabel, fig=fig
    )
    grid(plot_configuration.grid, fig=fig)
    errorbar(x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr, fig=fig)
    show_or_export(output_path=output_path, fig=fig)
