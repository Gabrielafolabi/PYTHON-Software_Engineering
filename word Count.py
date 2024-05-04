words = input("please type in your words")

space_count = 0

for char in words:
    if char == " ":
        space_count = space_count + 1
        
print (words)

print (f"your space_count is :  {space_count}")

word_count = space_count + 1
print(f"your word_count is :  {word_count}")