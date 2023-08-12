import numpy as np


def index_examples() -> None:
    """
    Purpose: example with indexes
    """
    A = np.array(np.arange(16)).reshape((4, 4))
    print(f"A:\n{A}")
    B = np.arange(16).reshape(4, 4)
    # print(f"B = {B}")
    if np.array_equal(A, B):
        print("A and B are equal")
    """ # multiple-lines comment
        [
            [ 0  1  2  3]
            [ 4  5  6  7]
            [ 8  9 10 11]
            [12 13 14 15]
        ]
    """
    # Create an array of indices
    indices = np.array([[1, 0], [3, 2], [1, 3]])
    print(f"array of indices\n{indices}")
    print(f"select 1:\n{A[[1, 3], :]}")
    print(f"select 2:\n{A[:, [0, 2]]}")
    print(f"select 3:\n{A[[1,3], [0, 2]]}")
    print(f"select 4:\n{A[[1,3,1],[0,2,3]]}")
    print(f"select 5:\n{A[indices[:,0],indices[:,1]]}")
    print(f"select 6:\n{A[indices]}")
    print(f"select 7:\n{A[np.ix_([1,3], [0,2])]}")
    keep_rows = np.repeat(False, A.shape[0])
    keep_rows[[1, 3]] = True
    print(f"same_values_array:\n{keep_rows}")
    print(
        f"keep_rows is{'' if np.array_equal(keep_rows, np.array([0,1,0,1])) == True else ' not'} equal"
    )
    return None


def square(n: int) -> int:
    """Calculate square of an integer number

    Args:
        n (int): input value

    Returns:
        int: returned value
    """
    return n * n


def main() -> None:
    """main function
    Returns:
        None: no returned value
    """
    print("Start of the program")
    x: list[int] = [3, 4, 5]
    y: list[int] = [4, 9, 7]
    # print(f"{x}, {y}, {x+y}")
    x1 = np.array([3, 4, 5])
    y1 = np.array([4, 9, 7])
    # print(f"{x1}, {y1}, {x1+y1}")
    x2 = np.array([[1, 2], [3, 4]])
    # print(f"{x2}")
    a = b = 2
    """
        if a == b:
        print("a and b are equal")
    """
    index_examples()
    # input("Press Enter to exit...")
    # da [79] e rivedere indici e plot
    return None


if __name__ == "__main__":
    main()
