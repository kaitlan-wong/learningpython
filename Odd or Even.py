
# This is a python program to check if the input number is odd or even,
# and whether or not the preceding numbers are odd or even.


def check_odd_even(n: int):
    for i in range(1, n+1):
        print(f"{i} is {('even' if i % 2 == 0 else 'odd')}")

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a number: "))
            check_odd_even(num)
            break
        except ValueError:
            print("Whoops, that's not a whole number! Please enter an integer.")