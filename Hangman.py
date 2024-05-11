
import random
word_list = ["Car", "House", "Canada"]

random_choice = random.choice(word_list)

word_length = len(random_choice)

display = []
for i in range(word_length):
    display += "_"
    
print (display)
print (random_choice)
end_of_game = False
while not end_of_game:
    guess = input("Guess the letters").lower()
    #print (random_choice)
    for position in range(word_length):
        letter = random_choice[position]
        if letter == guess:
            display[position] = letter
    
            
    print (display)
    
        
