def binary_search(array, low, high, value):

    if high >= low:
        middle = int((high + low) / 2)

        if array[middle] == value:
            return middle
        elif array[middle] > value:
            return binary_search(array, low, middle - 1, value)
        else:
            return binary_search(array, middle + 1, high, value)
    else:
        return -1


if __name__ == "__main__":
    A = list(range(100))
    print(binary_search(A, 0, len(A) - 1, value=50))
