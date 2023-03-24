import random
luckylist = []
for guess in range(1,7):
     guess1 = (random.randint(0,99))
     luckylist.append(guess1)
active = True
while active:
   play1 = int(input("Enter a number;enter 'q  to quit.; "))
   play2 = int(input("Enter another number; "))
   play3 = int(input("Enter another number; "))
   play4 = int(input("Enter another number; "))
   play5 = int(input("Enter another number; "))
   play6 = int(input("Enter another number; "))
   if play1 == 'q':
      active = False
   elif play1 == luckylist[0] and play2 == luckylist[1] and play3 == luckylist[2] and play4 == luckylist[3] and play5 == luckylist[4] and play6 == luckylist[5]:
       print("Congratulations,you have won the jackpot!!")
   else:
       print("Sorry try again,\n "
             f"These where the lucky numbers {luckylist}")
   # play5 = int(input("Enter another number; "))
   # play6 = int(input("Enter another number; "))
    # if play1 == luckylist[0]:
   #     print("You have one leg.\n")
   # elif play1 == luckylist[0] and play2
   # if play1 == luckylist[0] and play2 == luckylist[1]:
   #     print("You have two sure.")
   # elif play1 == luckylist[0] and play2 != luckylist[1]:
   #     print(f"Sorry,these were the luckynumbers,{luckylist}"
   #           f"You guessed {play1} instead of {luckylist[0]}\n"
   #           f"and {play2} instead of {luckylist[1]}")
   #        if play1 == luckylist[0] and play2 == luckylist[1] and play3 == luckylist[2] and play4 == luckylist[3] and play5 == luckylist[4] and play6 == luckylist[5]:
   #            print("Congratulations,you have won the jackpot!!")
   #        else:
   #             print("Sorry try again,\n "
   #                      f"These where the lucky numbers {luckylist}")



   # if play1 == lotterynum[0]:
   #      print("You have one leg.")
   # else:
   #       print(f"These were the lucky numbers.{lotterynum}\n"
   #               f"You guess the first number as {play1} whilkilch is incorrect")
   #       elif play2 == lotterynum[1]:
   #           print("You have two-sure.")
   #       else:
   #           print(f"These were the lucky numbers.{lotterynum}\n"
   #                 f"You guess the second number as {play2} which is incorrect.")
   #           elif play3 == lotterynum[2]:
   #               print("Congratulations,you have three strikes.")
   #           else:
   #               print(f"These were the lucky numbers.{lotterynum}\n"
   #                     f"You guess the third number as {play3} which is incorrect.")
   #               elif play4 == lotterynum[3]:
   #                   print("Congratulations,you have four strikes..")
   #               else:
   #                   print(f"These were the lucky numbers.{lotterynum}\n"
   #                         f"You guess the first number as {play1} which is incorrect.")
   #                   elif play5 == lotterynum[4]:
   #                       print("Congratulations,you got five strikes..")
   #                   else:
   #                       print(f"These were the lucky numbers.{lotterynum}\n"
   #                             f"You guess the first number as {play1} which is incorrect.")
   #                       elif play6== lotterynum[5]:
   #                           print("Congratulations you won.")
   #                       else:
   #                           print(f"These were the lucky numbers.{lotterynum}\n"
   #                                 f"You guess the first number as {play1} which is incorrect.")
   #           break
   #



