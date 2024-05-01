# class Person:
    # name = "Harry"
    # occupation = "Engineer"
    # networth = 10
#     def __init__(self,n,o):
#         print("Hi am contructor")
#         self.name = n
#         self.occupation = o

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = Person("Harry","Develper")
# b = Person("Hari","HR")

# a.info()
# b.info()

# # a.name = "Shubham"
# # a.networth = 20

# # print(a.name,a.networth)
# a.info()


# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using it")
#     return mfx

# @greet
# def hello():
#     print("Hello World")

# hello()

class MyClass:
    def __init__(self):
        self.value = Value
    
    def show(self):
        print(f"Value is {self._value}")
    
    @property
    def value(self):
        return self._value

