# Скрипт для подсчета строк в файле и количества слов для каждой строки.


def counting(file_name):

    with open(file_name, 'r') as file:
        string = 0

        # counting strings and words for each string
        for line in file:
            string += 1
            words = line.split()
            word = len(words)
            print(string, word)


if __name__ == '__main__':
    some_file = 'test.txt'
    counting(some_file)