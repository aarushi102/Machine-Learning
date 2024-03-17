print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay lets play :) ")

answer = input("What does gpu stands for? ")
if answer == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect:(")

answer = input("What does cpu stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect:(")

answer = input("What does rom stand for? ")
if answer == "read only memory":
    print("Correct!")
else:
    print("Incorrect:(")

answer = input("What does ram stand for? ")
if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect:(")

