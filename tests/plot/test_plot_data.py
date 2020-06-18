from pytest_cases import fixture_plus, cases_data

from eddington_matplotlib import plot_data, PlotConfiguration
from tests.plot import (
    check_error_bar,
    data,
    check_x_label,
    check_y_label,
    check_show_or_export,
    check_grid,
    check_title,
)
import tests.plot.plot_cases as cases


@fixture_plus
@cases_data(module=cases)
def plot_data_fixture(case_data, plt_mock):
    kwargs, output_path = case_data.get()
    plot_configuration = PlotConfiguration(**kwargs)
    plot_data(
        data=data, plot_configuration=plot_configuration, output_path=output_path,
    )
    return plt_mock, dict(output_path=output_path, **kwargs)


def test_title(plot_data_fixture):
    mocks, expected = plot_data_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_title(plt=plt, figure=figure, title=expected.get("data_title", None))


def test_xlabel(plot_data_fixture):
    mocks, expected = plot_data_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_x_label(plt=plt, figure=figure, xlabel=expected.get("xlabel", None))


def test_ylabel(plot_data_fixture):
    mocks, expected = plot_data_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_y_label(plt=plt, figure=figure, ylabel=expected.get("ylabel", None))


def test_show_or_export(plot_data_fixture):
    mocks, expected = plot_data_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_show_or_export(
        plt=plt, figure=figure, output_path=expected.get("output_path", None)
    )


def test_grid(plot_data_fixture):
    mocks, expected = plot_data_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_grid(plt=plt, figure=figure, grid=expected.get("grid", False))


def test_error_bar(plot_data_fixture):
    mocks, _ = plot_data_fixture
    plt, figure = mocks["plt"], mocks["figure"]
    check_error_bar(plt=plt, y=data.y)
