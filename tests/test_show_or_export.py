from pathlib import Path

from eddington_matplotlib.util import show_or_export


def test_show_figure(plt_mock):
    plt, figure = plt_mock["plt"], plt_mock["figure"]
    show_or_export(figure)
    plt.show.assert_called_once_with()


def test_save_figure(plt_mock):
    plt, figure = plt_mock["plt"], plt_mock["figure"]
    output_path = Path("/path/to/output/fig.png")
    show_or_export(figure, output_path=output_path)
    plt.show.asssert_not_called()
    figure.savefig.assert_called_once_with(output_path)
