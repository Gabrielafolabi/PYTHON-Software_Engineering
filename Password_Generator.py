import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','W', 'X', 'Y', 'Z']

Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

Symbols = ['`', '!', '@', '#', '$', '%', '^', '&', '*']

print('HELLO! I AM ROBOT GABE, I GENERATE PASSWORD... HOW CAN I BE OF HELP? \n')

Response = input('Would you like to generate a password?  \n Enter Yes/No:  \n')

if Response == 'Yes' or 'YES':
    no_letter = int(input('Enter the number of letters you desire:  \n'))
    print('Please enter a digit') 
    no_numbers = int(input('Enter the number of digits you desire:  \n'))
        
    print('Please enter a digit')
    no_symbols = int(input('Enter the number of symbols you desire:  \n'))
        
    print('Please enter a digit')
else:
    print('Thanks for visiting our sites')

Pass_Letter=[]
for i in range(1, no_letter+1):
    char = random.choice(Letters)
    Pass_Letter += char

for i in range(1, no_numbers+1):
    char = random.choice(Numbers)
    Pass_Letter += char

for i in range(1, no_symbols+1):
    char = random.choice(Symbols)
    Pass_Letter += char

print(Pass_Letter)
random.shuffle(Pass_Letter)
print(Pass_Letter)

New_Pass = ""
for char in Pass_Letter:
    New_Pass += char
print(New_Pass)




    


               
