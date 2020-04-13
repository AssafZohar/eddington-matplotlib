from pathlib import Path
import numpy as np
from eddington_core import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
    get_figure,
    title,
    label_axes,
    errorbar,
    plot,
    show_or_export,
    grid,
)


def plot_fitting(
    func,
    data: FitData,
    plot_configuration: PlotConfiguration,
    a: np.ndarray,
    step: float = None,
    output_path: Path = None,
):
    fig = get_figure()
    title(plot_configuration.title, fig=fig)
    label_axes(
        xlabel=plot_configuration.xlabel, ylabel=plot_configuration.ylabel, fig=fig
    )
    grid(plot_configuration.grid, fig=fig)
    errorbar(x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr, fig=fig)
    if step is None:
        step = (plot_configuration.xmax - plot_configuration.xmin) / 1000.0
    x = np.arange(plot_configuration.xmin, plot_configuration.xmax, step=step)
    y = func(a, x)
    plot(x, y, fig=fig)
    show_or_export(output_path=output_path, fig=fig)
