class Employee:
    no_of_employees = 8

    def __init__(self, aname, aage, asubject):
        self.name = aname
        self.age = aage
        self.subject = asubject

    def printdetails(self):
        return f"Name is {self.name}. Age is {self.age}. and subjects are {self.subject}"

    @classmethod
    def change_level(cls,newlevel):
        cls.no_of_employees = newlevel

    @classmethod
    def from_str(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])


harry = Employee("Aarushi", 13 , ["fench" , "korean "])
larry = Employee("Rohan", 12, ["Aar","ss"])
karan = Employee.from_str("karan-480-student")

print(karan.age)
# Employee.change_level(34)

# print(harry.no_of_employees)


