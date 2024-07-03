import random
options=["Rock","Paper","Scissors"]
print("ROCK PAPER SCISSORS")
print("****************************************************************")
useroption=input("enter Rock or Paper or Scissors ")
computerchoice=random.choice(options)
print("you chose the option ",useroption)
print("computer chose the option",computerchoice)
if useroption==computerchoice:
    print("its a tie with the computer")
elif useroption=="Rock" and computerchoice=="Scissors":
    print("you win against the computer")
elif useroption=="Paper" and computerchoice=="Rock":
    print("you win against the computer")
elif useroption=="Scissors" and computerchoice=="Paper":
    print("you win against the computer")
elif useroption=="Rock" and computerchoice=="Paper":
    print("you lost against the computer")
elif useroption=="Paper" and computerchoice=="Scissors":
    print("you lost against the computer")
elif useroption=="Scissors" and computerchoice=="Rock":
    print("you lost against the computer")
else:
    print("invalid option choosen")
print("****************************************************************")   