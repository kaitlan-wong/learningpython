
# This is a python program to check if the input number is odd or even.


def check_odd_even():
    while True:
        try:
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                print("The number is even, nice!")
            else:
                print("Oh wow the number is odd!!")
            break  # exit loop if input is valid (a number)
        except ValueError:
            print("Whoops, that's not a whole number! Please enter an integer.")

check_odd_even()