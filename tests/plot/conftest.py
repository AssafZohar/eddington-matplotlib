from pytest_cases import fixture_plus, cases_data
import tests.plot.plot_cases as cases
from eddington_matplotlib import PlotConfiguration, OutputConfiguration


@fixture_plus
@cases_data(module=cases)
def configurations(case_data):
    plot_configuration_kwargs, output_configuration_kwargs = case_data.get()
    return (
        PlotConfiguration(**plot_configuration_kwargs),
        OutputConfiguration(**output_configuration_kwargs),
    )
