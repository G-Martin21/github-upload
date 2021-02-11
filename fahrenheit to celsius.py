import random
roll = random.randint

#promp fahrenheit temperature
#temperature = input("Introduce a Fahrenheit temperature: ")
#if temperature.isnumeric() == False:   #check if is a number
  #  print('Value is not a number.')
  #  exit()
#else:
   # fahrenheit = int(temperature)

#celsius = (fahrenheit - 32) * 5/9       #convert to celsius
#print(int(celsius))  #output result
#Simple Calculator
legal_operations = ["+", "-", "*", "/", "^", "%"]
first_number = input("First number: ")
if first_number.isnumeric() == False:   #check if is a number
    print('Value is not a number.')
    exit()
operation = input("Operation: ")
if operation in legal_operations:
    second_number = input("Second number: ")
else:
    print("Not a valid operation")
    exit()  

if second_number.isnumeric() == False:   #check if is a number
    print('Value is not a number.')
    exit()    

if operation == "+":
    result = int(first_number) + int(second_number)
    print(result)
elif operation == "*":
    result = int(first_number) * int(second_number)
    print(result)