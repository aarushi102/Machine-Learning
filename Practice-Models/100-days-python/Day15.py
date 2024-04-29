# with open('myfile.txt','r') as f:
#     print(type(f))

#     f.seek(10)

#     print(f.tell())
#     data = f.read(5)
#     print(data)

# def double(x):
#     return x*2

# print(double(5))


# db = lambda x : x*2
# print(db(2))

# lambda arguments : expression
########  MAP

def cube(x):
    return x * x * x

print(cube(3))

l = [2,3,4,8,7,6,5]

newl = list(map(cube,l))
print(newl)

# map(function,iterable)


# filter 
def filter_function(a):
    return a<4

newnewl = list(filter(filter_function,l))
print(newnewl)

from functools import reduce
