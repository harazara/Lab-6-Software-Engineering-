# Zara Haruna


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

# hey
def encode(password):
    new_pass = ""
    for num in password:
        #turn password into int and add 3 then turn back into string
        num = str(int(num) + 3)
        new_pass += num
    return(new_pass)

def main():
    while True:
        print_menu()
        option1 = int(input("Please enter an option:"))
        if option1 == 1:
            encode1 = input("Please enter your password to encode:")
            print(encode(encode1))
    #print menu using while loop
    #ask for menu input
    #ask for password

if __name__ == '__main__':
    main()


