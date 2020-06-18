from pytest_cases import fixture_plus, cases_data

from eddington_matplotlib import plot_residuals, PlotConfiguration
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
    xmin,
    xmax,
)
import tests.plot.plot_cases as cases


@fixture_plus
@cases_data(module=cases)
def plot_residuals_fixture(case_data, plt_mock):
    kwargs, output_path = case_data.get()
    plot_configuration = PlotConfiguration(**kwargs)
    plot_residuals(
        func=dummy_func,
        data=data,
        a=a,
        plot_configuration=plot_configuration,
        output_path=output_path,
    )
    return plt_mock, dict(output_path=output_path, **kwargs)


def test_title(plot_residuals_fixture):
    mocks, expected = plot_residuals_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_title(plt=plt, figure=figure, title=expected.get("residuals_title", None))


def test_xlabel(plot_residuals_fixture):
    mocks, expected = plot_residuals_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_x_label(plt=plt, figure=figure, xlabel=expected.get("xlabel", None))


def test_ylabel(plot_residuals_fixture):
    mocks, expected = plot_residuals_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_y_label(plt=plt, figure=figure, ylabel=expected.get("ylabel", None))


def test_show_or_export(plot_residuals_fixture):
    mocks, expected = plot_residuals_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_show_or_export(
        plt=plt, figure=figure, output_path=expected.get("output_path", None)
    )


def test_grid(plot_residuals_fixture):
    mocks, expected = plot_residuals_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_grid(plt=plt, figure=figure, grid=expected.get("grid", False))


def test_horizontal_line(plot_residuals_fixture):
    mocks, expected = plot_residuals_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    plt.hlines.assert_called_with(
        0, xmin=xmin, xmax=xmax, linestyles="dashed", figure=figure
    )


def test_error_bar(plot_residuals_fixture):
    mocks, expected = plot_residuals_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_error_bar(plt=plt, y=data.y - dummy_func(a, data.x))


def test_plot(plot_residuals_fixture):
    mocks, expected = plot_residuals_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    plt.plot.assert_not_called()
