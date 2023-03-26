import random

choose = ["rock" , "paper" , "scissors"]

player1_score = 0
player2_score = 0


sets = int(input("How many sets do you want to play?"))
round_counter = 0

while round_counter < sets:


  player1 = random.choice(choose)
  player2 = random.choice(choose)


  print("( " , player1, " , " , player2 , " )")


  if player1 == player2:
      print("Tie! Both players chose the same action")


  elif player1 == "paper" and player2 == "rock":
      print("Player 1 is the winner")
      player1_score += 1
  elif player1 == "paper" and player2 == "scissors":
    print("Player 2 is the winner")
    player2_score += 1
  elif player1 == "scissors" and player2 == "rock":
    print("Player 2 is the winner")
    player2_score += 1
  elif player1 == "scissors" and player2 == "paper":
    print("Player 1 is the winner")
    player1_score += 1
  elif player1 == "rock" and player2 == "paper":
    print("Player 2 is the winner")
    player2_score += 1
  elif player1 == "rock" and player2 == "scissors":
    print("Player 1 is the winner")
    player1_score += 1
  else:
    print("Someting went wrong")


  print("Score is : ")
  print("Player 1 : ", player1_score)
  print("Player 2 : ", player2_score)
  round_counter+=1

if player1_score > player2_score:
  print("Winner is Player 1")
elif player2_score > player1_score:
  print("Winner is Player 2")
else:
  print("Draw")