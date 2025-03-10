def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

try:
    user_score = int(input("Enter your score: "))
    assign_grade(user_score)
except ValueError:
    print("Invalid input! Please enter a numerical score.")
