
a=10 #Global variable
def display():
    a=15 #Local variable
    print(a)
print(a)
display()


a=10 #Global variable
def display():
    global a    # To make variable useful in the local scope
    a = a + 15 #Local variable
    print(a)
print(a)
display()


name = "Ola" 
def noun():
    global name
    name = "How are you " + name
    print(name)
print(name)
noun()


