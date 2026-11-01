#assignment
# simple grading system
grade_mark = 56
if grade_mark >= 80:
    print("A")
elif grade_mark >=75:
    print("B+")
elif grade_mark >= 70:
    print("B")
elif grade_mark >= 65:
    print("C+")
elif grade_mark >= 60:
    print("C")
elif grade_mark >= 55:
    print("D+")
elif grade_mark >= 50:
    print("D")
elif grade_mark >= 45:
    print("E")
else:
    print("F")

print(grade_mark)

# a simple calculator
def handle_multiplication(a, b):
    return a * b

def handle_division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def handle_addition(a, b):
    return a + b

def handle_subtraction(a, b):
    return a - b 

def handle_modulo(a, b):
    """
    Returns the remainder of dividing the dividend by the divisor.
    Safely handles zero division. dividend = a, divisor = b
    """
    if b == 0:
        return "Error: Cannot divide by zero!"
    
    return a % b

print("A Simple Calculator")
print("1.ADD")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.MODULO")
print("6.EXIT")
operation = int(input("Please input your preferred choice:"))
if operation == 1:
    firstNumber = int(input("Please enter your first number:"))
    secondNumber = int(input("Please enter your  second number:"))
    print("Addition of the 2 numbers is ", handle_addition(firstNumber, secondNumber))
elif operation == 2 :
    firstNumber = int(input("Please enter your first number:"))
    secondNumber = int(input("Please enter your  second number:"))
    print("Subtraction of the 2 numbers is ", handle_subtraction(firstNumber, secondNumber))
elif operation == 3:
    firstNumber = int(input("Please enter your first number:"))
    secondNumber = int(input("Please enter your  second number:"))
    print("Multiplication of the 2 numbers is ", handle_multiplication(firstNumber, secondNumber))
elif operation == 4:
    firstNumber = int(input("Please enter your first number:"))
    secondNumber = int(input("Please enter your  second number:"))
    print("Division of the 2 numbers is ", handle_division(firstNumber, secondNumber))
else:
    firstNumber = int(input("Please enter your first number:"))
    secondNumber = int(input("Please enter your  second number:"))
    print("Modulo of the 2 numbers is ", handle_modulo(firstNumber, secondNumber))

final = int(input("Please enter 0 to exit to program:"))


#phonebook system
"""
my original attempt
"""
my_phonebook = {"name":"Kwesi", "phone_number": int(["0546884935"])}, {"name":"Ama", "phone number":int(["0244798405"])}, {"name":"Kwame", "phone number":int(["0505679000"])}, {"name":"Esi", "age":int(["0207897895"])}
for name,phone_number in my_phonebook.items():
    print(name,phone_number)

def phone_number_info(status):
    match status:
        
        case int(["024"]):
            return "MTN"
        case int(["025"]):
            return "MTN"
        case int(["053"]):
            return "MTN"
        case int(["054"]):
            return "MTN"
        case int(["055"]):
            return "MTN"
        case int(["059"]):
            return "MTN"
        case int(["020"]):
            return "TELECEL"
        case int(["050"]):
            return "TELECEL"
        case int(["023"]):
            return "AIRTELTIGO"
        case int(["026"]):
            return "AIRTELTIGO"
        case int(["027"]):
            return "AIRTELTIGO"
        case int(["056"]):
            return "AIRTELTIGO"
        case int(["057"]):
            return "AIRTELTIGO"
        
"""
my corrected version with AI use
"""
# phonebook system
my_phonebook = [
    {"name": "Kwesi", "phone_number": "0546884935"},
    {"name": "Ama", "phone_number": "0244798405"},
    {"name": "Kwame", "phone_number": "0505679000"},
    {"name": "Esi", "phone_number": "0207897895"},
]

def phone_number_info(phone_number):
    prefix = phone_number[:3]
    match prefix:
        case "024" | "025" | "053" | "054" | "055" | "059":
            return "MTN"
        case "020" | "050":
            return "TELECEL"
        case "023" | "026" | "027" | "056" | "057":
            return "AIRTELTIGO"
        case _:
            return "Unknown network"

for contact in my_phonebook:
    network = phone_number_info(contact["phone_number"])
    print(contact["name"], contact["phone_number"], network)