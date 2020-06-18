# importing libraries
import os
from random import choice

# to clear screen every time this program rounds
os.system('cls')

# pre defining the list of option and their superiority
rps = ('Rock', 'Paper', 'Scissors')
rps_dict = {
    'Rock' : {'Superior': 'Scissors', 'Inferior': 'Paper'},
    'Paper' : {'Superior': 'Rock', 'Inferior': 'Scissors'},
    'Scissors' : {'Superior' :'Paper', 'Inferior': 'Rock'}
}

# Defining the first function which displays the Result
def display_result(user_point, sys_point, wins, lost, draw) :
    print('Result: ', end=' ')

    if user_point > sys_point :
        print('You WIN!!')
    elif user_point < sys_point :
        print('You LOSE ..')
    else :
        print('It\'s a DRAW !!')

    print('---------------')
    # print the scores here
    print(f'Your score : {user_point}')
    print(f'Computer\'s score: {sys_point}')
    print('---------------')

    # print stats
    print(f'Wins: {wins}')
    print(f'Lost: {lost}')
    print(f'Tie: {draw}')

#defining fuction that iterates and adds scores
def score(rounds) :
    #defining a dictionary of arguments
    game_result = {
        'user_point': 0,
        'sys_point': 0,
        'wins': 0,
        'lost': 0,
        'draw': 0
    }
    while rounds > 0 :
        user_input = input('Enter your choice (1. Rock, 2. Paper, 3. Scissors, 0. Quit this program: ')

        #check whether the input available
        #if the input is within range of rps
        if user_input in ('1', '2', '3'):
            rounds = rounds - 1
            user_choice = rps[len(user_input) - 1]
            sys_choice = choice(rps)

            #when user's choice is superior
            if rps_dict[user_choice]['Superior'] == sys_choice :
                game_result['user_point'] += 1
                game_result['wins'] += 1
                result = 'You win..'

            #when computer,s choice is superior
            elif rps_dict[user_choice]['Inferior'] == sys_choice :
                game_result['sys_point'] += 1
                game_result['lost'] += 1
                result = 'You lose..'

            #when users choice and computer's choice is same
            else :
                game_result['draw'] += 1
                result = 'It\'s a Tie..'

            #printing result of each rounds
            print(f'Your score : {user_choice}. Computer : {sys_choice}. ||{result}||')

        #when you wish to quit the code
        elif user_input == '0' :
            break
            print("Thank You and Visit Again!!")

        #when the input is Invalid
        else :
            print('Invalid Input!!')
        print() #to leave a line

    #calling the first function and game_result keys as arguments
    display_result(**game_result)

if __name__ == '__main__':
    print("Welcome to the Rock-Paper-Scissors Game!!")

    #asking for the no of rounds to be played and checking if it is valid number
    try :
        rounds = int(input('How many rounds do you want to play? '))
        score(rounds)
    except ValueError :
        print('Please input a valid number!')
