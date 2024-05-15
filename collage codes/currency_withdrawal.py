# List of denominations sorted from highest to lowest
denominations = [500, 200, 100, 50, 10]

try:
    # Input the amount to withdraw
    amount = int(input("Enter the amount to withdraw: "))
    
    if amount <= 0:
        print("Please enter a positive amount.")
    else:
        notes_count = {}

        # Calculate the number of notes for each denomination
        for denom in denominations:
            # print(f"Denomination: {denom}")
            # print(f"Amount: {amount//denom}")
            notes_count[denom] = amount // denom
            amount = amount % denom

        # Print the number of notes for each denomination
        print("Currency notes to be given:")
        for denom in denominations:
            if notes_count[denom] > 0:
                print(f"{denom} : {notes_count[denom]}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
