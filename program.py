# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32
# I watced the extra video

def fizzbuzz(i:int):
  if i % 15 == 0:
      return "FizzBuzz"
  if i % 3 == 0:
      return "Fizz"
  if i % 5 == 0:
      return "Buzz"
    return i

result = ""
for myNumber in range(2, 33):
  result = str(result) + str(fizzbuzz(myNumber)) + "\n"

print(result)
