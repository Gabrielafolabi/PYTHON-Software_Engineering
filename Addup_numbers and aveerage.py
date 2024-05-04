print("Adding up sum numbers between 1000 to 1500")
i = 0
count = 1000
while ( count<=1500 ):
    i = i + count
    count = count + 1
print (f"the sum is {i}")


# Initialize variables
total = 0
num = 1000

# Use a while loop to iterate through numbers from 1000 to 1500
while num <= 1500:
    total += num  # Add current number to the total
    num += 1  # Increment number by 1 for the next iteration

# Print the result
print("The sum of numbers between 1000 and 1500 inclusive is:", total)

