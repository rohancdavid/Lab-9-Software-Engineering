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
