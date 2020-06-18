from pathlib import Path
from unittest import TestCase
import numpy as np

from eddington_matplotlib import plot_data
from tests.plot import PlotBaseTestCase


class PlotDataBaseTestCase(PlotBaseTestCase):
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


class TestPlotDataWithoutLabelsAndTitle(TestCase, PlotDataBaseTestCase):
    def setUp(self):
        PlotDataBaseTestCase.setUp(self)


class TestPlotDataWithXlabel(TestCase, PlotDataBaseTestCase):

    xlabel = "xlabel"

    def setUp(self):
        PlotDataBaseTestCase.setUp(self)


class TestPlotDataWithYlabel(TestCase, PlotDataBaseTestCase):

    ylabel = "ylabel"

    def setUp(self):
        PlotDataBaseTestCase.setUp(self)


class TestPlotDataWithBothLabels(TestCase, PlotDataBaseTestCase):

    xlabel = "xlabel"
    ylabel = "ylabel"

    def setUp(self):
        PlotDataBaseTestCase.setUp(self)


class TestPlotDataExportToFile(TestCase, PlotDataBaseTestCase):

    should_export = True
    output_path = Path("/dir/to/output/linear_data.png")

    def setUp(self):
        PlotDataBaseTestCase.setUp(self)


class TestPlotDataWithGrid(TestCase, PlotDataBaseTestCase):
    grid = True

    def setUp(self):
        PlotDataBaseTestCase.setUp(self)


class TestPlotDataWithTitle(TestCase, PlotDataBaseTestCase):
    data_title = "Data Title"

    def setUp(self):
        PlotDataBaseTestCase.setUp(self)
