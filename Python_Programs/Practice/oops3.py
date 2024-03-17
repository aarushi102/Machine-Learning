class Employee:
    no_of_employees = 8
    pass

harry = Employee()
larry = Employee()

harry.name = "Aarushi"
harry.age = 11
harry.subject = ["french","English","Marathi"]

larry.name ="Tiwari"
larry.age = 13
larry.subject = ["physics", "marathi"]

# print(larry.subject)
# print(harry.no_of_employees)
harry.no_of_employees = 9
print(harry.__dict__)
print(harry.no_of_employees)

print(harry.__dict__)
 