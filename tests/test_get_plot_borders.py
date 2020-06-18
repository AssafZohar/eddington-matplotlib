import pytest
from pytest_cases import cases_data, THIS_MODULE
import numpy as np
from eddington_matplotlib import PlotConfiguration

delta = 1e-5
size = 20


def case_positive_borders():
    inp = dict(min=1, max=6)
    out = dict(min=0.5, max=6.5)

    return inp, out


def case_min_border_zero():
    inp = dict(min=0, max=5)
    out = dict(min=-0.5, max=5.5)

    return inp, out


def case_min_border_negative_max_border_positive():
    inp = dict(min=-4, max=6)
    out = dict(min=-5, max=7)

    return inp, out


def case_max_border_zero():
    inp = dict(min=-5, max=0)
    out = dict(min=-5.5, max=0.5)

    return inp, out


def case_negative_borders():
    inp = dict(min=-6, max=-1)
    out = dict(min=-6.5, max=-0.5)

    return inp, out


@cases_data(module=THIS_MODULE)
def test_borders(case_data):
    inp, out = case_data.get()
    min_value, max_value = inp["min"], inp["max"]
    x = np.random.uniform(min_value, max_value, size=size)
    x = np.concatenate((x, np.array([min_value, max_value])), axis=None)
    np.random.shuffle(x)
    actual_min, actual_max = PlotConfiguration.get_plot_borders(x)
    assert out["min"] == pytest.approx(
        actual_min, rel=delta
    ), f"Expected minimum of {x} is different than expected."
    assert out["max"] == pytest.approx(
        actual_max, rel=delta
    ), f"Expected maximum of {x} is different than expected."
