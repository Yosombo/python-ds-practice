def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    day_name = {(2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'),
                (5, 'Thursday'), (6, "Friday"), (7, "Saturday"), (1, 'Sunday')}

    res = None
    for (k, v) in day_name:
        if k == day_of_week:
            res = v
    return res
