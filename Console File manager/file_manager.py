import sys
from functions import change_dir, save_info, copy_file, delete_file, get_list, create_folder, create_file

save_info("start")

try:
    command = sys.argv[1]
except IndexError:
    print('Enter a command, use "help" to get command list')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Enter a file name')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Enter a file name')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Enter a file name')
        else:
            delete_file(name)
    elif command == 'cd':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Enter a directory name')
        else:
            change_dir(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Enter a file name and new file name')
        else:
            copy_file(name, new_name)
    elif command == "help":
        all = {
            'list': '- to get list of files and folders at current directory',
            'create_file': '- to create new file',
            'create_folder': '- to create new folder',
            'delete': '- to delete file or folder',
            'cd': '- to change directory',
            'copy': '- to copy file with new file name'
        }

        print('Commands to use:\n')
        for key, value in all.items():
            print(key, value)

    save_info('end')
