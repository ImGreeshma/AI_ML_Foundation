num1, num2, operator =  input("Enter number1 number2 and operator(+,-,*,/) seperated by comma:").split(",")
num1 = int(num1.strip())
num2 = int(num2.strip())
operator = operator.strip()

if(operator == '+'):
    result = num1 + num2
elif(operator == '-'):
    result = num1 - num2
elif(operator == "*"):
    result = num1 * num2
elif(operator == '/'):
    if(num2 == 0):
        print("Division By Zero")
        exit()
    else:
        result = num1 / num2
else:
    print ("invalid Operator")
    exit()

print(f"Result = {result} ")
