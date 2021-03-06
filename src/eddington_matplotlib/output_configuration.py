"""Configuration for the results output."""
from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass
class OutputConfiguration:
    """Data class for the results output."""

    result_output_path: Union[Path, None] = None
    data_output_path: Union[Path, None] = None
    fitting_output_path: Union[Path, None] = None
    residuals_output_path: Union[Path, None] = None

    @classmethod
    def build(cls, base_name: str, output_dir: Path = None):
        """
        Build :class:`OutputConfiguration` instance.

        :param base_name: str. Base name that paths will be generated from.
        :param output_dir: Output directory for the plots.
        """
        if output_dir is None:
            return OutputConfiguration()
        normalized_base_name = base_name.lower().replace(" ", "_")
        return OutputConfiguration(
            result_output_path=(
                output_dir / f"{normalized_base_name}_fitting_result.txt"
            ),
            data_output_path=output_dir / f"{normalized_base_name}_data.png",
            fitting_output_path=output_dir / f"{normalized_base_name}_fitting.png",
            residuals_output_path=(
                output_dir / f"{normalized_base_name}_fitting_residuals.png"
            ),
        )
