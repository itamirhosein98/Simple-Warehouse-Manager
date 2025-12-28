import re
text = "my phone number is 123-456-7890"
result = re.findall(r'\d+', text)
print("Found phone numbers:", result)

try:
    number = int(input("enter your number:  "))
    result = 10 / number
    print(result)
except ZeroDivisionError:
    print("error! division by zero is not allowed.")
except ValueError:
    print("error! please enter a valid integer.")
       
       
def divition():
    try:
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        result = num1 / num2
        print(f"The result of {result}")
    except ZeroDivisionError:
        print("error! division by zero is not allowed.")
    except ValueError:
        print("error! please enter a valid integer.")
divition()
                   
                   
def save_nots():
    note = input("enter your note: ")
    with open("notes.txt", "a" ,encoding= "utf-8") as file:
        file.write(note + "\n")
    print("note saved successfully.")
def read_nots():
    try:
        with open("notes.txt", "r" ,encoding= "utf-8") as file:
            print("saved notes:")
            print(file.read())
    except FileNotFoundError:
        print("no notes found.")
save_nots()
read_nots()
            
            
def number(num):
    if num % 2 == 0 and num > 0:
        return num * 2
    elif num % 2 == 1 and num >45 0:
        return num / 2
    else:
        return "please enter a positive number."
input_num = int(input("enter your number: "))
print(number(input_num))
