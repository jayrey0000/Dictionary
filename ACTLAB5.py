def classify_age(age):
    if age < 0:
        print("Invalid age! Please enter a non-negative number.")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    else:
        print("You are a Senior.")

try:
    user_age = int(input("Enter your age: "))
    classify_age(user_age)
except ValueError:
    print("Invalid input! Please enter a numerical age.")
