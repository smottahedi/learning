"Bubble sort."


def bubble_sort(array):
    """
    Parameters
    ----------------

    array : list
        array is python list to be sorted.

    Returns
    ----------------
    array : list
        sorted array.
    """
    for _ in range(len(array) - 1, 0, -1):
        for j in range(_):
            print("iter ", array)
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array


if __name__ == "__main__":
    import random
    A = list(range(20))
    random.shuffle(A)
    print("before : ", A)
    A = bubble_sort(A)
    print("after : ", A)
