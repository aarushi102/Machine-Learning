def welcome():
    print("Welcome here you are aarushi ")


print(__name__)
if __name__ == "__main__":
    welcome()


import os

# if (not os.path.exists("stupid")):
#     os.mkdir("stupid")

# for i in range (1,10):
#     os.mkdir(f"stupid/day{i+1}")

folder = os.listdir("./")
print(folder)

# os.rmdir("stupid/day3")
# os.rmdir("stupid/day4")
# os.rmdir("stupid/day5")
# os.rmdir("stupid/day6")
# os.rmdir("stupid/day7")
# os.rmdir("stupid/day8")
# os.rmdir("stupid/day9")
# os.rmdir("stupid")

# file = open('myfile2.txt', 'a')
# # print(file)
# file.write("Hello How are you another python program to run \n")
# file.close()

# print(file)
# f = file.read()
# print(f)
# file.close()

# with open('myfile.txt','a') as f:
#     f.write("So I am doing this again and again because tis is fun")


f =open('myfile.txt','r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)