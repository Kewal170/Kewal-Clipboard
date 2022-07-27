import sys

import clipboard

filename = 'clipboard.txt'


def save_text(text):
    with open(filename, 'a') as f:
        f.write(text + "\n")
    print("-" * 50)
    print("Data updated!")


def load_text():
    with open(filename, 'r') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1
            print("{}: {}".format(count, line.strip()))


def save_items():
    user_text = input("Enter your text :")
    save_text(user_text)


def copy_items():
    print("-" * 50)
    load_text()
    print("-" * 50)
    try:
        user_copy_input_number = int(input("Enter the line number to copy that text > "))
        with open(filename, 'r') as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                count += 1
                if user_copy_input_number == count:
                    clipboard.copy(line)
                    print()
                    print("data copied!")
    finally:
        print("Please index number!")


def reset_items():
    print("-" * 50)
    with open(filename, 'w') as f:
        f.write('')
    print("-" * 50)
    print("File Reset done!")


def list_items():
    try:
        print("-" * 50)
        load_text()
        print("-" * 50)
    except:
        print(f"[-] Currently, no data found in {filename}")
        print("[*] To add data type :: python kewal_clipboard.py save")
        print("[*] For more info :: python kewal_clipboard.py help")


def k_help():
    print("-" * 50)
    print('''
=== save - To add data
=== list - To list data
=== load - To copy data
''')
    print("-" * 50)


try:
    if len(sys.argv) == 2:
        command = sys.argv[1]
        if command == 'save':
            print("-" * 50)
            key = input("Enter your text :")
            save_text(key)
        elif command == 'help':
            k_help()
        elif command == "copy":
            copy_items()
        elif command == 'list':
            list_items()
        elif command == 'reset':
            reset_items()
        else:
            print(f"{command} - unknown command")
            k_help()
except:
    k_help()
