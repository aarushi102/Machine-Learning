#only for streak
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id =id

    def showDetails(self):
        print(f"The name is {self.name} & id is {self.id}")

class Pogrammer(Employee):
    def showLanguage(self):
        print("The default language is python")


e1 = Employee("Aarushi", 30)
e1.showDetails()
e2 = Pogrammer("Vivek",92)
e2.showDetails()
e2.showLanguage()