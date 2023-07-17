"""Review of Ptyhon for ISLP"""
import numpy as np
from matplotlib.pyplot import subplots, show  # type: ignore
from matplotlib.markers import MarkerStyle  # type : ignore


def main() -> None:
    x1 = [3, 4, 5]
    y1 = [4, 9, 7]
    z1 = x1 + y1
    print(f"Value of z1 is: {z1}")
    x2 = np.array([3, 4, 5])
    y2 = np.array([4, 9, 7])
    z2 = x2 + y2
    print(f"Value of z2 is: {z2}")
    x3 = np.array([[1, 2, 3], [4, 5, 6]])
    print(
        f"Value of x3 is: {x3} with {x3.ndim} dimension(s) and type {x3.dtype} with shape {x3.shape}"
    )
    print(np.array([[1, 2], [3.0, 4]]).dtype)
    print(np.array([[1, 2], [3, 4]], float).dtype)
    print(f"Some of x3 is {x3.sum()}")
    x4 = np.array([[1, 2], [3.0, 4]])
    print(f"x4: {x4}\ntrasposted x4: {x4.T}")
    print(f"x4^2: {x4**2}")
    rng = np.random.default_rng(1303)
    x5 = rng.normal(loc=10, scale=1, size=50)
    print(x5, x5.mean())

    x = rng.standard_normal(100)
    y = rng.standard_normal(100)
    # fig, ax = subplots(figsize=(8, 8))
    fig, axes = subplots(nrows=2, ncols=3, figsize=(15, 5))
    fig, ax = subplots(figsize=(8, 8))
    ax.scatter(x, y, marker=MarkerStyle("o", fillstyle="full"))
    ax.set_xlabel("this is the x-axis")
    ax.set_ylabel("this is the y-axis")
    ax.set_title("Plot of X vs Y")
    axes[0, 1].plot(x, y, "o")
    axes[1, 2].scatter(x, y, marker="+")
    fig.set_size_inches(12, 3)
    show()

    return None


if __name__ == "__main__":
    main()
