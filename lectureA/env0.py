"""Setup file for testing Python environment"""
# import cowsay
import numpy
import requests
import pytest


def main() -> None:
    """Main function"""
    # print(f"cowsay version: {cowsay.__version__}")
    print(f"numpy version: {numpy.__version__}")
    print(f"pytest version: {pytest.__version__}")
    print(f"requests version: {requests.__version__}")


if __name__ == "__main__":
    main()
