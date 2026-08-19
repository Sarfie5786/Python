#importing the library that let's us call csv files
import csv
#importing the library that let's us put information into a bar graph
import matplotlib.pyplot as plot
#printing my StudentID
print("sarfie5786")
#setting the path to know what file to pull
path="C:\\PythonFiles\\4.6file.csv"

with open(path, newline='') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
f.close
#setting x and y axis for later
x=[]
y=[]
#resetting the file pulled
path="C:\\PythonFiles\\4.6file.csv"
#setting coordinates of what to pull and where to put it
with open(path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
#making settings for the bar graph
plot.bar(x,y, color = "g", width = 0.5, label = "States I've Visited")
plot.xlabel("States")
plot.ylabel("Times Visited")
plot.title("States I've Visited")
plot.legend()
plot.show()
