from pathlib import Path

from tests.plot import base_kwargs


def case_no_kwargs():
    return base_kwargs, None


def case_xlabel():
    return dict(xlabel="xlabel", **base_kwargs), None


def case_ylabel():
    return dict(ylabel="ylabel", **base_kwargs), None


def case_both_x_and_y_label():
    return dict(xlabel="xlabel", ylabel="ylabel", **base_kwargs), None


def case_fitting_title():
    return dict(title="Fitting Title", **base_kwargs), None


def case_data_title():
    return dict(data_title="Data Title", **base_kwargs), None


def case_residuals_title():
    return dict(residuals_title="Residuals Title", **base_kwargs), None


def case_output_path():
    return base_kwargs, Path("/dir/to/output/linear_data.png")


def case_grid():
    return dict(grid=True, **base_kwargs), None
