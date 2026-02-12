import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'


def assess_game(user_action, computer_action):

    if user_action == computer_action:
        print(f"The user and the computer picked {user_action}. Draw game!")

    elif user_action == ROCK:
        if computer_action == PAPER:
            print(f"{computer_action} covers {user_action}. Computer wins!")
        else:
            print(f"{user_action} smash {computer_action}. User wins!")


    elif user_action == PAPER:
        if computer_action == SCISSORS:
            print(f"{computer_action} cuts {user_action}. Computer wins!")
        else:
            print(f"{user_action} covers {computer_action}. User wins!")


    elif user_action == SCISSORS:
        if computer_action == ROCK:
            print(f"{computer_action} smash {user_action}. Computer wins!")
        else:
            print(f"{user_action} cuts {computer_action}. User wins!")


def main():
    game_actions = (ROCK, PAPER, SCISSORS)

    partida = True
    while partida == True:
        user_action = input(f"Pick a choice: rock, paper or scissors: ")
        computer_action = random.choice(game_actions)

        print(f"You picked {user_action}. The computer picked {computer_action}")
        assess_game(user_action, computer_action)

if __name__ == "__main__":
    main()