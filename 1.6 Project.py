# Never forget to insert datetime table
from datetime import datetime
# and never forget to give it a functional value
current_time = datetime.now()
print("Sarfie5786's Spreadsheet Automation Menu")
"""no loop yet according to expected output. will opt
for a match-type if it will eventually be that"""
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")
#giving a space to insert choice
choice = input("")

match choice:
    case "1":
        print(f"You selected 1 at {current_time}.")
    case "2":
        print(f"You selected 2 at {current_time}.")
    case "3":
        print(f"You selected 3 at {current_time}")
    # unrequested, but still important to include
    case _:
        print("Invalid Option.")
            
