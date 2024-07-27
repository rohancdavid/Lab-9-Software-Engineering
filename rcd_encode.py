# Lab 9: Encode Function
# Rohan David

def encode(password):
    encoded_str = []
    for i in password:
        digit = chr(ord(i) + 3)
        encoded_str.append(digit)
    return ''.join(encoded_str)

def decode(password): # decode function added by Samantha Wong 
    new_string = ""
    for i in range(len(password)):
        x = int(password[i]) -3
        new_string += str(x)
    return new_string


def main():
    password = None
    encoded_str = None
    while True:
        #menu
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        #option
        option = int(input("Please enter an option: "))
        if option == 1: #encode
            password = input("Please enter your password to encode: ")
            encoded_pw = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == 2: #decode
            decode(encoded_pw)
            print(f"The encoded password is {encoded_pw}, and the original password is {password}.\n")

        elif option == 3: #quit
            break


if __name__ == "__main__":
    main()