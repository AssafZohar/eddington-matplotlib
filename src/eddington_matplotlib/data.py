from eddington_core import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
    label_axes,
    errorbar,
    show_or_export,
    grid,
)


def plot_data(data: FitData, plot_configuration: PlotConfiguration, output_path=None):
    label_axes(xlabel=plot_configuration.xlabel, ylabel=plot_configuration.ylabel)
    grid(plot_configuration.grid)
    errorbar(x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr)
    show_or_export(output_path=output_path)
