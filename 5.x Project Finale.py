import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
from openpyxl.chart import LineChart, BarChart, Reference
import csv

# Never forget to insert datetime table
from datetime import datetime
# and never forget to give it a functional value
current_time = datetime.now()
print("Sarfie5786's Spreadsheet Automation Menu")

file="C:\\Users\\student\\Documents\\Week 4\\ZooData.csv"
final="C:\\Users\\student\\Documents\\Week 5\\final.xlsx"

df = pd.read_csv(file)

#making the list for the 'for' loop
options = ("1. Input Data", "2. View Current Data", "3. Generate Report")

print("Choose a number from the following options")
#adding data to the .csv file
def insertData(file, info):
    try:
        with open(file,"a+") as fopen:
            fopen.write(info + '\n')
    except:
        print("Error writing to this file.")
#allowing us to view info added to the file
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

        info = f"{date}, {lbs}, {kg:.2f}"
        insertData(file, info)
'''creating the chart in the excel file using file(the .csv file), and chartType
given by generateReport'''        
def createChart(file, chart, final):
    choice=input("Would you like the original data in pounds(1), or the converted data(2) in kilograms? ")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Final Project"
    ws.append(["Date", "Weight"])

    with open(file, "r") as fopen:
        reader = csv.reader(fopen)

        for row in reader:
            date_val = row[0]

            if choice == "1":
                weight_val = (float(row[1]))
            elif choice == "2":
                weight_val = (float(row[2]))

            ws.append([date_val, weight_val])
        max_r = ws.max_row
        data = Reference(ws, min_col=2, min_row=1, max_row=max_r)
        labels = Reference(ws, min_col=1, min_row=1, max_row=max_r)
        
        chart.title = "sarfie5786 August 27th, 2026"
        chart.x_axis_title = "Date"
        chart.y_axis_title = "Weight"
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(labels)
        chart.legend=None
        chart.width = 15
        chart.height = 10
        for series in chart.series:
            series.smooth=False
        ws.add_chart(chart, "D1")
        wb.save(final)
#function to ask user what kind of chart they'd like to make using the .csv file.        
def generateReport(file):
    chartType = input("Choose a line or bar chart: ")
    if chartType == "line":
        chart = LineChart()
    elif chartType == "bar":
        chart = BarChart()
    createChart(file, chart, final)
    
    
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
elif choice == "3":
    print(f"You selected 3 at {current_time}.")
    generateReport(file)
else:
    print("Error: The chosen functionality is not implemented yet.")
