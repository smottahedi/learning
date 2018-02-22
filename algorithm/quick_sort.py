"Quick-Sort."


def quick_sort(array):
    """
    Parameters
    ----------------

    array : vartype
        array is

    Returns
    ----------------

    """

    if len(array) < 2:
        return

    p = array[-1]
    L = []
    E = []
    G = []

    while array:
        if array[-1] < p:
            L.insert(0, array.pop())
        elif p < array[-1]:
            G.insert(0, array.pop())
        else:
            E.insert(0, array.pop())

    quick_sort(L)
    quick_sort(G)

    while G:
        array.insert(0, G.pop())

    while E:
        array.insert(0, E.pop())

    while L:
        array.insert(0, L.pop())


if __name__ == "__main__":
    import random
    A = list(range(20))
    random.shuffle(A)

    quick_sort(A)
    print(A)
