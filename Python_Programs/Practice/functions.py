def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def islesser(m,n):
    pass

def largestAmongThem(c,d):
    if c>d:
        print(c)
    else:
        print(d)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum =sum + i
    print(sum)

average(1,2,3,4,5,6,7,8,9,10)

# largestAmongThem(77,89)
# largestAmongThem(100,89)
# calculateGmean(9,10)
# calculateGmean(91,100)