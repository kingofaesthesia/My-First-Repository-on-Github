import random
jackpotbox = []
for numbers in range(1,7):
    jackpotbox.append(random.randint(0,99))

time = 0
userguess = []
correct_guess = []
active = True
while len(userguess) < 6 and active == True:
    inputguess = input("Enter your lucky guesses\n"
                       "Enter 'Q' to Quit; ").upper()
    if inputguess == 'Q':
       active == False
       break
    elif inputguess == int(inputguess):
     continue

    if int(inputguess) in jackpotbox:
      correct_guess.append(int(inputguess))

    if int(inputguess) in userguess:
         print("Entry already inputed.")
         continue
    elif int(inputguess) not in userguess:
         userguess.append(int(inputguess))

for num in userguess:
      if num in jackpotbox:
          time = time + 1
if time == 0:
       print("Uh-Oh,No winning today,\n"
            f"These were the lucky numbers,{jackpotbox}\n"
            f"You guessed these {userguess}")

elif time == 1:
       print("You have One leg,\n"
            f"These were the lucky numbers,{jackpotbox}\n"
            f"You guessed these {userguess}")

elif time == 2:
     print("Congrats,you got Two sure!!\n"
            f"These were the lucky numbers,{jackpotbox}\n"
            f"You guessed these {userguess}\n")

elif time == 3:
     print("Congrats,you got Three strikes!!"
            f"These were the lucky numbers,{jackpotbox}\n"
            f"You guessed these {userguess}\n")

elif time == 4:
     print("Congrats,you got Four strikes!!"
           f"These were the lucky numbers,{jackpotbox}\n"
            f"You guessed these {userguess}\n")

elif time ==  5:
    print("Congrats,you got five strikes,so close!!!\n"
          f"These were the lucky numbers,{jackpotbox}\n"
          f"You guessed these {userguess}\n")
elif time == 6:
    print("Congratulations,You Won The JACKPOT!!!!!!\n"
          f"These were the lucky numbers,{jackpotbox}\n"
          f"You guessed these {userguess}")