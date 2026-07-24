while True:
    try:
        number = int(input("Enter a valid integer: "))
        print("You enetered: ", number)
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")
        
