from typing import Union
from dataclasses import dataclass
import numpy as np
from numbers import Number


@dataclass
class PlotConfiguration:
    xmin: float
    xmax: float
    xlabel: Union[str, None] = None
    ylabel: Union[str, None] = None
    title: Union[str, None] = None
    residuals_title: Union[str, None] = None
    grid: bool = False
    export_result: bool = True
    plot_fitting: bool = True
    plot_residuals: bool = True
    plot_data: bool = False

    @classmethod
    def build(
        cls,
        base_name,
        title=None,
        residuals_title=None,
        xcolumn=None,
        ycolumn=None,
        xlabel=None,
        ylabel=None,
        **kwargs,
    ):
        base_name = base_name.title().replace("_", " ")
        title = cls.__get_title(base_name=base_name, title=title)
        residuals_title = cls.__get_residuals_title(
            title=title, residuals_title=residuals_title
        )
        return PlotConfiguration(
            xlabel=cls.__get_label(xcolumn, xlabel),
            ylabel=cls.__get_label(ycolumn, ylabel),
            title=title,
            residuals_title=residuals_title,
            **kwargs,
        )

    @classmethod
    def get_plot_borders(cls, x):
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
    def __get_residuals_title(cls, residuals_title, title):
        if residuals_title is not None:
            return residuals_title
        return f"{title} - Residuals"
