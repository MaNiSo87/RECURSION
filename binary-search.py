


def search(start, deth, end):
    if start == deth:
        return(start)
    x = input(f'Is your number between {start} and {deth} ({deth} is not counted), ans with yes and no.\n')
    if x == 'yes':
        return search(start, start + (deth-start) // 2 , deth)
    else:
        return search(deth, deth + ((end-deth) // 2), end)

print("choose a number between 1 and 100 (100 is not counted)\n\n")

print(f'Yout number is {search(1, 50, 99)}')
