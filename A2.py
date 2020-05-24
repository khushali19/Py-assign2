# Write a program to generate Fibonacci Series using recursion.


def fib(x):
                
    if x <= 1 :
        return x
    else :
        return (fib(x-1) + fib(x-2))
        
        
y = int(input("Enter the number "))

for i in range(y):
    
   print("Values are : ", fib(i))