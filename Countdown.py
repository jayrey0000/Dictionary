def countdown():
    answer = input("Do you want to print a countdown? (yes/no): ").strip().lower()
    
    if answer == "yes":
        for i in range(10, 0, -1):
            print(i)
        print("Countdown complete!")
    else:
        print("Maybe next time!")

countdown()