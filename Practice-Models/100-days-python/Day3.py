l = [3,5,6,7,8,8,0]
print(type(l))
print(l)
print(l[0])

#beest way to get ri of negative indexing we do length of list -1
print(len(l))
print(l[1:-2])
print(l[1:6])

lst = [i for i in range(20)]
print(lst)

lst = [i for i in range(20) if i%2==0]
print(lst)


l2 = [11,23,1,2,3,4,5,67,87,55,4,33]
print(l2)

l2.append(3)
print(l2)

l2.sort()
print(l2)

l2.reverse()
print(l2)

l3=l+l2
l3.sort()
print(l3)