import os
import matplotlib.pyplot as plt  # type:ignore
import numpy as np  # type:ignore
from pandas import Series, read_csv, Index


def find_nearest(array, value):
    """
    Here's a function that finds the index of the nearest neighbor
    and returns the value of the nearest neighbor.  Note that this
    is just for k = 1 and the distance function is simply the
    absolute value.

    Args:
        array (_type_): _description_
        value (_type_): _description_

    Returns:
        None: no returned value
    """
    idx = (np.abs(array - value)).idxmin()
    return idx, array[idx]


def tv_budget() -> None:
    """
    Advertising for tv bugdet vs sales.
    Code from: https://harvard-iacs.github.io/2018-CS109A/lectures/lecture-4/demo/

    Parameters
    ----------
    None

    Returns
    -------
    None: no returned value
    """
    # Read data
    df_adv = read_csv("Advertising.csv")
    # Sort the data
    idx = np.argsort(df_adv.TV)  # Get indices ordered from lowest to highest values
    # Get the actual data in the order from above
    data_x: Series[float] = df_adv.TV.iloc[idx]
    data_y: Series[float] = df_adv.sales.iloc[idx]
    # Get a subset of the data
    idx2 = Index([7, 12, 34, 39, 74, 101, 109, 172])
    df_adv_TV = data_x.iloc[idx2]  # df_adv.TV[5:13]
    df_adv_sales = data_y.iloc[idx2]  # df_adv.sales[5:13]
    data_x = df_adv_TV
    data_y = df_adv_sales
    # Note that we have used the idxmin method in our function.  This is
    # because `array' is a pandas dataframe and idxmin() is designed to
    # work with pandas dataframes.  If we are working with a numpy array
    # then the appropriate method would be `argmin()'.

    # Create some artificial x-values (might not be in the actual dataset)
    x = np.linspace(
        np.min(np.array(data_x, dtype=float)), np.max(np.array(data_x, dtype=float))
    )

    # Initialize the y-values to zero
    y = np.zeros((len(x)))

    # Apply the KNN algorithm.  Try to predict the y-value at a given x-value
    # Note:  You may have tried to use the `range' method in your code.  Enumerate
    # is far better in this case.  Try to understand why.
    for i, xi in enumerate(x):
        y[i] = data_y[find_nearest(data_x, xi)[0]]

    plt.figure(num="Plot TV budgets Vs Sales")
    # Plot the original data using black x's.
    # Plot your solution
    plt.plot(x, y, "-.")
    # Plot the original data using black x's.
    plt.plot(df_adv_TV, df_adv_sales, "kx")
    plt.title("")
    plt.xlabel("TV budget in $1000")
    plt.xlim(0, 249)
    plt.ylabel("Sales in $1000")
    plt.ylim(0, 23)
    plt.show()
    return None


def advertising_polifill() -> None:
    """
    Advertising with polifill

    Parameters
    ----------
    None

    Returns
    -------
    None: no returned value
    """
    file_name = "./Advertising.csv"
    plots_title = os.path.splitext(os.path.basename(file_name))[0]
    adv = read_csv(file_name)
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))
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
    plt.show()
    return None


def main() -> None:
    """
    Main function

    Parameters
    ----------
    None

    Returns
    -------
    None: no returned value
    """
    print("Start of program")
    tv_budget()
    print("End of program")
    return None


if __name__ == "__main__":
    main()
