Num2 = 0
while True:
    Num = int(input("Input your values"))
    Num2 = Num2 + Num
    if Num < 0:
        Num2 = Num2 - Num
        break
print(f"The sum of all your valid values inputted is :  {Num2}")

