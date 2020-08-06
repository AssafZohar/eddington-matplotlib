import numpy as np
import pytest
from mock import call

from eddington import FitData, fit_function


@fit_function(n=2, save=False)
def dummy_func(a, x):
    return a[0] + a[1] * x


delta = 1e-5
decimal = 5

a = np.array([1.1, 1.92])
data = FitData.random(dummy_func)
xmin = -1
xmax = 1
xrange = np.arange(xmin, xmax, step=0.002)
yrange = dummy_func(a, xrange)
base_kwargs = dict(xmin=xmin, xmax=xmax)


def check_error_bar(plt, y):
    assert (
        plt.errorbar.call_count == 1
    ), "errorbar call count is different than expected"
    assert (
        len(plt.errorbar.call_args[0]) == 0
    ), "errorbar arguments number is different than expected"
    assert (
        len(plt.errorbar.call_args[1]) == 8
    ), "errorbar keyword arguments number is different than expected"
    assert (
        pytest.approx(plt.errorbar.call_args[1]["x"], rel=delta) == data.x
    ), "X is different than expected"
    assert (
        pytest.approx(plt.errorbar.call_args[1]["y"], rel=delta) == y
    ), "Y is different than expected"
    assert (
        pytest.approx(plt.errorbar.call_args[1]["xerr"], rel=delta) == data.xerr
    ), "X error is different than expected"
    assert (
        pytest.approx(plt.errorbar.call_args[1]["yerr"], rel=delta) == data.yerr
    ), "Y error is different than expected"
    assert (
        plt.errorbar.call_args[1]["markersize"] == 1
    ), "markersize is different than expected"
    assert (
        plt.errorbar.call_args[1]["marker"] == "o"
    ), "marker is different than expected"
    assert (
        plt.errorbar.call_args[1]["linestyle"] == "None"
    ), "linestyle is different than expected"


def check_title(plt, figure, title=None):
    if title is None:
        plt.title.assert_not_called()
    else:
        plt.title.assert_called_once_with(title, figure=figure)


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
