def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    uniq_num = list(set(nums))
    counted = {}
    max = ['k', 0]

    for num in uniq_num:
        counted[num] = nums.count(num)

    for (k, v) in counted.items():
        if v > max[1]:
            max[0] = k
            max[1] = v
    return max[0]