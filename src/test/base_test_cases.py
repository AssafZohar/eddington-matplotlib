from collections import namedtuple
import numpy as np
from mock import patch, call

from eddington_matplotlib import PlotConfiguration


FitData = namedtuple("FitData", ["x", "y", "xerr", "yerr"])


class PlotBaseTestCase:

    decimal = 5

    a = np.array([1.1, 1.92])
    x = np.arange(1, 10)
    xerr = np.random.normal()
    yerr = np.random.normal()
    y = 1 + 2 * (x + xerr) + yerr
    data = FitData(x=x, y=y, xerr=xerr, yerr=yerr)
    xlabel = None
    ylabel = None
    title = None
    data_title = None
    residuals_title = None
    expected_title = None

    grid = False
    output_path = None

    xmin = -1
    xmax = 1

    def setUp(self):
        plot_patcher = patch("eddington_matplotlib.util.plt")
        self.plt = plot_patcher.start()
        self.figure = self.plt.figure.return_value

        self.addCleanup(plot_patcher.stop)

        self.plot_configuration = PlotConfiguration(
            xlabel=self.xlabel,
            ylabel=self.ylabel,
            data_title=self.data_title,
            title=self.title,
            residuals_title=self.residuals_title,
            xmin=self.xmin,
            xmax=self.xmax,
            grid=self.grid,
        )

    @classmethod
    def func(cls, a, x):
        return a[0] + a[1] * x

    def check_error_bar(self, y):
        self.assertEqual(
            1,
            self.plt.errorbar.call_count,
            msg="errorbar call count is different than expected",
        )
        self.assertEqual(
            0,
            len(self.plt.errorbar.call_args_list[0].args),
            msg="errorbar arguments number is different than expected",
        )
        self.assertEqual(
            8,
            len(self.plt.errorbar.call_args_list[0].kwargs),
            msg="errorbar keyword arguments number is different than expected",
        )
        np.testing.assert_almost_equal(
            self.x,
            self.plt.errorbar.call_args_list[0].kwargs["x"],
            decimal=self.decimal,
            err_msg="X is different than expected",
        )
        np.testing.assert_almost_equal(
            y,
            self.plt.errorbar.call_args_list[0].kwargs["y"],
            decimal=self.decimal,
            err_msg="Y is different than expected",
        )
        np.testing.assert_almost_equal(
            self.xerr,
            self.plt.errorbar.call_args_list[0].kwargs["xerr"],
            decimal=self.decimal,
            err_msg="X error is different than expected",
        )
        np.testing.assert_almost_equal(
            self.yerr,
            self.plt.errorbar.call_args_list[0].kwargs["yerr"],
            decimal=self.decimal,
            err_msg="Y error is different than expected",
        )
        self.assertEqual(
            1,
            self.plt.errorbar.call_args_list[0].kwargs["markersize"],
            msg="markersize is different than expected",
        )
        self.assertEqual(
            "o",
            self.plt.errorbar.call_args_list[0].kwargs["marker"],
            msg="marker is different than expected",
        )
        self.assertEqual(
            "None",
            self.plt.errorbar.call_args_list[0].kwargs["linestyle"],
            msg="linestyle is different than expected",
        )

    def test_title(self):
        titles = [
            title
            for title in [self.data_title, self.title, self.residuals_title]
            if title is not None
        ]
        if len(titles) == 0:
            self.plt.title.assert_not_called()
            return
        for i, title in enumerate(titles):
            self.assertEqual(
                call(title, figure=self.figure),
                self.plt.title.call_args_list[i],
                msg=f"Title call number {i} is different than expected",
            )

    def test_xlabel(self):
        if self.xlabel is None:
            self.plt.xlabel.assert_not_called()
        else:
            self.plt.xlabel.assert_called_once_with(self.xlabel, figure=self.figure)

    def test_ylabel(self):
        if self.ylabel is None:
            self.plt.ylabel.assert_not_called()
        else:
            self.plt.ylabel.assert_called_once_with(self.ylabel, figure=self.figure)

    def test_show_or_export(self):
        if self.output_path is None:
            self.plt.show.assert_called_once_with()
            self.figure.savefig.assert_not_called()
        else:
            self.plt.show.assert_not_called()
            self.figure.savefig.assert_called_once_with(self.output_path)

    def test_grid(self):
        if self.grid:
            self.plt.grid.assert_called_with(True, figure=self.figure)
        else:
            self.plt.grid.assert_not_called()