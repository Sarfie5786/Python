# Never forget to insert datetime table
from datetime import datetime
# and never forget to give it a functional value
current_time = datetime.now()
print("Sarfie5786's Spreadsheet Automation Menu")

#making the list for the 'for' loop
options = ("1. Input Data", "2. View Current Data", "3. Generate Report")

print("Choose a number from the following options")

for option in options:
    print(option)
    
choice = input()

if choice == "1":
    print(f"You selected one at {current_time}.")
elif choice == "2":
    print(f"You selected 2 at {current_time}.")
elif choice == "3":
    print(f"You selected 3 at {current_time}.")
else:
    print("Error: Invalid choice selected.")
