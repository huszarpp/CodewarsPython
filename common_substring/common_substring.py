def substring_test(s1, s2):

    for i in range(len(s1) - 1):
        if s1.lower()[i:i+2] in s2.lower():
            return True

    return False