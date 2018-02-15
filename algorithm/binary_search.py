
def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while (low <= high):
        middle = int((high + low) / 2)
        if input_array[middle] == value:
            return middle
        elif value < input_array[middle]:
            high = middle - 1
        elif value > input_array[middle]:
            low = middle + 1
    return -1


if __name__ == "__main__":
    test_list = [1, 3, 9, 11, 15, 19, 29]
    test_val1 = 25
    test_val2 = 15
    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))
    print(binary_search(test_list, 3))
