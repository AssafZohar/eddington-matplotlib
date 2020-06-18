from pathlib import Path
from typing import Optional

import numpy as np
import pytest
from mock import patch, call

from eddington_core import FitData, fit_function
from eddington_matplotlib import PlotConfiguration

delta = 1e-5
decimal = 5


@fit_function(n=2, save=False)
def dummy_func(a, x):
    return a[0] + a[1] * x


data = FitData.random(dummy_func)


def check_error_bar(plt, y):
    assert (
        1 == plt.errorbar.call_count
    ), "errorbar call count is different than expected"
    assert 0 == len(
        plt.errorbar.call_args_list[0].args
    ), "errorbar arguments number is different than expected"
    assert 8 == len(
        plt.errorbar.call_args_list[0].kwargs
    ), "errorbar keyword arguments number is different than expected"
    assert data.x == pytest.approx(
        plt.errorbar.call_args_list[0].kwargs["x"], rel=delta
    ), "X is different than expected"
    assert y == pytest.approx(
        plt.errorbar.call_args_list[0].kwargs["y"], rel=delta
    ), "Y is different than expected"
    assert data.xerr == pytest.approx(
        plt.errorbar.call_args_list[0].kwargs["xerr"], rel=delta
    ), "X error is different than expected"
    assert data.yerr == pytest.approx(
        plt.errorbar.call_args_list[0].kwargs["yerr"], rel=delta
    ), "Y error is different than expected"
    assert (
        1 == plt.errorbar.call_args_list[0].kwargs["markersize"]
    ), "markersize is different than expected"
    assert (
        "o" == plt.errorbar.call_args_list[0].kwargs["marker"]
    ), "marker is different than expected"
    assert (
        "None" == plt.errorbar.call_args_list[0].kwargs["linestyle"]
    ), "linestyle is different than expected"


def check_titles(plt, figure, titles=None):
    if titles is None or len(titles) == 0:
        plt.title.assert_not_called()
        return
    assert plt.title.call_count == len(
        titles
    ), "Title function has been called unexpected times"
    for i, title in enumerate(titles):
        assert plt.title.call_args_list[i] == call(
            title, figure=figure
        ), f"Title call number {i} is different than expected"


def check_x_label(plt, figure, xlabel=None):
    if xlabel is None:
        plt.xlabel.assert_not_called()
    else:
        plt.xlabel.assert_called_once_with(xlabel, figure=figure)


def check_y_label(plt, figure, ylabel=None):
    if ylabel is None:
        plt.ylabel.assert_not_called()
    else:
        plt.ylabel.assert_called_once_with(ylabel, figure=figure)


def check_show_or_export(plt, figure, output_path=None):
    if output_path is None:
        plt.show.assert_called_once_with()
        figure.savefig.assert_not_called()
    else:
        plt.show.assert_not_called()
        figure.savefig.assert_called_once_with(output_path)


def check_grid(plt, figure, grid=False):
    if grid:
        plt.grid.assert_called_with(True, figure=figure)
    else:
        plt.grid.assert_not_called()


class PlotBaseTestCase:
    decimal = decimal

    a = np.array([1.1, 1.92])
    data = data
    xlabel: Optional[str] = None
    ylabel: Optional[str] = None
    title: Optional[str] = None
    data_title: Optional[str] = None
    residuals_title: Optional[str] = None
    expected_title: Optional[str] = None

    grid = False
    output_path: Optional[Path] = None

    xmin = -1
    xmax = 1

    def setUp(self):
        plot_patcher = patch("eddington_matplotlib.util.plt")
        self.plt = plot_patcher.start()
        self.figure = self.plt.figure.return_value

        self.addCleanup(plot_patcher.stop)

        self.plot_configuration = PlotConfiguration(
            xlabel=self.xlabel,
            ylabel=self.ylabel,
            data_title=self.data_title,
            title=self.title,
            residuals_title=self.residuals_title,
            xmin=self.xmin,
            xmax=self.xmax,
            grid=self.grid,
        )

    @classmethod
    def func(cls, a, x):
        return a[0] + a[1] * x

    def test_title(self):
        titles = [
            title
            for title in [self.data_title, self.title, self.residuals_title]
            if title is not None
        ]
        check_titles(plt=self.plt, figure=self.figure, titles=titles)

    def test_xlabel(self):
        check_x_label(plt=self.plt, figure=self.figure, xlabel=self.xlabel)

    def test_ylabel(self):
        check_y_label(plt=self.plt, figure=self.figure, ylabel=self.ylabel)

    def test_show_or_export(self):
        check_show_or_export(
            plt=self.plt, figure=self.figure, output_path=self.output_path
        )

    def test_grid(self):
        check_grid(plt=self.plt, figure=self.figure, grid=self.grid)
