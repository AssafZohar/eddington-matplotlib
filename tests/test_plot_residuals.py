from pathlib import Path
from unittest import TestCase

from eddington_matplotlib import plot_residuals
from tests.base_test_cases import PlotBaseTestCase


class PlotResidualsBaseTestCase(PlotBaseTestCase):
    def setUp(self):
        PlotBaseTestCase.setUp(self)
        plot_residuals(
            func=self.func,
            data=self.data,
            plot_configuration=self.plot_configuration,
            a=self.a,
            output_path=self.output_path,
        )

    def test_error_bar(self):
        self.check_error_bar(y=self.data.y - self.func(self.a, self.data.x))

    def test_horizontal_line(self):
        self.plt.hlines.assert_called_with(
            0, xmin=self.xmin, xmax=self.xmax, linestyles="dashed", figure=self.figure
        )


class TestPlotResidualsWithoutLabelsAndTitle(TestCase, PlotResidualsBaseTestCase):
    def setUp(self):
        PlotResidualsBaseTestCase.setUp(self)


class TestPlotResidualsWithXlabel(TestCase, PlotResidualsBaseTestCase):

    xlabel = "xlabel"

    def setUp(self):
        PlotResidualsBaseTestCase.setUp(self)


class TestPlotResidualsWithYlabel(TestCase, PlotResidualsBaseTestCase):

    ylabel = "ylabel"

    def setUp(self):
        PlotResidualsBaseTestCase.setUp(self)


class TestPlotResidualsWithTitle(TestCase, PlotResidualsBaseTestCase):

    residuals_title = "Title - Residuals"

    def setUp(self):
        PlotResidualsBaseTestCase.setUp(self)


class TestPlotResidualsWithLabelsAndTitle(TestCase, PlotResidualsBaseTestCase):

    xlabel = "xlabel"
    ylabel = "ylabel"
    residuals_title = "Title - Residuals"

    def setUp(self):
        PlotResidualsBaseTestCase.setUp(self)


class TestPlotResidualsExportToFile(TestCase, PlotResidualsBaseTestCase):

    output_path = Path("/dir/to/output/linear_fitting_residuals.png")

    def setUp(self):
        PlotResidualsBaseTestCase.setUp(self)


class TestPlotFittingWithGrid(TestCase, PlotResidualsBaseTestCase):
    grid = True

    def setUp(self):
        PlotResidualsBaseTestCase.setUp(self)
