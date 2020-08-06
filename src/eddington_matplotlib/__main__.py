"""Main module to plot fitting data."""
from argparse import ArgumentParser
from pathlib import Path
import json
import numpy as np

from eddington import FitData, FitFunctionsRegistry, FitResult
from eddington_matplotlib import PlotConfiguration, OutputConfiguration, plot_all

parser = ArgumentParser(description="Plot data and results from file")
parser.add_argument("input", type=Path, help="Input file to plot from")
parser.add_argument(
    "-o", "--output", type=Path, help="Output directory to save plots in"
)
parser.add_argument(
    "-g", "--grid", default=False, action="store_true", help="Add grid to plot"
)


def main():
    """
    Main method to plot data from json file.

    Examples for json datafiles can be seen in the "examples" directory.
    """
    args = parser.parse_args()
    input_path = args.input
    with open(input_path, mode="r") as json_file:
        json_obj = json.load(json_file)
    func = FitFunctionsRegistry.load(json_obj["fit_function"])
    fix = json_obj.get("fix", None)
    if fix is not None:
        for index, value in fix:
            func.fix(index, value)
    json_data = {key: np.array(value) for key, value in json_obj["data"].items()}
    data = FitData(data=json_data)
    result = FitResult(**json_obj["result"])
    xmin, xmax = PlotConfiguration.get_plot_borders(data.x)
    plot_configuration = PlotConfiguration.build(
        base_name=input_path.stem,
        xmin=xmin,
        xmax=xmax,
        xlabel="x",
        ylabel="y",
        grid=args.grid,
    )
    output_configuration = OutputConfiguration.build(
        base_name=func.name, output_dir=args.output
    )
    plot_all(
        func=func,
        data=data,
        result=result,
        plot_configuration=plot_configuration,
        output_configuration=output_configuration,
    )
    func.clear_fixed()


if __name__ == "__main__":
    main()
