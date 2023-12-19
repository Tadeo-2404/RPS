import random
import os

types = ['r', 'p', 's']
globalScore = 0

def clear_screen():
    os.system('cls')

def checkScore():
    global globalScore 
    print(f'My score: {globalScore}')

def verify_input(user_input):
    if user_input not in ["r", "p", "s"]:
        return False
    return True

def rChoice(userInput, pcInput):
    global globalScore 
    if userInput == "r" and pcInput == "p":
        print('You lost!! PC wins')
    elif userInput == "r" and pcInput == "s":
        globalScore  += 1
        print('You won!! PC lost')
    elif userInput == "r" and pcInput == "r":
        print('It is a draw!!')
        
    elif userInput == "p" and pcInput == "r":
        globalScore  += 1
        print('You won!! PC lost')
    elif userInput == "p" and pcInput == "s":
        print('You lost!! PC wins')
    elif userInput == "p" and pcInput == "p":
        print('It is a draw!!')
        
    elif userInput == "s" and pcInput == "r":
        print('You lost!! PC wins')
    elif userInput == "s" and pcInput == "p":
        globalScore  += 1
        print('You won!! PC lost')
    elif userInput == "s" and pcInput == "s":
        print('It is a draw!!')
        
def p2Choice(p1, p2):
    if p1 == "r" and p2 == "p":
        print('Player 1 lost!! Player 2 wins')
    elif p1 == "r" and p2 == "s":
        print('Player 1 won!! Player 2 lost')
    elif p1 == "r" and p2 == "r":
        print('It is a draw!!')
        
    elif p1 == "p" and p2 == "r":
        print('Player 1 won!! Player 2 lost')
    elif p1 == "p" and p2 == "s":
        print('Player 1 lost!! Player 2 wins')
    elif p1 == "p" and p2 == "p":
        print('It is a draw!!')
        
    elif p1 == "s" and p2 == "r":
        print('Player 1 lost!! Player 2 wins')
    elif p1 == "s" and p2 == "p":
        print('Player 1 won!! Player 2 lost')
    elif p1 == "s" and p2 == "s":
        print('It is a draw!!')

def playPC():
    clear_screen()
    userInput = input('Select your type (rock(r)/papper(p)/scissor(s)): ')
    while verify_input(userInput) == False:
        print('Invalid choice, try again')
        userInput = input('Select your type (rock(r)/papper(p)/scissor(s)): ')
            
    pcInput = random.choice(types)
    print('=======================')
    print(f"You chose: {userInput}")
    print(f"PC chose: {pcInput}")
    rChoice(userInput, pcInput)
    print('=======================')
    
def playPlayer():
    clear_screen()
    print('Player 1')
    player1Input = input('Select your type (rock(r)/papper(p)/scissor(s)): ')
    while verify_input(player1Input) == False:
        print('Invalid choice, try again')
        player1Input = input('Select your type (rock(r)/papper(p)/scissor(s)): ')
        
    print('Player 2')
    player2Input = input('Select your type (rock(r)/papper(p)/scissor(s)): ')
    while verify_input(player2Input) == False:
        print('Invalid choice, try again')
        player2Input = input('Select your type (rock(r)/papper(p)/scissor(s)): ')

    print('=======================')
    print(f"Player 1 chose: {player1Input}")
    print(f"Player 2 chose: {player2Input}")
    p2Choice(player1Input, player2Input)
    print('=======================')

def main():
    clear_screen()
    print('Welcome to Rock, Paper, Scissors game')
    print('Select an option:')
    print('1) Play against PC')
    print('2) Play against Player')
    print('3) Check score')
    choice = input('Enter your choice: ')

    if choice == "1":
        playPC()
    elif choice == "2":
        playPlayer()
    elif choice == "3":
        checkScore()
    else:
        print('Invalid choice, try again')

while True:
    main()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
