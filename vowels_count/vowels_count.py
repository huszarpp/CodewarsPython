def get_count(input_str):

    num_vowels = 0
    VOWELS = 'aeiou'
    for char in input_str:
        # if char in VOWELS:
        #     num_vowels += 1
        num_vowels += 1 if VOWELS.find(char) > 0 else 0
    return num_vowels