import pytest
from pathlib import Path

from eddington_core import FitData
from mock import Mock
import numpy as np
from pytest_cases import fixture_plus

from eddington_matplotlib import plot_all
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
    show_or_export = mocker.patch("eddington_matplotlib.all.show_or_export")
    result = Mock()
    result.a = a
    return dict(
        plot_data=plot_data,
        plot_fitting=plot_fitting,
        plot_residuals=plot_residuals,
        show_or_export=show_or_export,
        result=result,
    )


@fixture_plus
def plot_all_fixture(configurations, plot_functions_mock):
    plot_configuration, output_configuration = configurations
    plot_all(
        func=func,
        data=data,
        plot_configuration=plot_configuration,
        output_configuration=output_configuration,
        result=plot_functions_mock["result"],
    )
    return configurations, plot_functions_mock


def test_export_result(plot_all_fixture):
    (plot_configuration, output_configuration), mocks = plot_all_fixture

    result = mocks["result"]
    if plot_configuration.print_results:
        result.print_or_export.assert_called_once_with(
            output_configuration.result_output_path,
        )
    else:
        result.print_or_export.assert_not_called()


def test_plot_data(plot_all_fixture):
    (plot_configuration, output_configuration), mocks = plot_all_fixture

    plot_data = mocks["plot_data"]
    show_or_export = mocks["show_or_export"]
    if plot_configuration.plot_data:
        plot_data.assert_called_once_with(
            data=data, plot_configuration=plot_configuration,
        )
        show_or_export.assert_any_call(
            fig=plot_data.return_value,
            output_path=output_configuration.data_output_path,
        )
    else:
        plot_data.assert_not_called()


def test_plot_fitting(plot_all_fixture):
    (plot_configuration, output_configuration), mocks = plot_all_fixture

    plot_fitting = mocks["plot_fitting"]
    show_or_export = mocks["show_or_export"]
    if plot_configuration.plot_fitting:
        plot_fitting.assert_called_once_with(
            func=dummy_func, a=a, data=data, plot_configuration=plot_configuration,
        )
        show_or_export.assert_any_call(
            fig=plot_fitting.return_value,
            output_path=output_configuration.fitting_output_path,
        )
    else:
        plot_fitting.assert_not_called()


def test_plot_residuals(plot_all_fixture):
    (plot_configuration, output_configuration), mocks = plot_all_fixture

    plot_residuals = mocks["plot_residuals"]
    show_or_export = mocks["show_or_export"]
    if plot_configuration.plot_residuals:
        plot_residuals.assert_called_once_with(
            func=dummy_func, a=a, data=data, plot_configuration=plot_configuration,
        )
        show_or_export.assert_any_call(
            fig=plot_residuals.return_value,
            output_path=output_configuration.residuals_output_path,
        )
    else:
        plot_residuals.assert_not_called()


def test_show_or_export_cal_count(plot_all_fixture):
    (plot_configuration, output_configuration), mocks = plot_all_fixture
    show_or_export = mocks["show_or_export"]
    expected_count = len(
        [
            boolean
            for boolean in [
                plot_configuration.plot_data,
                plot_configuration.plot_fitting,
                plot_configuration.plot_residuals,
            ]
            if boolean
        ]
    )
    assert (
        expected_count == show_or_export.call_count
    ), "show_or_export call count is different than expected"
