try:
    # Get input from the user and convert it to an integer
    num = int(input("Enter a number: "))

    # Check if the remainder when divided by 2 is 0
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
except ValueError:
    print("Please enter a vali.")