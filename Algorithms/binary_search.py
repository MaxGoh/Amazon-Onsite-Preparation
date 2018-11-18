def binary_search(arr, l, r, val):
    """
    # Returns index of x in arr if present, else -1

    Time Complexity: O(Logn)
    Space Complexity: O(1)

    :param arr: List[int]
    :param val: int
    :return: int
    """
    if r >= l:

        mid = 1 + (r - l) // 2

        if arr[mid] == val:
            return mid

        elif arr[mid] > val:
            return binary_search(arr, l, mid-1, val)

        else:
            return binary_search(arr, mid+1, r, val)

    else:
        return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    res = binary_search(arr, 0, len(arr) - 1, x)
    print(res)
