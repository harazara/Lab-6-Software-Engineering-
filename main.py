# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

# hey
def encode(password):
    for num in password:
        #turn password into int and add 3 then turn back into string
        num = str(int(num) + 3)
        password += num
    print(password)

def main():
    while True:
        print_menu()
        option1 = int(input("Please enter an option:"))
        if option1 == 1:
            encode1 = input("Please enter your password to encode:")
            encode(encode1)
    #print menu using while loop
    #ask for menu input
    #ask for password

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
