from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass
class OutputConfiguration:

    data_output_path: Union[Path, None] = None
    fitting_output_path: Union[Path, None] = None
    residuals_output_path: Union[Path, None] = None

    @classmethod
    def build(cls, func_name: str, output_dir: Path = None):

        (
            data_output_path,
            fitting_output_path,
            residuals_output_path,
        ) = cls.__get_output_paths(func_name=func_name, output_dir=output_dir)
        return OutputConfiguration(
            data_output_path=data_output_path,
            fitting_output_path=fitting_output_path,
            residuals_output_path=residuals_output_path,
        )

    @classmethod
    def __get_output_paths(cls, func_name: str, output_dir: Path):
        if output_dir is None:
            return None, None, None

        underscore_func_name = func_name.lower().replace(" ", "_")
        data_output_path = output_dir / f"{underscore_func_name}_data.png"
        fitting_output_path = output_dir / f"{underscore_func_name}_fitting.png"
        residuals_output_path = (
            output_dir / f"{underscore_func_name}_fitting_residuals.png"
        )
        return data_output_path, fitting_output_path, residuals_output_path
