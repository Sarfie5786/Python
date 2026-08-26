import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
from openpyxl.chart import PieChart, BarChart, Reference
from openpyxl.chart.label import DataLabelList
import csv

path="C:\\Final Exam\\final.csv"
final="C:\\Final Exam\\final.xlsx"

name=[]
income=[]


def askUser():
    #setting value to the total
    noneShallPass=0
    #loop running for 5 cycles for 5 entries
    for blackKnight in range(5):
        #asking for the number for any of the entries
        blackKnight = int(input("Please enter a number: "))
        #adding that entry to the total
        noneShallPass = noneShallPass + blackKnight
    #after loop is run, display the total
    print(f"The sum for the 5 numbers entered is: {noneShallPass}")

def askIncome():
    with open(path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        #for data from row 5(0) through row 9(5), so 5 new names total
        for data in range(1,6):
            #asking for names to be entered
            name = input("Please enter a name: ")
            #asking for their income
            income = input("Please enter their income: ")
            #appends the new data into the .csv file and reruns until 5 new names are entered.
            writer.writerow([name, income])

csv_filename=path
excel_filename=final

df = pd.read_csv(csv_filename)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "final exam"
data = Reference(ws, min_col=2, min_row=1, max_row=len(df)+1)
labels = Reference(ws, min_col=1, min_row=2, max_row=len(df) + 1)
    
def excelPie(csv_filename, excel_filename):
    pie=PieChart()
    pie.title = "sarfie5786 August 26th, 2026"
    pie.add_data(data, titles_from_data=True)
    pie.set_categories(labels)
    ws.add_chart(pie, "A10")

def verticalBar():
    bar=BarChart()
    bar.type = 'col'
    bar.style = 10
    bar.color='g'
    bar.title = "sarfie5786 Augst 26th, 2026"
    bar.x_axis.title = "Name"
    bar.y_axis.title = "Income"
    bar.add_data(data, titles_from_data=True)
    bar.set_categories(labels)
    bar.dataLabels = DataLabelList()
    bar.dataLabels.showVal = True
    bar.legend=None
    bar.width = 15
    bar.height=10
    ws.add_chart(bar, "D1")

askUser()
askIncome()

ws.append(["Name", "Income"])
for row in df.itertuples(index=False):
    ws.append(list(row))

for cell in ws['B'][1:]:
    cell.number_format = '0'

excelPie(csv_filename, excel_filename)
verticalBar()
wb.save(excel_filename)
