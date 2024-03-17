class mera:
    def __init__(self, aname):
        self.name = aname

    def naam(self):
        return f"Hello, My name is {self.name}"

aaru = mera("Aarushi")
piyu = mera("AjayKumar")
surname = mera("Tiwari")

print(aaru.naam())
print(piyu.naam())
print(surname.naam())