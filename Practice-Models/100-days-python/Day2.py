import os
os.system("python --version")

numbers =10
# for i in range(0,10):
#     print(i)

# i = 1
# while(i<9):
#     print(i)
#     i = i+1

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum+i
    
#     print ("Average is ", sum/len(numbers))


# average(9,10,11)

def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  area = length * width
  return area

# Get the length and width from the user
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Call the function to calculate the area
area = calculate_area(length, width)

# Print the area
print(f"The area of the rectangle is: {area}")
