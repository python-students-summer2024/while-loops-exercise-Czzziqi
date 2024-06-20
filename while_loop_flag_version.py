def get_starting_number():
    number = input ("How many bottles of beer on the wall? ")
    while not number. isdigit() or int(number) < 1:
        print("Please enter a valid integer 1 or greater.")
        number = input ("How many bottles of beer on the wall?")
    return int(number)


def sing(starting_number):
    continue_sing=True
    while continue_sing:
        if starting_number>1:
            print(f"{starting_number} bottles of beer on the wall, {starting_number} bottles of beer.")
            if starting_number-1==1:
                print(f"Take one down, pass it around, {starting_number-1} bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {starting_number-1} bottles of beer on the wall.\n")
        else:
            print(f"{starting_number} bottle of beer on the wall, {starting_number} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            continue_sing=False
        starting_number=starting_number-1

