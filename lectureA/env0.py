"""Setup file for testing Python environment"""
# import cowsay  # type:ignore
import numpy
import requests
import pytest
import pandas


def main() -> None:
    """Main function"""
    # print(f"cowsay version: {cowsay.__version__}")
    print(f"numpy version: {numpy.__version__}")
    print(f"pytest version: {pytest.__version__}")
    print(f"requests version: {requests.__version__}")
    print(f"pandas version: {pandas.__version__}")

    return None


def square(n: int) -> int:
    return n * n


if __name__ == "__main__":
    main()
