def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = []
    non_true = [0, '', [], False, (), None]
    for el in lst:
        if non_true.count(el) == 0:
            new_lst.append(el)
    return new_lst
