# This program works correctly for only positive numbers and has a bit-width of 6 bits
# So I have to continue working on it.


def twos_complement(decimal_num):
    # This function takes a decimal number 
    binary = bin(int(decimal_num))[2:]
    # Converts the number to binary
    print(f"The binary is {binary}")
    # Prints the result
    flipped = []
    for number in binary:
        if number == "0":
            number = "1"
            flipped.append(number)
        else:
            number = "0"
            flipped.append(number)
    # Flips the 0s and 1s to 1s and 0s respectively and adds them to a list called Flipped
    inverted = "".join(flipped)
    # Converts that list to a string called inverted
    print(f"The inverted binary is {inverted} ")
    # Displays the inverted binary to the screen
    back_to_decimal = int(inverted, 2)
    print(f"The inverted binary to decimal is {back_to_decimal}")
    # Converts and displays the inverted binary to an integer/decimal value
    complement = back_to_decimal + 1
    return bin(complement)[2:]
    # adds 1 to the integer and returns it's value in binary

while True:
    number = input("Enter a number to find it's twos complement or enter q to exit the program: ")
    if number.lower() == "q":
        break
    else:
    
        try:
            print(f"The two's complement is {twos_complement(number)}")
        except TypeError:
            print("Please enter a decimal number! ") 
        except ValueError:
            print("Please enter a decimal number!")     

    
    
