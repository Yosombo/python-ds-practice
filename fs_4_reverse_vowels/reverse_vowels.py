def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    check_vowels = 'uoieaUOIEA'
    index = []
    vowels = []
    word = list(s)

    for i, val in enumerate(word):
        if val in check_vowels:
            index.append(i)
            vowels.append(val)

    vowels.reverse()

    vowel_id = 0
    for i in index:
        word[i] = vowels[vowel_id]
        vowel_id += 1
    return ''.join(word)
