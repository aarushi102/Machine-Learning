class Person:
    # name = "Harry"
    # occupation = "Engineer"
    # networth = 10
    def __init__(self,n,o):
        print("Hi am contructor")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Harry","Develper")
b = Person("Hari","HR")

a.info()
b.info()

# # a.name = "Shubham"
# # a.networth = 20

# # print(a.name,a.networth)
# a.info()


