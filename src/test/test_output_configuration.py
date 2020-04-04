from pathlib import Path
from unittest import TestCase

from eddington_matplotlib import OutputConfiguration


class OutputConfigurationBaseTestCase:
    func_name = "func_name"
    result_output_path = None
    data_output_path = None
    fitting_output_path = None
    residuals_output_path = None

    def setUp(self):
        self.output_configuration = OutputConfiguration.build(
            base_name=self.func_name, output_dir=self.output_dir
        )

    def test_result_output_path(self):
        self.assertEqual(
            self.result_output_path,
            self.output_configuration.result_output_path,
            msg="Data output path is different than expected",
        )

    def test_data_output_path(self):
        self.assertEqual(
            self.data_output_path,
            self.output_configuration.data_output_path,
            msg="Data output path is different than expected",
        )

    def test_fitting_output_path(self):
        self.assertEqual(
            self.fitting_output_path,
            self.output_configuration.fitting_output_path,
            msg="Fitting output path is different than expected",
        )

    def test_residuals_output_path(self):
        self.assertEqual(
            self.residuals_output_path,
            self.output_configuration.residuals_output_path,
            msg="Residuals output path is different than expected",
        )


class TestOutputConfigurationWithoutOutputDir(
    TestCase, OutputConfigurationBaseTestCase
):
    output_dir = None
    data_output_path = None
    fitting_output_path = None
    residuals_output_path = None

    def setUp(self):
        OutputConfigurationBaseTestCase.setUp(self)


class TestOutputConfigurationWithOutputDir(TestCase, OutputConfigurationBaseTestCase):
    output_dir = Path("directory")
    result_output_path = output_dir / "func_name_fitting_result.txt"
    data_output_path = output_dir / "func_name_data.png"
    fitting_output_path = output_dir / "func_name_fitting.png"
    residuals_output_path = output_dir / "func_name_fitting_residuals.png"

    def setUp(self):
        OutputConfigurationBaseTestCase.setUp(self)
