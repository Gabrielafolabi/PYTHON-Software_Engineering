import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','W', 'X', 'Y', 'Z']

Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

Symbols = ['`', '!', '@', '#', '$', '%', '^', '&', '*']

print('HELLO! I AM ROBOT GABE, I GENERATE PASSWORD... HOW CAN I BE OF HELP? \n')

Response = input('Would you like to generate a password?  \n Enter Yes/No:  \n')

if Response == 'Yes' or 'YES':
    while True:
        no_letter = (input('Enter the number of letters you desire:  \n'))
        if no_letter.isdecimal():
            break
        print('Please enter a digit')

    while True:
        no_numbers = (input('Enter the number of digits you desire:  \n'))
        if no_numbers.isdecimal():
            break
        print('Please enter a digit')

    while True:
            
        no_symbols = (input('Enter the number of symbols you desire:  \n'))
        if no_symbols.isdecimal():
            break
        print('Please enter a digit')
else:
    print('Thanks for visiting our sites')

New_no_letter =int(no_letter)
New_no_numbers = int(no_numbers)
New_no_symbols = int(no_symbols)

Pass_Letter=[]
for i in range(1, New_no_letter+1):
    char = random.choice(Letters)
    Pass_Letter += char

for i in range(1, New_no_numbers+1):
    char = random.choice(Numbers)
    Pass_Letter += char

for i in range(1, New_no_symbols+1):
    char = random.choice(Symbols)
    Pass_Letter += char

#print(Pass_Letter)
random.shuffle(Pass_Letter)
#print(Pass_Letter)

New_Pass = ""
for char in Pass_Letter:
    New_Pass += char
print(New_Pass)




    


               
