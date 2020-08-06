"""Plot fitting data."""
from eddington import FitData

from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.util import (
    get_figure,
    errorbar,
)


def plot_data(data: FitData, plot_configuration: PlotConfiguration):
    """
    Plot fitting data.

    :param data: Fitting data
    :param plot_configuration: Plot configuration
    """
    fig = get_figure(
        title_name=plot_configuration.data_title, plot_configuration=plot_configuration
    )
    errorbar(fig=fig, x=data.x, y=data.y, xerr=data.xerr, yerr=data.yerr)
    return fig
