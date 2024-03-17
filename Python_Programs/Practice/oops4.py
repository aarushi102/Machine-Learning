class Employee:
    no_of_employees = 8
    def __init__(self, aname, aage, asubject):
        self.name = aname
        self.age = aage
        self.subject = asubject

    def printdetails(self):
        return f"Name is {self.name}. Age is {self.age}. and subjects are {self.subject}"
         

harry = Employee("Aarushi", 13 , ["fench" , "korean "])
#larry = Employee()

# harry.name = "Aarushi"
# harry.age = 11
# harry.subject = ["french","English","Marathi"]

# larry.name ="Tiwari"
# larry.age = 13
# larry.subject = ["physics", "marathi"]

print(harry.printdetails())
#print(larry.printdetails())
