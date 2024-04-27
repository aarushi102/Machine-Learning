print("Hello")

def recursion(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* recursion(n-1)

# print("###########################")
    
# recursion(6)
print(recursion(3))
print("###########################")

######### fibonacci series
def fibonacci(n):
    if (n==0 or n==1):
        return 1
    else:
        return fibonacci(n)
print("###########################")


f1 = 0
f2 = 1
# n = 9
n = int(input())
print(f1)
print(f2)
for i in range(n):
    # print(fibonacci)
    fibonacci = f1+f2
    print(fibonacci)
    f1 = f2
    f2 = fibonacci

print("###########################")

def next(n):
    if n<=1:
        return n
    else:
        return next(n-1) +next(n-2)

n = 10

print("fibonacci sequewnce")

for i in range(n):
    print(next(i))

