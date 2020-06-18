import pytest
from pathlib import Path

from eddington_core import FitData
from mock import Mock
import numpy as np

from eddington_matplotlib import PlotConfiguration, OutputConfiguration, plot_all
from tests.plot import dummy_func


should_print_results = True
should_plot_fitting = True
should_plot_residuals = True
should_plot_data = False

xmin = 0.2
xmax = 9.8
func = dummy_func
data = FitData.random(dummy_func)
a = np.array([1, 2])
output_dir = Path("dir/to/output")


@pytest.fixture
def plot_functions_mock(mocker):

    plot_data = mocker.patch("eddington_matplotlib.all.plot_data")
    plot_fitting = mocker.patch("eddington_matplotlib.all.plot_fitting")
    plot_residuals = mocker.patch("eddington_matplotlib.all.plot_residuals")
    result = Mock()
    result.a = a
    return dict(
        plot_data=plot_data,
        plot_fitting=plot_fitting,
        plot_residuals=plot_residuals,
        result=result,
    )


@pytest.fixture(
    params=[
        dict(),
        dict(plot_data=True),
        dict(plot_fitting=False),
        dict(plot_residuals=False),
        dict(print_results=False),
    ]
)
def case_data(request, plot_functions_mock):
    kwargs = request.param
    plot_configuration = PlotConfiguration.build(
        base_name=func.name, xmin=xmin, xmax=xmax, **kwargs
    )
    output_configuration = OutputConfiguration.build(
        base_name=func.name, output_dir=output_dir
    )

    plot_all(
        func=func,
        data=data,
        plot_configuration=plot_configuration,
        output_configuration=output_configuration,
        result=plot_functions_mock["result"],
    )
    inp = dict(
        plot_configuration=plot_configuration,
        output_configuration=output_configuration,
        kwargs=kwargs,
    )
    return inp, plot_functions_mock


def test_export_result(case_data):
    inp, mocks = case_data
    kwargs = inp["kwargs"]
    result = mocks["result"]
    if kwargs.get("print_results", True):
        result.print_or_export.assert_called_once_with(
            inp["output_configuration"].result_output_path,
        )
    else:
        result.print_or_export.assert_not_called()


def test_plot_data(case_data):
    inp, mocks = case_data
    kwargs = inp["kwargs"]
    if kwargs.get("plot_data", False):
        mocks["plot_data"].assert_called_once_with(
            data=data,
            plot_configuration=inp["plot_configuration"],
            output_path=inp["output_configuration"].data_output_path,
        )
    else:
        mocks["plot_data"].assert_not_called()


def test_plot_fitting(case_data):
    inp, mocks = case_data
    kwargs = inp["kwargs"]
    result = mocks["result"]
    if kwargs.get("plot_fitting", True):
        mocks["plot_fitting"].assert_called_once_with(
            func=func,
            data=data,
            a=result.a,
            plot_configuration=inp["plot_configuration"],
            output_path=inp["output_configuration"].fitting_output_path,
        )
    else:
        mocks["plot_fitting"].assert_not_called()


def test_plot_residuals(case_data):
    inp, mocks = case_data
    kwargs = inp["kwargs"]
    result = mocks["result"]
    if kwargs.get("plot_residuals", True):
        mocks["plot_residuals"].assert_called_once_with(
            func=func,
            data=data,
            a=result.a,
            plot_configuration=inp["plot_configuration"],
            output_path=inp["output_configuration"].residuals_output_path,
        )
    else:
        mocks["plot_residuals"].assert_not_called()
