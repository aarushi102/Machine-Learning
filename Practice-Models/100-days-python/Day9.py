key = {1:"What", 2:"is"}

print(type(key),key)

dic = {
    345:"Aarushi",
    78:"Lara",
    99:"Brain"
}

print(dic[78])
print(dic.keys())
print(dic.values())
# print(dic.get[90])

print(dic.items())

for key, value in dic.items():
    print(f'The value correspnding to the key {key} is {value}')


ep ={
    122:45,
    57:78,
    65:99,
    99:100
}

print(ep)

ep2 = {333:19,
90:78
}

print(ep.update(ep2))
print("##################")

print(ep)

print(ep.popitem())
print(ep)

del ep[65]

print(ep)
del ep
print(ep)
