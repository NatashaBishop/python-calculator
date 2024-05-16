**Client Brief:**

Develop a Basic Calculator application that allows users to perform simple arithmetic operations such as addition, subtraction, multiplication, and division. The application should be user-friendly, prompt the user for inputs, perform the calculation, and display the result. It should also handle basic errors like division by zero and invalid inputs.

**Programming Requirements**

**● Intended Purpose:** 

Create the application that performs addition, subtraction, multiplication and division on user's imputed data and on user requested operation. 

**● Data Requirements:**

Data has to be provided by the user: numbers to be calculated and the arithmetic operation to be performed on the data provided.
● Audience: Anyone who has the need to perform basic calculations and has access to a device to run Python applications (such as a computer with Python 3 installed) and a hardware peripheral with text input capability (such as keyboard)
● Platform: Linux/Windows/MacOS based terminal
● Intended Use: To be used in the IT environment for basic calculations.
● Security: Operation system will check on the user rights when the operation system starts, the application will check on the data type and data size to prevent bots and malicious use. The datatype used will limit the data size. 


**Design Documentation**
*Pseudocode*
● Write your Pseudocode here, make sure it is at least 10 lines.
BEGIN
FUNCTION add(a, b)
	RETURN a + b
END FUNCTION

FUNCTION sub(a, b)
    RETURN a-b
END FUNCTION

FUNCTION mult(a, b)
    RETURN a*b
END FUNCTION

FUNCTION div(a, b)
    RETURN a/b
END FUNCTION
FUNCTION div(a, b)
    IF b is not 0 THEN
        RETURN a / b
    ELSE
        PRINT "Division by zero is not allowed"
END FUNCTION



WHILE True
# Get first argument from user
PRINT "Enter the first argument: " 
READ first argument

# Get operator from user
PRINT "Enter the operator: "
READ operator

\# Get second argument from user
PRINT "Enter the second argument: " 
READ second argument
# Convert a nab b to integers
	TRY:
        a = CONVERT_TO_INTEGER(a)
        b = CONVERT_TO_INTEGER(b)
   	 EXCEPT ValueError:
        PRINT "Invalid number argument..."
    # Making the decision:
    IF operator != None THEN
        IF operator == "+" THEN
            PRINT "Sum: ", add(a, b)
        ELIF operator == "-" THEN
            PRINT "Difference: ", sub(a, b)
        ELIF operator == "*" THEN
            PRINT "Multiplication: ", mult(a, b)
        ELIF operator == "/" THEN
            div(a, b)
        ELSE
            PRINT "Invalid operator"
        END IF
        BREAK
END

Flowchart
●	Lucidchart (https://www.lucidchart.com) used to build the required flowchart and convert it into image. Pleas, see file flowchart4calculator

 


