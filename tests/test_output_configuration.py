from pytest_cases import cases_data, THIS_MODULE
from pathlib import Path

from eddington_matplotlib import OutputConfiguration


func_name = "func_name"


def case_no_output_dir():
    output_configuration = OutputConfiguration.build(base_name=func_name)
    expected = dict(
        result_output_path=None,
        data_output_path=None,
        fitting_output_path=None,
        residuals_output_path=None,
    )
    return output_configuration, expected


def case_with_output_fir():
    output_dir = Path("directory")
    output_configuration = OutputConfiguration.build(
        base_name=func_name, output_dir=output_dir
    )
    expected = dict(
        result_output_path=output_dir / "func_name_fitting_result.txt",
        data_output_path=output_dir / "func_name_data.png",
        fitting_output_path=output_dir / "func_name_fitting.png",
        residuals_output_path=output_dir / "func_name_fitting_residuals.png",
    )
    return output_configuration, expected


@cases_data(module=THIS_MODULE)
def test_result_output_path(case_data):
    output_configuration, expected = case_data.get()
    assert (
        expected["result_output_path"] == output_configuration.result_output_path
    ), "Data output path is different than expected"


@cases_data(module=THIS_MODULE)
def test_data_output_path(case_data):
    output_configuration, expected = case_data.get()
    assert (
        expected["data_output_path"] == output_configuration.data_output_path
    ), "Data output path is different than expected"


@cases_data(module=THIS_MODULE)
def test_fitting_output_path(case_data):
    output_configuration, expected = case_data.get()
    assert (
        expected["fitting_output_path"] == output_configuration.fitting_output_path
    ), "Fitting output path is different than expected"


@cases_data(module=THIS_MODULE)
def test_residuals_output_path(case_data):
    output_configuration, expected = case_data.get()
    assert (
        expected["residuals_output_path"] == output_configuration.residuals_output_path
    ), "Residuals output path is different than expected"
