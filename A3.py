# W.A.P to create a calculator (for each operator keep separate function).

def ad(i,j):
    print("Addition ", (i+j))
    
def sub(i,j):
    print("Subtraction ", (i-j))
    
def mul(i,j):
    print("Multiplication ", (i*j))
    
def div(i,j):
    print("Division ", (i/j))
    
def mod(i,j):
    print("Modulo ", (i%j))
    
def pow(i,j):
    print("Power ", (i**j))


print("Give input for Calculator ... ")
k=0

while(k!=7):
    
    k = int(input("press 1. Add, 2. Mul, 3. Div, 4. Sub, 5. Modulo, 6. Power, 7. Exit"))

    i=int(input("enter number 1: "))
    j=int(input("enter number 2: "))
    
    if(k==1):
        ad(i,j)
        
    elif(k==2):
        mul(i,j)
     
    elif(k==3):
        div(i,j)
     
    elif(k==4):
        sub(i,j)
     
    elif(k==5):
        mod(i,j)
     
    else:
        pow(i,j)
     




 