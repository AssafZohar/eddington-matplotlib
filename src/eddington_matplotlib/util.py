import matplotlib.pyplot as plt


def get_figure():
    return plt.figure()


def plot(x, y, fig):
    plt.plot(x, y, figure=fig)


def horizontal_line(xmin, xmax, y=0):
    plt.hlines(y, xmin=xmin, xmax=xmax, linestyles="dashed")


def errorbar(x, y, xerr, yerr, fig):
    plt.errorbar(
        x=x,
        y=y,
        xerr=xerr,
        yerr=yerr,
        markersize=1,
        marker="o",
        linestyle="None",
        figure=fig,
    )


def title(title_name, fig):
    if title_name is not None:
        plt.title(title_name, figure=fig)


def label_axes(xlabel, ylabel, fig):
    if xlabel is not None:
        plt.xlabel(xlabel, figure=fig)
    if ylabel is not None:
        plt.ylabel(ylabel, figure=fig)


def grid(is_grid, fig):
    if is_grid:
        plt.grid(True, figure=fig)


def show_or_export(fig: plt.Figure, output_path=None):
    if output_path is None:
        plt.show()
        return
    fig.savefig(output_path)
