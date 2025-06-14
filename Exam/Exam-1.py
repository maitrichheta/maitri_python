while True:

    print("Welcome to the Bill Splitter App!")
    print()
    
    bill = float(input("Enter the total bill amount:₹ "))
    people = int(input("Enter Number of people: "))
    tip_percent = int(input("Enter tip percentage (0/5/10/15/20): "))

    if bill < 0 or people <= 0 or tip_percent not in [0, 5, 10, 15, 20]:
        print("Invalid input! Please try again.")
        continue

    tip = (tip_percent / 100) * bill
    final_bill = bill + tip
    per_person = final_bill / people

    print(f"\nTip Amount: ₹{tip:.2f}")
    print(f"Totl Bill (with tip): ₹{final_bill:.2f}")
    print(f"Each person should pay: ₹{per_person:.2f}")

    again = input("\nwould you like to calculate anothrr bill? (y/n): ").lower()
    if again != 'y':
        print("Thank you for using the Bill Splitter App!")
        break
