def linear_search(array, val):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    :param array: List[int]
    :param val: int
    :return: bool
    """
    for i in array:
        if i == val:
            return True

    return False