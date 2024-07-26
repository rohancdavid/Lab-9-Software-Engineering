# Lab 9: Encode Function
# Rohan David

def encode(password):
    encoded_str = []
    for i in password:
        digit = chr(ord(i) + 3)
        encoded_str.append(digit)
    return ''.join(encoded_str)

