import pytest


@pytest.fixture
def plt_mock(mocker):
    plt = mocker.patch("eddington_matplotlib.util.plt")
    figure = plt.figure.return_value
    return dict(plt=plt, figure=figure)
