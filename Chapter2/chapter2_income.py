import os
from matplotlib.markers import MarkerStyle  # type:ignore
import matplotlib.pyplot as plt  # type:ignore
import numpy as np  # type:ignore
from pandas import read_csv


def main() -> None:
    """
        Main function()
    Returns:
        None: this function returns no value
    """
    print("Start of program")
    # my code here
    file_name = "Income1.csv"
    plots_title = os.path.splitext(os.path.basename(file_name))[0]
    income = read_csv(file_name)
    x = income["Education"]
    y = income["Income"]
    a, b = np.polyfit(x, y, 1)
    fig, axis = plt.subplots(figsize=(6, 7))
    print("End of program")
    axis.scatter(x, y, color="red", marker=MarkerStyle("o"))
    axis.plot(x, a * x + b, color="blue")
    axis.set_xlabel("Years of education")
    axis.set_ylabel("Income")
    fig.suptitle("Incomes")

    """
        # plot without subplots
        # Create a line plot
        plt.scatter(x, y, color="red", marker=MarkerStyle("o"))

        # Add labels and title
        plt.xlabel("Years of education")
        plt.ylabel("Income")
        plt.title("Incomes")

        # Add legend
        plt.legend()
    """
    # Show the plot
    plt.show()
    return None


if __name__ == "__main__":
    main()
