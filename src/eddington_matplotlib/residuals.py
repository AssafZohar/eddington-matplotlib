from pathlib import Path

import numpy as np
from eddington_core import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
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
    title(plot_configuration.residuals_title)
    label_axes(xlabel=plot_configuration.xlabel, ylabel=plot_configuration.ylabel)
    grid(plot_configuration.grid)
    y_residuals = data.y - func(a, data.x)
    horizontal_line(plot_configuration.xmin, plot_configuration.xmax)
    errorbar(x=data.x, y=y_residuals, xerr=data.xerr, yerr=data.yerr)
    show_or_export(output_path=output_path)
