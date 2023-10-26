from random import randint

#  user has to enter 6 numbers. Program include 4 validations:
#  user can't use other value than number
#  user can't use number bigger than 49 and smaller than 1
#  user can't use number which used previous
print('Please enter 6 number from 1 to 49')
user_numbers = []
while len(user_numbers) < 6:
    try:
        number = int(input('Enter numer: '))
    except ValueError:
        print("Entered other value like number")
        continue
    if number > 49:
        print('Entered bigger value than 49')
        continue
    elif number < 1:
        print('Entered smaller value than 1')
        continue
    elif number in user_numbers:
        print('The number has already entered')
        continue
    else:
        user_numbers.append(number)

user_numbers.sort()
print(f"Your numbers: {user_numbers}")

#  computer choose 6 numbers with range 1 to 49
computer_numbers = []
while len(computer_numbers) < 6:
    com_number = randint(1, 49)
    if com_number in computer_numbers:
        continue
    else:
        computer_numbers.append(com_number)

computer_numbers.sort()
print(f"Computer number: {computer_numbers}")

#  program compare user numbers and computer numbers and show how many numbers is same
wins = 0
for number in user_numbers:
    if number in computer_numbers:
        wins += 1
print(f"You choose {wins} number/s", end='')
if wins >= 3 and wins <= 6:
    print(" and you win money")
else:
    print(" and you don't win anything")
