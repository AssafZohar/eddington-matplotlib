"""Configuration for the fitting results."""
from typing import Union
from dataclasses import dataclass
import numpy as np
from numbers import Number


@dataclass
class PlotConfiguration:  # pylint: disable=R0902
    """Data class for plotting fitting results."""

    xmin: float
    xmax: float
    xlabel: Union[str, None] = None
    ylabel: Union[str, None] = None
    title: Union[str, None] = None
    data_title: Union[str, None] = None
    residuals_title: Union[str, None] = None
    grid: bool = False
    print_results: bool = True
    plot_fitting: bool = True
    plot_residuals: bool = True
    plot_data: bool = False

    @classmethod
    def build(  # pylint: disable=R0913
        cls,
        base_name,
        title=None,
        data_title=None,
        residuals_title=None,
        xcolumn=None,
        ycolumn=None,
        xlabel=None,
        ylabel=None,
        **kwargs,
    ):
        """
        Build a :class:`PlotConfiguration` instance.

        :param base_name: str. Base name that titles will be generated from if not
         specified.
        :param title: str or None. Title for the fitting plot.
        :param data_title: str or None. Title for the data plot.
        :param residuals_title: str or None. Title for the residuals plot.
        :param xcolumn: str, int or None. x column specifier
        :param ycolumn: str, int or None. x column specifier
        :param xlabel: str or None. Label for the x axis.
        :param ylabel: str or None. Label for the y axis.
        :param kwargs: dict. Extra arguments.
        :return: :class:`PlotConfiguration` instance
        """
        base_name = base_name.title().replace("_", " ")
        title = cls.__get_title(base_name=base_name, title=title)
        data_title = cls.__get_data_title(title=title, data_title=data_title)
        residuals_title = cls.__get_residuals_title(
            title=title, residuals_title=residuals_title
        )
        return PlotConfiguration(
            xlabel=cls.__get_label(xcolumn, xlabel),
            ylabel=cls.__get_label(ycolumn, ylabel),
            title=title,
            data_title=data_title,
            residuals_title=residuals_title,
            **kwargs,
        )

    @classmethod
    def get_plot_borders(cls, x):  # pylint: disable=C0103
        """
        Get borders for a plot based on its x values.

        :param x: Array. x values of the fitting
        :return: tuple. minimum and maximum values for the plot.
        """
        xmin = np.min(x)
        xmax = np.max(x)
        gap = (xmax - xmin) * 0.1
        return xmin - gap, xmax + gap

    @classmethod
    def __get_label(cls, header, label):
        if label is not None:
            return label
        if isinstance(header, Number):
            return None
        return header

    @classmethod
    def __get_title(cls, base_name, title):
        if title is not None:
            return title
        return f"{base_name} Fitting"

    @classmethod
    def __get_data_title(cls, data_title, title):
        if data_title is not None:
            return data_title
        return f"{title} - Data"

    @classmethod
    def __get_residuals_title(cls, residuals_title, title):
        if residuals_title is not None:
            return residuals_title
        return f"{title} - Residuals"
