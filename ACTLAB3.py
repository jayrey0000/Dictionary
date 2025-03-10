def check_number(num):
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")

try:
    user_input = int(input("Enter a number: "))
    check_number(user_input)
except ValueError:
    print("Invalid input! Please enter an integer.")
