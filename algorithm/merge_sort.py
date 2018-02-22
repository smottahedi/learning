"Merge Sort."


def merge_sort(array):
    """
    Parameters
    ----------------

    array : list
        array is list numbers to be sorted.

    Returns
    ----------------
    array : list
        array is the sorted array.
    """

    if len(array) < 2:
        return

    left = array[:len(array) // 2]
    right = array[len(array) // 2:]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, array)


def merge(left, right, array):
    """
    Parameters
    ----------------

    left : list
        left is list of numbers.
    right : list
        right is list of numbers.

    Returns
    ----------------
    array : list
        array is list of two merged list.
    """
    i = j = 0

    while i + j < len(array):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1


if __name__ == "__main__":
    import random
    A = list(range(30))
    random.shuffle(A)
    merge_sort(A)
    print(A)
