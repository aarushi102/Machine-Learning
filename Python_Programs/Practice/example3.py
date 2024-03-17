# factorial another method

def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)
num = int(input())
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")  
else:
    print("Factorial is", factorial(num))
