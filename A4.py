# W.A.P to handle file opening (file not found) and divide by zero exception.


def div(a,b):
    
    try:
        print("Division ", (a/b))
    except ZeroDivisionError:
        print("Division by zero error :( ")
    
print("Exeption handling .. ")    

a=int(input("enter number 1: "))
b=int(input("enter number 2: "))

div(a,b)


print("File handling .. ")

try:
    str = input("Enter the file name ")
    fhand=open(str)
    for line in fhand:
        print("data is ", line)

except FileNotFoundError:
        print("File not found error :( ")

  