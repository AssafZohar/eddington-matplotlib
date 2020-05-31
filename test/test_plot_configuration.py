from unittest import TestCase

from eddington_matplotlib import PlotConfiguration


class PlotConfigurationBaseTestCase:
    decimal = 5

    xmin = 0.2
    xmax = 9.8
    base_name = "Base Name"
    grid = False
    xcolumn = xlabel = "x_column_example"
    ycolumn = ylabel = "y_column_example"
    title = "Base Name Fitting"
    residuals_title = "Base Name Fitting - Residuals"

    @classmethod
    def build_kwargs(
        cls,
        xlabel=None,
        ylabel=None,
        title=None,
        residuals_title=None,
        data_title=None,
        grid=False,
    ):
        kwargs = dict(
            xlabel=xlabel,
            ylabel=ylabel,
            title=title,
            residuals_title=residuals_title,
            data_title=data_title,
            grid=grid,
        )
        return kwargs

    def setUp(self):
        self.plot_configuration = PlotConfiguration.build(
            base_name=self.base_name,
            xmin=self.xmin,
            xmax=self.xmax,
            xcolumn=self.xcolumn,
            ycolumn=self.ycolumn,
            **self.kwargs
        )

    def test_xmin(self):
        self.assertAlmostEqual(
            self.xmin,
            self.plot_configuration.xmin,
            places=self.decimal,
            msg="X min value is different than expected",
        )

    def test_xmax(self):
        self.assertAlmostEqual(
            self.xmax,
            self.plot_configuration.xmax,
            places=self.decimal,
            msg="X max value is different than expected",
        )

    def test_xlabel(self):
        self.assertEqual(
            self.xlabel,
            self.plot_configuration.xlabel,
            msg="X label is different than expected",
        )

    def test_ylabel(self):
        self.assertEqual(
            self.ylabel,
            self.plot_configuration.ylabel,
            msg="Y label is different than expected",
        )

    def test_title(self):
        self.assertEqual(
            self.title,
            self.plot_configuration.title,
            msg="Title is different than expected",
        )

    def test_residuals_title(self):
        self.assertEqual(
            self.residuals_title,
            self.plot_configuration.residuals_title,
            msg="Residuals title is different than expected",
        )

    def test_grid(self):
        if self.grid:
            self.assertTrue(self.plot_configuration.grid, msg="Grid should be true")
        else:
            self.assertFalse(self.plot_configuration.grid, msg="Grid should be false")


class TestPlotConfigurationWithStringHeaders(TestCase, PlotConfigurationBaseTestCase):
    kwargs = PlotConfigurationBaseTestCase.build_kwargs()

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)


class TestPlotConfigurationWithXLabelOverride(TestCase, PlotConfigurationBaseTestCase):
    xlabel = "some x label"
    kwargs = PlotConfigurationBaseTestCase.build_kwargs(xlabel=xlabel)

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)


class TestPlotConfigurationWithYLabel(TestCase, PlotConfigurationBaseTestCase):
    ylabel = "some y label"
    kwargs = PlotConfigurationBaseTestCase.build_kwargs(ylabel=ylabel)

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)


class TestPlotConfigurationWithXAndYLabel(TestCase, PlotConfigurationBaseTestCase):
    xlabel = "xlabel"
    ylabel = "ylabel"
    kwargs = PlotConfigurationBaseTestCase.build_kwargs(xlabel=xlabel, ylabel=ylabel)

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)


class TestPlotConfigurationWithNumberHeaders(TestCase, PlotConfigurationBaseTestCase):
    xcolumn, ycolumn = 5.2, 2
    kwargs = PlotConfigurationBaseTestCase.build_kwargs()

    xlabel = ylabel = None

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)


class TestPlotConfigurationWithTitle(TestCase, PlotConfigurationBaseTestCase):
    title = "An Awesome Title"
    residuals_title = "An Awesome Title - Residuals"
    kwargs = PlotConfigurationBaseTestCase.build_kwargs(title=title)

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)


class TestPlotConfigurationWithResidualsTitle(TestCase, PlotConfigurationBaseTestCase):
    residuals_title = "An Awesome Residuals Title"
    kwargs = PlotConfigurationBaseTestCase.build_kwargs(residuals_title=residuals_title)

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)


class TestPlotConfigurationWithDataTitle(TestCase, PlotConfigurationBaseTestCase):
    data_title = "An Awesome Data Title"
    kwargs = PlotConfigurationBaseTestCase.build_kwargs(data_title=data_title)

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)


class TestPlotConfigurationWithGrid(TestCase, PlotConfigurationBaseTestCase):
    grid = True
    kwargs = PlotConfigurationBaseTestCase.build_kwargs(grid=True)

    def setUp(self):
        PlotConfigurationBaseTestCase.setUp(self)