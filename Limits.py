
    
while True:
    limit = int(input("Please type in your limit:  "))
    if limit > 0:
        break
    print("Please enter a limit greater than 0")
even_add = 0
odd_add = 0
            
for num in range (1, limit + 1):
    if num % 2 == 0:
        even_add = even_add + num
    else:
        odd_add = odd_add + num   
print(f"The limit you entered is :  {limit}")
print(f"Addition of Odd numbers is  {odd_add}")
print(f"Addition of Even numbers is  {even_add}")  