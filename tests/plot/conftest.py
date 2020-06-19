import pytest
from pytest_cases import fixture_plus, cases_data
import tests.plot.plot_cases as cases
from eddington_matplotlib import PlotConfiguration, OutputConfiguration


@pytest.fixture
def plt_mock(mocker):
    plt = mocker.patch("eddington_matplotlib.util.plt")
    figure = plt.figure.return_value
    return dict(plt=plt, figure=figure)


@fixture_plus
@cases_data(module=cases)
def configurations(case_data):
    plot_configuration_kwargs, output_configuration_kwargs = case_data.get()
    return (
        PlotConfiguration(**plot_configuration_kwargs),
        OutputConfiguration(**output_configuration_kwargs),
    )
