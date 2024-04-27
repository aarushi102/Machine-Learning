for i in range(3):
    print(i)
else:
    print("Sorr")

number = input("Enter a number: ")

print(f"the multiplicatin of {number} are as follows")
try:

    for i in range(1,11):
        print(f"{number} X {i} = ", int(number)*i)
# except Exception as e:
#     print(e)
except:
    print("Please enter valid format")

finally:
    print("They always executeme ")

print("other lines")
print("done executing")
