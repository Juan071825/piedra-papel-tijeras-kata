import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2



class RPS:

    def __init__(self):

        self.game_result = GameResult
        self.victories = {
            GameAction.Rock: GameAction.Paper, 
            GameAction.Paper: GameAction.Scissors, 
            GameAction.Scissors: GameAction.Rock 
        }
        


    def assess_game(self, user_action, computer_action):

        game_result = None

        if user_action == computer_action:
            print(f"User and computer picked {user_action.name}. Draw game!")
            game_result = GameResult.Tie

        # You picked Rock

        elif computer_action == self.victories[user_action]:
            print(f"Computer picked {computer_action.name} and user picked {user_action.name}. Computer wins!")
            game_result = GameResult.Defeat


        else:
            print(f"Computer picked {computer_action.name} and user picked {user_action.name}. User wins!")
            game_result = GameResult.Victory
    

        return game_result


    def get_computer_action(self):
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")

        return computer_action


    def get_user_action(self):
        # Scalable to more options (beyond rock, paper and scissors...)
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
        user_action = GameAction(user_selection)

        return user_action


    def play_another_round(self):
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'


    def main(self):

        while True:
            try:
                user_action = self.get_user_action()
            except ValueError:
                range_str = f"[0, {len(GameAction) - 1}]"
                print(f"Invalid selection. Pick a choice in range {range_str}!")
                continue

            computer_action = self.get_computer_action()
            self.assess_game(user_action, computer_action)

            if not self.play_another_round():
                break


if __name__ == "__main__":

    game = RPS()
    game.main()
