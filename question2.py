import re

def sum_of_digits():
    numbers = input("Enter series of single digit numbers")
    return sum([int(num) for num in str(numbers) if  not re.match(r"\W", num)])

print(sum_of_digits())
  