import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # type:ignore
import mplcursors  # type:ignore


def main() -> None:
    print("Start of the program")
    # x1 = np.linspace(0, 10, 500, endpoint=True)
    # Data matrix
    data = {
        "TV": [230.1, 44.5, 17.2, 151.5, 180.8],
        "radio": [37.8, 39.3, 45.9, 41.3, 10.8],
        "newspaper": [69.2, 45.1, 69.3, 58.5, 58.4],
        "sales": [22.1, 10.4, 9.3, 18.5, 12.9],
    }
    table = [
        {"TV": 230.1, "radio": 37.8, "newspaper": 69.2, "sales": 22.1},
        {"TV": 44.5, "radio": 39.3, "newspaper": 45.1, "sales": 10.4},
        {"TV": 17.2, "radio": 45.9, "newspaper": 69.3, "sales": 9.3},
        {"TV": 151.5, "radio": 41.3, "newspaper": 58.5, "sales": 18.5},
        {"TV": 180.8, "radio": 10.8, "newspaper": 58.4, "sales": 12.9},
    ]
    df = pd.DataFrame(table)
    print(df)
    # Extract the TV and Sales values
    tv_values = [row["TV"] for row in table]
    sales_values = [row["sales"] for row in table]

    # Create a figure and set the window title
    fig = plt.figure(num="Plot of TV vs Sales")

    # Create a scatter plot
    scatter = plt.scatter(tv_values, sales_values)
    # Change the title of the plot
    plt.title("TV vs Sales")
    plt.xlabel("TV")
    plt.ylabel("Sales")

    # Add tooltips to each point
    for i in range(len(tv_values)):
        plt.annotate(
            f"(TV: {tv_values[i]}, Sales: {sales_values[i]})",
            (tv_values[i], sales_values[i]),
        )

    # Create the tooltips
    mplcursors.cursor(scatter, hover=True).connect(
        "add",
        lambda sel: sel.annotation.set_text(
            f"TV: {sel.target[0]}, Sales: {sel.target[1]}"
        ),
    )

    # Add grid to x and y axes
    plt.grid(which="both")

    # Show the plot
    plt.show(block=False)
    input("Press Enter to exit...")

    return None


if __name__ == "__main__":
    main()
