import numpy
import cowsay
import requests
import pytest

def main():
    print(f"cowsay version: {cowsay.__version__}")
    print(f"numpy version: {numpy.__version__}")
    print(f"pytest version: {pytest.__version__}")
    print(f"requests version: {requests.__version__}")

if __name__ == '__main__':
    main()
