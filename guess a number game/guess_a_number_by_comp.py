# Guess a number game
import random

start = 1
end = 100

print('Make a number game')
user = None

while user != "=":
    number = random.randint(start, end)
    print(number)
    user = input("= is for win, > is our number bigger, < is for our number smaller: ")
    # Если компьютер угадал число, игрок выбирает “победа”.
    if user == "=":
        print("computer wins")
        break
    # Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
    elif user == ">":
        start = number + 1
        print(number)
    # Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
    elif user == "<":
        end = number - 1
        print(number)
# Игра продолжается до тех пор пока компьютер не отгадает число.