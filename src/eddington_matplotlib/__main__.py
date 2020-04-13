from argparse import ArgumentParser
from pathlib import Path
import json
import numpy as np

from eddington_core import FitData, FitFunctionsRegistry, FitResult
from eddington_matplotlib import PlotConfiguration, OutputConfiguration, plot_all

parser = ArgumentParser(description="Plot data and results from file")
parser.add_argument("-i", "--input", type=Path, help="Input file to plot from")
parser.add_argument(
    "-g", "--grid", default=False, action="store_true", help="Add grid to plot"
)


def main():
    args = parser.parse_args()
    input_path = args.input
    with open(input_path, mode="r") as json_file:
        json_obj = json.load(json_file)
    func = FitFunctionsRegistry.load(
        json_obj["fit_function"], *json_obj.get("parameters", [])
    )
    json_data = {key: np.array(value) for key, value in json_obj["data"].items()}
    data = FitData(**json_data)
    result = FitResult(**json_obj["result"])
    xmin, xmax = PlotConfiguration.get_plot_borders(data.x)
    plot_configuration = PlotConfiguration.build(
        base_name=input_path.stem,
        xmin=xmin,
        xmax=xmax,
        xlabel="x",
        ylabel="y",
        export_result=False,
        grid=args.grid,
    )
    output_configuration = OutputConfiguration()
    plot_all(
        func=func,
        data=data,
        result=result,
        plot_configuration=plot_configuration,
        output_configuration=output_configuration,
    )


if __name__ == "__main__":
    main()
