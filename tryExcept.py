def divide(number1, number2):
   try:
       number1_int = int(number1)
       number2_int = int(number2)
       return number1_int / number2_int
   except ValueError:          #ya bu sekilde ikili yazabilirsin yada tek bir tane except yazıp hata turunu belirtmesin sana kalmıs
       print("Only integers are allowed! Try again.")

   except ZeroDivisionError:
       print("You cannot divide any number by zero!")

number1 = input("Please provide number1 : ")
number2 = input("Please provide number2 : ")

print(divide(number1,number2))