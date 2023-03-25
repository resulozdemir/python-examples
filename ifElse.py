favNumber = 5
if favNumber < 15:
  print("My favorite number is smaller than 15")

print(type(favNumber))

celcius = 32

if celcius > 30:
  print("hot")
elif 30 >= celcius > 20:
  print("good")
elif -273 < celcius <= 20:
  print("cold")
else:
  print("Someting went wrong")

driver_license = True
age = 19

if age > 18:
  if driver_license:
    print("you can drive")
  else:
    print("you cant drive")
else:
  print("you shouldnt drive")


player1 = "deneme"
player2 = "deneme"

if player1 == player2:
  print("Tie! Both players chose the same action")
