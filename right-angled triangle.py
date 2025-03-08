# Ask the user if they want to print the triangle
user_input = input("Do you want to print a right-angled triangle? (yes/no): ").strip().lower()

# If the user enters "yes", print the triangle using a for loop
if user_input == "yes":
    for i in range(1, 11):  # Loop from 1 to 10 (height of the triangle)
        print("*" * i)  # Print '*' repeated i times
else:
    print("Triangle not printed. Exiting the program.")