from pytest_cases import fixture_plus

from eddington_matplotlib import plot_residuals
from tests.plot import (
    check_error_bar,
    data,
    a,
    check_title,
    check_x_label,
    check_y_label,
    check_grid,
    dummy_func,
    xmin,
    xmax,
)


@fixture_plus
def plot_residuals_fixture(configurations, plt_mock):
    plot_configuration, _ = configurations
    fig = plot_residuals(
        a=a, func=dummy_func, data=data, plot_configuration=plot_configuration,
    )
    return fig, plot_configuration, plt_mock


def test_result_figure(plot_residuals_fixture):
    figure, _, mocks = plot_residuals_fixture
    assert figure == mocks["figure"], "Returned figure is different than expected"


def test_title(plot_residuals_fixture):
    figure, plot_configuration, mocks = plot_residuals_fixture
    plt = mocks["plt"]
    check_title(plt=plt, figure=figure, title=plot_configuration.residuals_title)


def test_xlabel(plot_residuals_fixture):
    figure, plot_configuration, mocks = plot_residuals_fixture
    plt = mocks["plt"]
    check_x_label(plt=plt, figure=figure, xlabel=plot_configuration.xlabel)


def test_ylabel(plot_residuals_fixture):
    figure, plot_configuration, mocks = plot_residuals_fixture
    plt = mocks["plt"]
    check_y_label(plt=plt, figure=figure, ylabel=plot_configuration.ylabel)


def test_grid(plot_residuals_fixture):
    figure, plot_configuration, mocks = plot_residuals_fixture
    plt = mocks["plt"]
    check_grid(plt=plt, figure=figure, grid=plot_configuration.grid)


def test_horizontal_line(plot_residuals_fixture):
    figure, _, mocks = plot_residuals_fixture
    plt = mocks["plt"]
    plt.hlines.assert_called_with(
        0, xmin=xmin, xmax=xmax, linestyles="dashed", figure=figure
    )


def test_error_bar(plot_residuals_fixture):
    _, _, mocks = plot_residuals_fixture
    plt, _ = mocks["plt"], mocks["figure"]
    check_error_bar(plt=plt, y=data.y - dummy_func(a, data.x))


def test_plot(plot_residuals_fixture):
    _, _, mocks = plot_residuals_fixture
    plt, _ = mocks["plt"], mocks["figure"]
    plt.plot.assert_not_called()
