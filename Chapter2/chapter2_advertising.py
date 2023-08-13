import os
from matplotlib.pyplot import subplots, show  # type:ignore
import numpy as np  # type:ignore
from pandas import Series, read_csv


def main() -> None:
    """Main function

    Returns:
        None: return no value
    """
    print("Start of program")
    file_name = "./Advertising.csv"
    plots_title = os.path.splitext(os.path.basename(file_name))[0]
    adv = read_csv(file_name)
    fig, axes = subplots(nrows=1, ncols=3, figsize=(8, 4))
    # define x and y from dataframe
    y = adv["sales"]
    x: Series[float]
    a: np.ndarray
    b: np.ndarray

    for index in range(axes.size):
        x = adv.iloc[:, index + 1]
        a, b = np.polyfit(x, y, 1)
        axes[index].plot(x, a * x + b, color="blue")
        axes[index].scatter(
            x,
            y,
            color="red",
            marker="o",
            facecolor="none",
            edgecolors="red",
        )
        axes[index].set_xlabel(str(x.name).title())
        axes[index].set_ylabel("Sales")
    fig.suptitle(plots_title)
    show()
    print("End of program")
    return None


if __name__ == "__main__":
    main()
