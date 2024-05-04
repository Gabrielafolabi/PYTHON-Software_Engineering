count = 1
sum = 0

while (count <= 2):
    try:
        num = input("input a number : ")
        num2 = int(num)
        sum = sum + num2
        count = count + 1
    except ValueError:
        print("Please enter a valid number")
print(f"The sum of your numbers is : {sum}")

average = sum/2
print(f"The average is : {average}")
