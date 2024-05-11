import random
random_integer = random.randint(1, 10)
print (random_integer)
#import my_module
#print (my_module.pi)
random_float = random.random()  #generate float between 0 and 1
print(random_float)

random_float * 8 # This is to extend the range

love_score = random.randint(1, 100)
print(f"your love score is:  {love_score}")


print(" Please click run to roll your dice")

dice_roll = random.randint(0, 1)

if dice_roll == 0:
    print (dice_roll)
    print("Tails")
else:
    print(dice_roll)
    print("Heads")



names = input("please drop your names")

names_lists = names.split()

names_len = len(names_lists)
random = random.randint (0, names_len-1) 

who_will_pay = names_lists[random]
print(names_lists)
print (random)
print("who will pay for bills: " +  who_will_pay)