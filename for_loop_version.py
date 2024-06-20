def get_starting_number():
    number = input ("How many bottles of beer on the wall? ")
    while not number. isdigit() or int(number) < 1:
        print("Please enter a valid integer 1 or greater.")
        number = input ("How many bottles of beer on the wall?")
    return int(number)

        
def sing(starting_number):
    for i in range(starting_number, 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall. \n")
        elif i ==2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottle of beer on the wall. \n")
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")