def userInputs():
  inputUse1 = input("enter num ")
  while not inputUse1.isdigit():
    inputUse1 = input("enter num ")
  userIn = inputUse1
  return userIn

def fizzBuzz(userIn):
  num = int(userIn)
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"


num = userInputs()
print(fizzBuzz(num))