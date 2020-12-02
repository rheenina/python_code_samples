#guess a number game
import random

number = random.randint(1, 100)
#print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input("Choose a level: "))
max_count = levels[level]

user_count = int(input("Enter a number of users: "))
users = []
for i in range(user_count):
    user_name = input(f"Enter name of {i} user: ")
    users.append(user_name)

print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print("You all loose")
        break
    print(f'Try № {count}')
    for user in users:
        print(f'Turn of {user}')
        user_number = int(input('Enter a number: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print("Your number is bigger than made one")
        else:
            print("Your number is smaller than made one")
else:
    print(f"{winner_name} wins")
