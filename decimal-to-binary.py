

def transfer(decimal, result):
    if decimal == 0:
        return result
    
    result = str(decimal % 2) + result
    return transfer(decimal // 2, result)

print(transfer(int(input()), ""))