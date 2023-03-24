import random
jackpotbox = []
for numbers in range(1,7):
    jackpotbox.append(random.randint(0,99))
    print(jackpotbox)

player_guess = []
while len(player_guess) < 6:
    gameplay = input('''
    Guess the Correct 6 numbers to win the Jackpot
    Enter a number to play
    Enter 'Q' to Quit.
    ''').upper()
    if gameplay == 'Q':
         break
    elif gameplay == int(gameplay):
        player_guess.append(gameplay)

        if player_guess == jackpotbox:
            print("Congratulations,you've won the Jackpot!!!!")

        elif player_guess[0] == gameplay[0]:
            print("Youre almost close")