"""Setup file for testing Python environment"""
# import cowsay
import numpy  # type:ignore
import requests  # type:ignore
import pytest  # type:ignore


def main() -> None:
    """Main function"""
    # print(f"cowsay version: {cowsay.__version__}")
    print(f"numpy version: {numpy.__version__}")
    print(f"pytest version: {pytest.__version__}")
    print(f"requests version: {requests.__version__}")

    return None


def square(n: int) -> int:
    return n * n


if __name__ == "__main__":
    main()
