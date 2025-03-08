def login():
    print("Welcome! Please log in to use the program.")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":  # Sample credentials
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Access denied.\n")
        return False

def hello_po():
    print("\nHello po sa taong nagbabasa nitong code ko!\n")

def nested_loops():
    a1 = int(input("Enter value for a1: "))
    a2 = int(input("Enter value for a2: "))
    a3 = int(input("Enter value for a3: "))
    a4 = int(input("Enter value for a4: "))
    a5 = int(input("Enter value for a5: "))
    a6 = int(input("Enter value for a6: "))
    a7 = int(input("Enter value for a7: "))
    a8 = int(input("Enter value for a8: "))

    for a in range(a1):
        for b in range(a2):
            for c in range(a3):
                for d in range(a4):
                    for e in range(a5):
                        for f in range(a6):
                            for g in range(a7):
                                for h in range(a8):
                                    print(f"a-{a}, b-{b}, c-{c}, d-{d}, e-{e}, f-{f}, g-{g}, h-{h}")

def main():
    if login():
        while True:
            hello_po()
            nested_loops()
            
            choice = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
            if choice != "yes":
                print("Exiting program. Thank you!")
                break

main()
