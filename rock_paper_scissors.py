import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "You win, rock smashes scissors"
    else:
      return "Paper covers rock. You lose."

  elif player == "paper":
    if computer == "scissors":
      return "You lose, scissorsn cuts paper"
    else:
      return "Paper covers rock. You win."

  elif player == "scissors":
    if computer == "paper":
      return "You win, scissorsn cuts paper"
    else:
      return "You lose, rock smashes scissors"

choices = get_choices
# result = check_win(choices["player"], choices["computer"])
# print(result)
print(choices['player'])
