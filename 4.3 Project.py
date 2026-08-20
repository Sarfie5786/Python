# Never forget to insert datetime table
from datetime import datetime
# and never forget to give it a functional value
current_time = datetime.now()
print("Sarfie5786's Spreadsheet Automation Menu")

file="C:\\Users\\student\\Documents\\Week 4\\ZooData.csv"
#making the list for the 'for' loop
options = ("1. Input Data", "2. View Current Data", "3. Generate Report")

print("Choose a number from the following options")
#adding data to the .csv file
def insertData(file, data):
    try:
        with open(file,"a+") as fopen:
            fopen.write(data + '\n')
    except:
        print("Error writing to this file.")
#allowing us to view data added to the file
def viewData(file):
    try:
        with open(file,"r") as fopen:
            print(f"Data from: {file}")
            
            for line in fopen:
                print(line.strip())

    except:
        print("Error reading this file.")
#converting pounds into kilograms
def convertData(lbs):
    kg = float(lbs / 2.205)
    return kg
#recording the date, the pounds we input, the kilograms it converts to, and adds that data to the file.
def getInput():
    entryNum = int(input("How many entries are you inputting: "))
    
    for biggusdickus in range(entryNum):
        date = input("Please enter a date: \n")
        lbs = int(input("Enter the weight in pounds for the inputted data:\n"))
        
        #using converData() to turn the argument(lbs) to the return(Kg)
        kg = convertData(lbs)
        print(f"The following was saved at {current_time}, {lbs}, {kg:.2f}.")

        data = f"{date}, {lbs}, {kg:.2f}"
        insertData(file, data)
        
for option in options:
    print(option)
    
choice = input()

if choice == "1":
    print(f"You selected one at {current_time}.")
    getInput()
#can delete the comment notation later as the error message was already made.
elif choice == "2":
    print(f"You selected 2 at {current_time}.")
    viewData(file)
#elif choice == "3":
    #print(f"You selected 3 at {current_time}.")
else:
    print("Error: The chosen functionality is not implemented yet.")
