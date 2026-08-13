# Never forget to insert datetime table
from datetime import datetime
# and never forget to give it a functional value
current_time = datetime.now()
print("Sarfie5786's Spreadsheet Automation Menu")

#making the list for the 'for' loop
options = ("1. Input Data", "2. View Current Data", "3. Generate Report")

print("Choose a number from the following options")

def convertData(lbs):
    Kg = float(lbs / 2.205)
    return Kg

def getInput():
    entryNum = int(input("How many entries are you inputting: "))
    for biggusdickus in range(entryNum):
        date = input("Please enter a date: \n")
        lbs = int(input("Enter the weight in pounds for the inputted data:\n"))
        
        #using converData() to turn the argument(lbs) to the return(Kg)
        Kg = convertData(lbs)
        print(f"The following was saved at {current_time}, {lbs}, {Kg:.2f}.")
        
for option in options:
    print(option)
    
choice = input()

if choice == "1":
    print(f"You selected one at {current_time}.")
    getInput()
#can delete the comment notation later as the error message was already made.
#elif choice == "2":
    #print(f"You selected 2 at {current_time}.")
#elif choice == "3":
    #print(f"You selected 3 at {current_time}.")
else:
    print("Error: The chosen functionality is not implemented yet.")
