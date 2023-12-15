a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i in range(3,13):
    print("{:3d} {:5d} {:6d}".format(i, i*i, i*i*i))

# Formatted string
Balloons = 10
print("Sammy has {} balloons today!".format(Balloons))


for i in range(2, 4):
    print(i, end= " ")



#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if lastdigit > 5:
    print(f"last digit of {number} is {lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"last digit of {number} is {lastdigit} and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print(f"last digit of {number} is {lastdigit} and less than 6 and not 0")


for i in range(10):
    for j in range(i + 1, 10):
        print("{:02d}".format(i * 10 + j), end=", " if i < 9 or j < 8 else "\n")








import random
number = random.randint(-10, 10)

if number > 0:
    print("{} is positive" .format(number), end = " ")

elif number == 0:
    print("{} is zero" .format(number), end = " ")

elif number < 0:
    print("{} is negative" .format(number), end = " ")



def my_function(counter=89):
    print("Counter: {}".format(counter))

    my_function(89)