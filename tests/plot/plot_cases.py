from pathlib import Path

from tests.plot import base_kwargs


def case_no_kwargs():
    return base_kwargs, dict()


def case_xlabel():
    return dict(xlabel="xlabel", **base_kwargs), dict()


def case_ylabel():
    return dict(ylabel="ylabel", **base_kwargs), dict()


def case_both_x_and_y_label():
    return dict(xlabel="xlabel", ylabel="ylabel", **base_kwargs), dict()


def case_fitting_title():
    return dict(title="Fitting Title", **base_kwargs), dict()


def case_data_title():
    return dict(data_title="Data Title", **base_kwargs), dict()


def case_residuals_title():
    return dict(residuals_title="Residuals Title", **base_kwargs), dict()


def case_plot_data_to_file():
    return (
        dict(**base_kwargs, plot_data=True),
        dict(data_output_path=Path("/dir/to/output/data.png")),
    )


def case_plot_data_to_console():
    return (
        dict(**base_kwargs, plot_data=True),
        dict(),
    )


def case_plot_fitting_to_file():
    return (
        base_kwargs,
        dict(fitting_output_path=Path("/dir/to/output/fitting.png")),
    )


def case_no_plot_fitting():
    return (
        dict(**base_kwargs, plot_fitting=False),
        dict(),
    )


def case_plot_residuals_to_file():
    return (
        base_kwargs,
        dict(residuals_output_path=Path("/dir/to/output/residuals.png")),
    )


def case_no_plot_residuals():
    return (
        dict(**base_kwargs, plot_residuals=False),
        dict(),
    )


def case_print_results_to_file():
    return (
        base_kwargs,
        dict(result_output_path=Path("/dir/to/output/results.txt")),
    )


def case_without_print_results():
    return (
        dict(**base_kwargs, print_results=False),
        dict(),
    )


def case_grid():
    return dict(grid=True, **base_kwargs), dict()
