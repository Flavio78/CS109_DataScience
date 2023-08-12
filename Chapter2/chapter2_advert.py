from matplotlib.pyplot import subplots, show  # type:ignore
import pandas as pa
from matplotlib.markers import MarkerStyle  # type:ignore


def main() -> None:
    """Main function

    Returns:
        None: return no value
    """
    print("Start of program")
    adv = pa.read_csv("Advertising.csv")
    # print(f"Advertising DataFrame:\n{adv}")
    fig, axes = subplots(nrows=1, ncols=3, figsize=(8, 4))
    # define x and y from dataframe
    y = adv["sales"]
    axes[0].scatter(adv["TV"], y, marker=MarkerStyle("o"))
    axes[0].set_xlabel("TV")
    axes[0].set_ylabel("Sales")
    axes[1].scatter(adv["radio"], y, marker=MarkerStyle("o"))
    axes[1].set_xlabel("Radio")
    axes[1].set_ylabel("Sales")
    axes[2].scatter(adv["newspaper"], y, marker=MarkerStyle("o"))
    axes[2].set_xlabel("Newspaper")
    axes[2].set_ylabel("Sales")
    fig.suptitle("Sales")
    show()
    print("End of program")
    return None


if __name__ == "__main__":
    main()
