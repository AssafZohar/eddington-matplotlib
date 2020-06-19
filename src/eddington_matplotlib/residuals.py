"""Plot residuals of a fitting."""
from pathlib import Path

import numpy as np
from eddington_core import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
    get_figure,
    horizontal_line,
    errorbar,
    show_or_export,
)


def plot_residuals(  # pylint: disable=C0103
    func, data: FitData, plot_configuration: PlotConfiguration, a: np.ndarray
):
    """
    Plot residuals plot.

    :param func: Fitting function.
    :param data: Fitting data
    :param plot_configuration: Plot configuration
    :param a: The parameters result
    """
    fig = get_figure(
        title_name=plot_configuration.residuals_title,
        plot_configuration=plot_configuration,
    )
    y_residuals = data.y - func(a, data.x)
    horizontal_line(fig=fig, xmin=plot_configuration.xmin, xmax=plot_configuration.xmax)
    errorbar(fig=fig, x=data.x, y=y_residuals, xerr=data.xerr, yerr=data.yerr)
    return fig
