import pytest
from pytest_cases import cases_data, THIS_MODULE
from typing import Union

from eddington_matplotlib import PlotConfiguration


delta = 1e-5

xmin = 0.2
xmax = 9.8
base_name = "Base Name"
grid = False
xcolumn: Union[str, float, None] = "x_column_example"
ycolumn: Union[str, float, None] = "y_column_example"
default_title = "Base Name Fitting"
default_data_title = "Base Name Fitting - Data"
default_residuals_title = "Base Name Fitting - Residuals"

common_kwargs = dict(
    base_name=base_name, xmin=xmin, xmax=xmax, xcolumn=xcolumn, ycolumn=ycolumn,
)


def case_no_kwargs():
    return PlotConfiguration.build(**common_kwargs), dict()


def case_x_label_override():
    kwargs = dict(xlabel="some x label")
    return PlotConfiguration.build(**common_kwargs, **kwargs), kwargs


def case_y_label_override():
    kwargs = dict(ylabel="some y label")
    return PlotConfiguration.build(**common_kwargs, **kwargs), kwargs


def case_both_x_and_y_label_override():
    kwargs = dict(xlabel="some x label", ylabel="some y label")
    return PlotConfiguration.build(**common_kwargs, **kwargs), kwargs


def case_both_x_and_y_wth_number_headers():
    kwargs = dict(xcolumn=5.2, ycolumn=2)
    return (
        PlotConfiguration.build(base_name=base_name, xmin=xmin, xmax=xmax, **kwargs),
        dict(xlabel=None, ylabel=None),
    )


def case_title():
    title = "An Awesome Title"
    residuals_title = "An Awesome Title - Residuals"
    data_title = "An Awesome Title - Data"
    kwargs = dict(title=title)
    return (
        PlotConfiguration.build(**common_kwargs, **kwargs),
        dict(title=title, residuals_title=residuals_title, data_title=data_title),
    )


def case_residuals_title():
    residuals_title = "An Awesome Residuals Title"
    kwargs = dict(residuals_title=residuals_title)
    return (
        PlotConfiguration.build(**common_kwargs, **kwargs),
        dict(residuals_title=residuals_title),
    )


def case_data_title():
    data_title = "An Awesome Data Title"
    kwargs = dict(data_title=data_title)
    return (
        PlotConfiguration.build(**common_kwargs, **kwargs),
        dict(data_title=data_title),
    )


def case_grid():
    return (
        PlotConfiguration.build(**common_kwargs, grid=True),
        dict(grid=True),
    )


@cases_data(module=THIS_MODULE)
def test_xmin(case_data):
    plot_configuration, _ = case_data.get()
    assert xmin == pytest.approx(
        plot_configuration.xmin, rel=delta
    ), "X min value is different than expected"


@cases_data(module=THIS_MODULE)
def test_xmax(case_data):
    plot_configuration, _ = case_data.get()
    assert xmax == pytest.approx(
        plot_configuration.xmax, rel=delta
    ), "X max value is different than expected"


@cases_data(module=THIS_MODULE)
def test_xlabel(case_data):
    plot_configuration, expected = case_data.get()
    xlabel = expected.get("xlabel", xcolumn)
    assert plot_configuration.xlabel == xlabel, "X label is different than expected"


@cases_data(module=THIS_MODULE)
def test_ylabel(case_data):
    plot_configuration, expected = case_data.get()
    ylabel = expected.get("ylabel", ycolumn)
    assert plot_configuration.ylabel == ylabel, "Y label is different than expected"


@cases_data(module=THIS_MODULE)
def test_title(case_data):
    plot_configuration, expected = case_data.get()
    title = expected.get("title", default_title)
    assert plot_configuration.title == title, "Title is different than expected"


@cases_data(module=THIS_MODULE)
def test_residuals_title(case_data):
    plot_configuration, expected = case_data.get()
    residuals_title = expected.get("residuals_title", default_residuals_title)
    assert (
        plot_configuration.residuals_title == residuals_title
    ), "Residuals title is different than expected"


@cases_data(module=THIS_MODULE)
def test_data_title(case_data):
    plot_configuration, expected = case_data.get()
    data_title = expected.get("data_title", default_data_title)
    assert (
        plot_configuration.data_title == data_title
    ), "Data title is different than expected"


@cases_data(module=THIS_MODULE)
def test_grid(case_data):
    plot_configuration, expected = case_data.get()
    if expected.get("grid", False):
        assert plot_configuration.grid, "Grid should be true"
    else:
        assert not plot_configuration.grid, "Grid should be false"
