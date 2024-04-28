import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter your Choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    Choice = int(input("Enter your Choice"))

    while Choice>3 or Choice<1:
        Choice= int(input("Enter a valid Choice please"))
    

    if Choice == 1:
        Choice_name = 'Rock'
    elif Choice==2:
        Choice_name = 'Paper'
    else:
        Choice_name='Scissors'

    print(f"Users Choice is {Choice_name}")

    print("Now its computers turn")

    comp_Choice = random.randint(1,3)

    while comp_Choice==Choice:
        comp_Choice = random.randint(1,3)

    if comp_Choice == 1:
        comp_Choice_name = 'rocK'
    elif comp_Choice == 2:
        comp_Choice_name = 'papeR'
    else:
        comp_Choice_name = 'scissoR'
    print("Computer Choice is \n", comp_Choice_name)
    print(Choice_name,'Vs',comp_Choice_name)


    if Choice == comp_Choice:
        print('Its a Draw',end="")
        result="DRAW"
    # condition for winning      
    if (Choice==1 and comp_Choice==2):
        print('paper wins =>',end="")
        result='papeR'
    elif (Choice==2 and comp_Choice==1):
        print('paper wins =>',end="")
        result='Paper'

    if (Choice==1 and comp_Choice==3):
        print('Rock wins =>\n',end= "")
        result='Rock'
    elif (Choice==3 and comp_Choice==1):
        print('Rock wins =>\n',end= "")
        result='rocK'
         
    if (Choice==2 and comp_Choice==3):
        print('Scissors wins =>',end="")
        result='scissoR'
    elif (Choice==3 and comp_Choice==2):
        print('Scissors wins =>',end="")
        result='Rock'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == Choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")

    ans = input().lower()
    if ans =='n':
        break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
