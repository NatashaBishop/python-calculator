# Four function Calculator commandline tool
# This Python calculator is a coursework for 
# Westminter Adult Education Service Colledge
#for Level 2 Software Development Sertificate

# -------------------------------------------------------- #
# -- CALCULATOR ------------------------------------------ #
# -------------------------------------------------------- #

# Adding numbers function:
def add(a, b):
    return a + b

# Subtracting numbers function:
def sub(a, b):
    return a - b

# Multiplying numbers function:
def mult(a, b):
    return a * b

# Dividing numbers function:
def div(a, b):
    if b != 0:
        return a / b
#handling division by zero:
    else:
        print("Division by zero is not allowed")
        b = None

# declaring variables:
a = None
b = None
operator = None

while (True):
    # Prompting user to input values
    a = input("Enter the first argument: ")
    operator = input("Enter the operator: ")
    b = input("Enter the second argument: ")
  #converting values to integers
    try:  
        a = int(a)
        b = int(b)
    except ValueError:
        print ("Invalid number argument...")
        operator = None

    # making the decision:
    if (operator != None):
        if (operator == "+"):
            print ("Sum: ", add(a, b))
        elif (operator == "-"):
            print ("Difference: ", sub(a, b))
        elif (operator == "*"):
            print ("Multiplication: ", mult(a, b))
        elif (operator == "/"):
            div(a, b)
        else:
            print ("Invalid operator")
        break
