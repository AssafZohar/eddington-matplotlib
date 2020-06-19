from pytest_cases import fixture_plus

from eddington_matplotlib import plot_fitting
from tests.plot import (
    check_error_bar,
    data,
    check_x_label,
    check_y_label,
    check_grid,
    check_title,
    dummy_func,
    a,
)


@fixture_plus
def plot_fitting_fixture(configurations, plt_mock):
    plot_configuration, _ = configurations
    fig = plot_fitting(
        a=a, func=dummy_func, data=data, plot_configuration=plot_configuration,
    )
    return fig, plot_configuration, plt_mock


def test_result_figure(plot_fitting_fixture):
    figure, _, mocks = plot_fitting_fixture
    assert figure == mocks["figure"], "Returned figure is different than expected"


def test_title(plot_fitting_fixture):
    figure, plot_configuration, mocks = plot_fitting_fixture
    plt = mocks["plt"]
    check_title(plt=plt, figure=figure, title=plot_configuration.title)


def test_xlabel(plot_fitting_fixture):
    figure, plot_configuration, mocks = plot_fitting_fixture
    plt = mocks["plt"]
    check_x_label(plt=plt, figure=figure, xlabel=plot_configuration.xlabel)


def test_ylabel(plot_fitting_fixture):
    figure, plot_configuration, mocks = plot_fitting_fixture
    plt = mocks["plt"]
    check_y_label(plt=plt, figure=figure, ylabel=plot_configuration.ylabel)


def test_grid(plot_fitting_fixture):
    figure, plot_configuration, mocks = plot_fitting_fixture
    plt = mocks["plt"]
    check_grid(plt=plt, figure=figure, grid=plot_configuration.grid)


def test_error_bar(plot_fitting_fixture):
    _, _, mocks = plot_fitting_fixture
    plt, _ = mocks["plt"], mocks["figure"]
    check_error_bar(plt=plt, y=data.y)
