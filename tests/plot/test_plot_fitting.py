from pytest_cases import fixture_plus, cases_data
import pytest

from eddington_matplotlib import plot_fitting, PlotConfiguration
from tests.plot import (
    check_error_bar,
    data,
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
import tests.plot.plot_cases as cases


@fixture_plus
@cases_data(module=cases)
def plot_fitting_fixture(case_data, plt_mock):
    kwargs, output_path = case_data.get()
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
    mocks, _ = plot_fitting_fixture
    plt, _ = mocks["plt"], mocks["figure"]
    check_error_bar(plt=plt, y=data.y)


def test_plot(plot_fitting_fixture):
    mocks, _ = plot_fitting_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    assert plt.plot.call_count == 1, "Plot call count is different than expected"
    assert (
        len(plt.plot.call_args[0]) == 2
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
