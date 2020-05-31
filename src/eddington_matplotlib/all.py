"""Plot all desired plot."""
from eddington_core import FitData, FitResult

from eddington_matplotlib.fitting import plot_fitting
from eddington_matplotlib.residuals import plot_residuals
from eddington_matplotlib.output_configuration import OutputConfiguration
from eddington_matplotlib.plot_configuration import PlotConfiguration
from eddington_matplotlib.data import plot_data


def plot_all(
    func,
    data: FitData,
    result: FitResult,
    plot_configuration: PlotConfiguration,
    output_configuration: OutputConfiguration,
):
    """
    Plot all desired plot.

    :param func: Fitting function.
    :param data: Fitting data.
    :param result: Fitting result.
    :param plot_configuration: Plot configuration.
    :param output_configuration: :class:`OutputConfiguration` instance indicates
     where and whether to save plot to file.
    """
    if plot_configuration.export_result:
        result.export_to_file(output_configuration.result_output_path)
    if plot_configuration.plot_data:
        plot_data(
            data=data,
            plot_configuration=plot_configuration,
            output_path=output_configuration.data_output_path,
        )
    if plot_configuration.plot_fitting:
        plot_fitting(
            func=func,
            data=data,
            plot_configuration=plot_configuration,
            a=result.a,
            output_path=output_configuration.fitting_output_path,
        )
    if plot_configuration.plot_residuals:
        plot_residuals(
            func=func,
            data=data,
            plot_configuration=plot_configuration,
            a=result.a,
            output_path=output_configuration.residuals_output_path,
        )
