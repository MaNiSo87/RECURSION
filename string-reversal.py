


def reversal(input, i):
    if len(input) == i + 1:
        pass
    else:
        reversal(input, i +1)
    print(input[i], end='')
        



reversal(input(), 0)