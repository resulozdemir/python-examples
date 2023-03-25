import time
import random

numbers = [1,2,3,4,5,6,7,8,9,0]
for i in numbers:
  print(i)

for i in range(5,21):
  print(i)

for i in range(1,101):
  if i % 5 == 0:
    print(i)


celsius = 30

while celsius < 50:
  if celsius > 30:
    print("haot")
  elif 30 >= celsius > 20:
    print("good")
  elif -273 < celsius <= 20:
    print("cold")
  else:
    print("someting went wrong")

  print("The current temperature is ", celsius)
  celsius += 5
  time.sleep(1)

while True:
  random_number = random.randrange(1000)
  print(random_number)

  if random_number == 777:
    print("found!")
    break
