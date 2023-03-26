def hello(name):
    print("Hello ",name)

def sum(number1, number2):
  answer = number1 + number2
  return answer


result = sum(3,8)
print(result)

def greetings1(name):
    print(f'Hello, {name}')
    print('Hello ' + name)
    print('Hello ', name)

greetings1('resul')


def greetings2(first_name, last_name, auto_correction = True):
  if auto_correction:
    capitalized_first_name = first_name.capitalize()
    capitalized_last_name = last_name.capitalize()
    print("Hello,", capitalized_first_name, capitalized_last_name)
  else:
    print("Hello,", first_name, last_name)

greetings2("reSul","oZdeMir")

def greetings3(first_name, last_name, auto_correction):
  if auto_correction:
    capitalized_first_name = first_name.capitalize()
    capitalized_last_name = last_name.capitalize()
    print("Hello,", capitalized_first_name, capitalized_last_name)
  else:
    print("Hello,", first_name, last_name)

greetings3("reSul","oZdeMir",True)

greetings3( last_name = "ozDemir", auto_correction = False, first_name = "resUl" )


number = 19 # global degisken

def change_number():
  global number
  number = 2  # eger usteki tanımlamayı yapmasaydık local degiskendi

change_number()
print(number)


def fahrenheit_celcius(temperature, mode):
  assert mode == "f2c" or mode == "c2f", "Invalid argument!"
  if mode == "f2c":
    result = (temperature - 32) * 5 / 9
    return result
  else:
    result = (temperature * 9 / 5) + 32
    return result


def pound_kilogram(quantity, mode):
    assert mode == "pound2kg" or mode == "kg2pound", "Invalid argument!"

    if mode == "pound2kg":
        weight = quantity * 0.45359
        return weight

    else:
        weight = quantity / 0.45359
        return weight


def mile2km(miles):
  distance = miles * 1.60934
  return distance

def km2mile(km):
  distance = km / 1.60934
  return distance

