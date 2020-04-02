import numpy as np

from eddington.matplotlib.configuration import PlotConfiguration
from eddington.matplotlib.util import (
    title,
    label_axes,
    errorbar,
    plot,
    show_or_export,
    grid,
)


def plot_fitting(
    func,
    data,
    plot_configuration: PlotConfiguration,
    a: np.ndarray,
    step: float = None,
):
    title(plot_configuration.title)
    label_axes(xlabel=plot_configuration.xlabel, ylabel=plot_configuration.ylabel)
    grid(plot_configuration.grid)
    errorbar(x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr)
    if step is None:
        step = (plot_configuration.xmax - plot_configuration.xmin) / 1000.0
    x = np.arange(plot_configuration.xmin, plot_configuration.xmax, step=step)
    y = func(a, x)
    plot(x, y)
    show_or_export(plot_configuration.fitting_output_path)