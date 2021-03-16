def solution(s):
    if len(s) % 2 == 1:
        s += "_"
    split_string = []
    for i in range(0, len(s) - 1, 2):
        split_string.append(s[i] + s[i + 1])
    print(split_string)
    return split_string