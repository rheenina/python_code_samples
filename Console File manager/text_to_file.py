# Скрипт записи текста в файл построчно. Последняя пустая строка говорит о завершение записи.


def create_file(name=input('Name a file to create: ')):
    with open(name, 'a', encoding='UTF-8'):
        return name


def create_text():
    file_name = create_file()

    with open(file_name, 'a', encoding='UTF-8') as f:

        while True:
            text = input('Enter some text to write down: ')

            if not text:
                break

            f.write(text + '\n')


if __name__ == '__main__':
    try:
        create_text()
    except FileNotFoundError:
        print('File was not named.')
