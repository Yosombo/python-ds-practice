def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'
    """
    swap_item_lower = to_swap.lower()
    swap_item_upper = to_swap.upper()
    swapped = []
    for char in phrase:
        if char == swap_item_lower:
            swapped.append(char.upper())
        elif char == swap_item_upper:
            swapped.append(char.lower())
        else:
            swapped.append(char)
    return ''.join(swapped)
