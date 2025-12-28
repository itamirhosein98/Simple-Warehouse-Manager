# def doble(x):
#     return x * 2
# doble = lambda x: x * 2
# print(doble(5))
def number(x, y):
    return x * y
number = lambda x, y: x * y
input1 = int(input("enter first number: "))
input2 = int(input("enter second number: "))
print(number(input1, input2))