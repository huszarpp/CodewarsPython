
def is_anagram(test, original):

    if len(test) != len(original):
        return False

    test_list = list(test.lower())
    original_list = list(original.lower())

    test_list.sort()
    original_list.sort()

    for i in range(len(test_list)):
        if test_list[i] != original_list[i]:
            return False

    return True