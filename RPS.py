#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  playAgain = "Y"
  while playAgain == "Y":

    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice(["R", "P", "S"])
  
    #Prompt the user for their RPS selection
    player = input ("Pick your weapon (R, P, S):")
  
   #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer Chose R")
    elif computer == "P":
      print("Computer chose Paper")
    elif computer == "S":
      print ("Computer chose Scissors")

    if player == "R":
      print("Player chose Rock")
    elif player == "P": 
      print ("Player chose Paper")
    elif player == "S":
      print ("Player chose Scissors")
    else:
      print ("Player input invalid Entry, please try again.")

  #Winner Loser or Tie?

    if player == "R" and computer == "P": 
      print ("You Lose.")
      losses = losses + 1
    elif player == "R" and computer == "S":
      print ("You Win!")
      wins = wins + 1

    if player == "P" and computer == "R": 
      print ("You Win!")
      wins = wins + 1
    elif player == "P" and computer == "S":
      print ("You lose.")
      losses = losses + 1

    if player == "S" and computer == "R":
      print ("You lose.")
      losses = losses + 1
    if player == "S" and computer == "P":
      print ("You Win!")
      wins = wins + 1

    if player == computer:
      print ("It's a tie.")
      ties = ties + 1

    #Ask the user if they would like to play again.
    playAgain = input ("Would you like to play again? (Y/N): ")


  while playAgain == "N":
    #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)
    playAgain = "done"
    

if __name__ == '__main__':
  main()
