from typing import Union
from dataclasses import dataclass
from pathlib import Path
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
    data_output_path: Union[Path, None] = None
    fitting_output_path: Union[Path, None] = None
    residuals_output_path: Union[Path, None] = None

    @classmethod
    def build(
        cls,
        func_name,
        title=None,
        residuals_title=None,
        xcolumn=None,
        ycolumn=None,
        xlabel=None,
        ylabel=None,
        output_dir=None,
        **kwargs,
    ):
        title = cls.__get_title(func_name=func_name, title=title)
        residuals_title = cls.__get_residuals_title(
            title=title, residuals_title=residuals_title
        )
        (
            data_output_path,
            fitting_output_path,
            residuals_output_path,
        ) = cls.__get_output_paths(output_dir=output_dir, func_name=func_name)
        return PlotConfiguration(
            xlabel=cls.__get_label(xcolumn, xlabel),
            ylabel=cls.__get_label(ycolumn, ylabel),
            title=title,
            residuals_title=residuals_title,
            data_output_path=data_output_path,
            fitting_output_path=fitting_output_path,
            residuals_output_path=residuals_output_path,
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
    def __get_title(cls, func_name, title):
        if title is not None:
            return title
        return f"{func_name} Fitting"

    @classmethod
    def __get_residuals_title(cls, residuals_title, title):
        if residuals_title is not None:
            return residuals_title
        return f"{title} - Residuals"

    @classmethod
    def __get_output_paths(cls, output_dir, func_name):
        if output_dir is None:
            return None, None, None

        underscore_func_name = func_name.lower().replace(" ", "_")
        data_output_path = output_dir / f"{underscore_func_name}_data.png"
        fitting_output_path = output_dir / f"{underscore_func_name}_fitting.png"
        residuals_output_path = (
            output_dir / f"{underscore_func_name}_fitting_residuals.png"
        )
        return data_output_path, fitting_output_path, residuals_output_path
