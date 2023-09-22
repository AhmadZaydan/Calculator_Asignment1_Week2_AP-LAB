#Function for addition
def add(x,y):
    result = x + y
    return result

#Function for substraction
def subs(x,y):
    result = x - y
    return result

#Function for multiplication
def mult(x,y):
    result = x * y
    return result

#Function for division
def div(x,y):
    result = x / y
    return result

#Function for power
def pow(x,y):
    result = x ** y
    return result

#Function to calculate inputted numbers
def calculate(calc, x, y):
    if(calc == "add"):
        res = add(x, y)

    if(calc == "subs"):
        res = subs(x, y)
        
    if(calc == "mult"):
        res = mult(x, y)
        
    if(calc == "div"):
        res = div(x, y)
    
    if(calc == "pow"):
        res = pow(x, y)
           
    return res

#Function to check wether the first number inputted is numeric or not
def checker1():
    check = False
    while check == False:
        num = input("Enter first number: ")
        if num.isnumeric():
            num = float(num)
            check = True
            return num
        else:
            check = False

#Function to check wether the second number inputted is numeric or not
def checker2():
    check = False
    while check == False:
        num = input("Enter second number: ")
        if num.isnumeric():
            num = float(num)
            check = True
            return num
        else:
            check = False

#Get first number
num1 = checker1()
print("")

#Choose calculation method
calc = input("choose calculation method(add, subs, mult, div, pow): ")
print("")

#Get second number
num2 = checker2()
print("")

#Get result
num3 = calculate(calc, num1, num2)
print(num3)
print("")

#Give choice to continue or quit
choice = input("continue or quit?  ")

if(choice == "continue"):
    print("")
    counter = False
    while(counter == False):
        calc = input("choose calculation method(add, subs, mult, div, pow): ")
        print("")
        num4 = checker2()
        print("")
        print(calculate(calc, num3, num4))
        print("")
        num3 = calculate(calc, num3, num4)
        print("")
        choice = input("continue or quit?  ")

        if(choice == "continue"):
            print("")
            counter = False

        elif(choice == "quit"):
            counter = True
            print("stop")

elif(choice == "quit"):
    print("stop")

