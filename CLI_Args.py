import sys


def add(num1,num2):
    result=num1+num2
    return result

num1=float(sys.argv[1])
num2=float(sys.argv[2])

print(add(num1,num2))
