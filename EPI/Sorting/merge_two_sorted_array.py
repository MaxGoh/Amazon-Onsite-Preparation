def merge_two_sorted_array(l1, l2):
    """
    Time Complexity: O(n+m)
    Space Complexity: O(n+m)

    :param l1: List[int]
    :param l2: List[int]
    :return: List[int]
    """
    if not l1:
        return l2
    if not l2:
        return l1

    merge_list = []

    i1 = 0
    i2 = 0
    l1_len = len(l1) - 1
    l2_len = len(l2) - 1

    while i1 <= l1_len and i2 <= l2_len:
        if l1[i1] < l2[i2]:
            merge_list.append(l1[i1])
            i1 += 1

        else:
            merge_list.append(l2[i2])
            i2 += 1

    while i1 <= l1_len:
        merge_list.append(l1[i1])
        i1 += 1

    while i2 <= l2_len:
        merge_list.append(l2[i2])
        i2 += 1

    return merge_list


if __name__ == "__main__":
    l1 = [3, 5, 8, 10, 25, 52]
    l2 = [1, 51, 100, 141, 1231312]

    merge_list = merge_two_sorted_array(l1, l2)
    print(merge_list)