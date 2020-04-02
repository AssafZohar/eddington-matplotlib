from eddington_matplotlib import PlotConfiguration
from eddington_matplotlib.util import (
    label_axes,
    errorbar,
    show_or_export,
    grid,
)


def plot_data(data, plot_configuration: PlotConfiguration):
    label_axes(xlabel=plot_configuration.xlabel, ylabel=plot_configuration.ylabel)
    grid(plot_configuration.grid)
    errorbar(x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr)
    show_or_export(plot_configuration.data_output_path)
