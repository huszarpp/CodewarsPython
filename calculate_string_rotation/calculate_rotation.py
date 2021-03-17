def shifted_diff(first, second):

    if first == second:
        return 0

    rotate_counter = 0
    for i in range(len(first)):
        second = second[1:] + second[0]
        rotate_counter += 1
        if (first == second):
            return rotate_counter

    return -1