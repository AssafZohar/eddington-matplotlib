from pathlib import Path

import pytest

from eddington_matplotlib import plot_fitting, PlotConfiguration
from tests.plot import (
    check_error_bar,
    data,
    base_kwargs,
    a,
    check_title,
    check_x_label,
    check_y_label,
    check_show_or_export,
    check_grid,
    dummy_func,
    delta,
    xrange,
    yrange,
)


@pytest.fixture(
    params=[
        dict(kwargs=base_kwargs, output_path=None),
        dict(kwargs=dict(xlabel="xlabel", **base_kwargs), output_path=None),
        dict(kwargs=dict(ylabel="ylabel", **base_kwargs), output_path=None),
        dict(
            kwargs=dict(xlabel="xlabel", ylabel="ylabel", **base_kwargs),
            output_path=None,
        ),
        dict(kwargs=dict(title="Fitting Title", **base_kwargs), output_path=None),
        dict(kwargs=base_kwargs, output_path=Path("/dir/to/output/linear_data.png")),
        dict(kwargs=dict(grid=True, **base_kwargs), output_path=None),
    ]
)
def plot_fitting_fixture(request, plt_mock):
    param = request.param
    kwargs, output_path = param["kwargs"], param["output_path"]
    plot_configuration = PlotConfiguration(**kwargs)
    plot_fitting(
        func=dummy_func,
        data=data,
        a=a,
        plot_configuration=plot_configuration,
        output_path=output_path,
    )
    return plt_mock, dict(output_path=output_path, **kwargs)


def test_title(plot_fitting_fixture):
    mocks, expected = plot_fitting_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_title(plt=plt, figure=figure, title=expected.get("title", None))


def test_xlabel(plot_fitting_fixture):
    mocks, expected = plot_fitting_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_x_label(plt=plt, figure=figure, xlabel=expected.get("xlabel", None))


def test_ylabel(plot_fitting_fixture):
    mocks, expected = plot_fitting_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_y_label(plt=plt, figure=figure, ylabel=expected.get("ylabel", None))


def test_show_or_export(plot_fitting_fixture):
    mocks, expected = plot_fitting_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_show_or_export(
        plt=plt, figure=figure, output_path=expected.get("output_path", None)
    )


def test_grid(plot_fitting_fixture):
    mocks, expected = plot_fitting_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_grid(plt=plt, figure=figure, grid=expected.get("grid", False))


def test_error_bar(plot_fitting_fixture):
    mocks, expected = plot_fitting_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_error_bar(plt=plt, y=data.y)


def test_plot(plot_fitting_fixture):
    mocks, expected = plot_fitting_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    assert 1 == plt.plot.call_count, "Plot call count is different than expected"
    assert 2 == len(
        plt.plot.call_args[0]
    ), "Plot arguments count is different than expected"
    assert plt.plot.call_args[0][0] == pytest.approx(
        xrange, rel=delta
    ), "Plot x is different than expected"
    assert plt.plot.call_args[0][1] == pytest.approx(
        yrange, rel=delta
    ), "Plot y is different than expected"
    assert ["figure"] == list(
        plt.plot.call_args[1].keys()
    ), "Plot keyword arguments count is different than expected"
    assert (
        figure == plt.plot.call_args[1]["figure"]
    ), "Plot figure is different than expected"


# class TestPlotFittingWithoutLabelsAndTitle(TestCase, PlotFittingBaseTestCase):
#     def setUp(self):
#         PlotFittingBaseTestCase.setUp(self)
#
#
# class TestPlotFittingWithXlabel(TestCase, PlotFittingBaseTestCase):
#
#     xlabel = "xlabel"
#
#     def setUp(self):
#         PlotFittingBaseTestCase.setUp(self)
#
#
# class TestPlotFittingWithYlabel(TestCase, PlotFittingBaseTestCase):
#
#     ylabel = "ylabel"
#
#     def setUp(self):
#         PlotFittingBaseTestCase.setUp(self)
#
#
# class TestPlotFittingWithTitle(TestCase, PlotFittingBaseTestCase):
#
#     title = "title"
#
#     def setUp(self):
#         PlotFittingBaseTestCase.setUp(self)
#
#
# class TestPlotFittingWithLabelsAndTitle(TestCase, PlotFittingBaseTestCase):
#
#     xlabel = "xlabel"
#     ylabel = "ylabel"
#     title = "title"
#
#     def setUp(self):
#         PlotFittingBaseTestCase.setUp(self)
#
#
# class TestPlotFittingExportToFile(TestCase, PlotFittingBaseTestCase):
#
#     output_path = Path("/dir/to/output/linear_fitting.png")
#
#     def setUp(self):
#         PlotFittingBaseTestCase.setUp(self)
#
#
# class TestPlotFittingWithGrid(TestCase, PlotFittingBaseTestCase):
#     grid = True
#
#     def setUp(self):
#         PlotFittingBaseTestCase.setUp(self)
