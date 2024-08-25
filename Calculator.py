def sum(n1, n2):
    return n1 + n2 

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def subtract(n1, n2):
    return n1 - n2

operator = {
    "*": multiply,
    "-": subtract,
    "/": divide,
    "+": sum,    
    }



def Goodbye():
    print("Thanks for your time")

def calculate():
    while True: 
        Num1 = ((input("what is the first number: ")))
        
        if Num1.isdecimal():
            break
        print("Provide a digit")
    Num1_new = int(Num1)
    calculator_robot = True
    while calculator_robot:
        print("See given operators below: \n")
        
        for symbol in operator:
            print(symbol)  
            
        op_select = (input("Choose your operator: "))
        #print(operator[op_select])
        
        while True: 
            Num2 = ((input("what is the other number: ")))
            
            if Num2.isdecimal():
                break
            print("Provide a digit")
        Num2_new = int(Num2)
        output = operator[op_select](Num1_new, Num2_new)
        print(f"{Num1_new} {op_select} {Num2_new} = {output}")

        response = (input(f"enter y to continue with {output} and n to discontinue or exit : "))

        if response == "exit":
            calculator_robot = False
            Goodbye()
        elif response == "y":
            Num1_new = output
        elif response == "n":
            calculator_robot = False
            calculate()
        
calculate()