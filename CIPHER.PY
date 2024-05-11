alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','W', 'X', 'Y', 'Z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','W', 'X', 'Y', 'Z', ' ', '.']




def encode(plain_text, shift_number):
    new_letter = ""
    for i in plain_text:
        position = alphabet.index(i)
        new_position = position + shift_number
        shift_letter = alphabet[new_position]
        new_letter += shift_letter
    print(f"Your encoded text is {new_letter}")


def decode(plain_text, shift_number):
    new_letter = ""
    for i in plain_text:
        position = alphabet.index(i)
        new_position = position - shift_number
        shift_letter = alphabet[new_position]
        new_letter += shift_letter 
        
    print(f"Your decoded text is {new_letter}")


should_continue = True
name = input("What is your name?")
print(f"Hi {name} do you want to encode or decode a text:  ")
while should_continue:
    while True:
        direction = input ("please input encode or decode:  ")
        if direction == "encode" and "decode":
            break
        elif direction == "decode":
            break
        #print ("please input encode or decode")
    text = input("your plain text:  ").lower()
    shift = int(input("put in the private crypto key:  "))
    
    
    if direction == "encode":    
        encode(plain_text=text, shift_number=shift)
    elif direction == "decode":
        decode(plain_text=text, shift_number=shift)
    response = input("Do you wish to continue?, Yes or No:  ")
    
    if response == "No":
        should_continue = False
print(f"Goodbye {name}")
        
        
        
    
    
    
    
    
