from pathlib import Path
from unittest import TestCase
import numpy as np

from eddington_matplotlib import plot_data
from test.base_test_cases import PlotBaseTestCase


class PlotFittingBaseTestCase(PlotBaseTestCase):
    xrange = np.arange(PlotBaseTestCase.xmin, PlotBaseTestCase.xmax, step=0.002)
    yrange = PlotBaseTestCase.a[0] + PlotBaseTestCase.a[1] * xrange

    def setUp(self):
        PlotBaseTestCase.setUp(self)
        plot_data(
            data=self.data,
            plot_configuration=self.plot_configuration,
            output_path=self.output_path,
        )

    def test_error_bar(self):
        self.check_error_bar(y=self.data.y)


class TestPlotFittingWithoutLabelsAndTitle(TestCase, PlotFittingBaseTestCase):
    def setUp(self):
        PlotFittingBaseTestCase.setUp(self)


class TestPlotFittingWithXlabel(TestCase, PlotFittingBaseTestCase):

    xlabel = "xlabel"

    def setUp(self):
        PlotFittingBaseTestCase.setUp(self)


class TestPlotFittingWithYlabel(TestCase, PlotFittingBaseTestCase):

    ylabel = "ylabel"

    def setUp(self):
        PlotFittingBaseTestCase.setUp(self)


class TestPlotFittingWithBothLabels(TestCase, PlotFittingBaseTestCase):

    xlabel = "xlabel"
    ylabel = "ylabel"

    def setUp(self):
        PlotFittingBaseTestCase.setUp(self)


class TestPlotFittingExportToFile(TestCase, PlotFittingBaseTestCase):

    should_export = True
    output_path = Path("/dir/to/output/linear_data.png")

    def setUp(self):
        PlotFittingBaseTestCase.setUp(self)


class TestPlotFittingWithGrid(TestCase, PlotFittingBaseTestCase):
    grid = True

    def setUp(self):
        PlotFittingBaseTestCase.setUp(self)
