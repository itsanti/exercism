def score(word):
    letter_values = {
        'AEIOULNRST':1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
         'QZ': 10
    }

    return sum([letter_values[key] for char in word for key in letter_values.keys() if char.upper() in key])
