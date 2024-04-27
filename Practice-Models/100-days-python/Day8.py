set = {2,3,44,5,6,4,3,2,2,2,2,2,2}
print(set)

set.add("Hello")
print(set)

# harry= set()
# print(type(harry))

s1 = {1,2,3,4,5}
s2={4,5,6,7,7,8}

print(s1.union(s2))
s1.update(s2)
print(s1)
print(s2)
print("###############333")
print(s1.intersection(s2))

city = {"Tokyo","Seoul","India"}
city2 = {"Tokyo"}

print(city2.issubset(city))

city.remove("Tokyo")
print(city)
city.discard("bharat")

print("############################")
# city.remove("bharat")

del city