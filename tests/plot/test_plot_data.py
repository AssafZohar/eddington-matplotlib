from pathlib import Path
import pytest

from eddington_matplotlib import plot_data, PlotConfiguration
from tests.plot import (
    check_error_bar,
    base_kwargs,
    data,
    check_x_label,
    check_y_label,
    check_show_or_export,
    check_grid,
    check_title,
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
        dict(kwargs=dict(data_title="Data Title", **base_kwargs), output_path=None),
        dict(kwargs=base_kwargs, output_path=Path("/dir/to/output/linear_data.png")),
        dict(kwargs=dict(grid=True, **base_kwargs), output_path=None),
    ]
)
def plot_data_fixture(request, plt_mock):
    param = request.param
    kwargs, output_path = param["kwargs"], param["output_path"]
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
