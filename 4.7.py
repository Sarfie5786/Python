import pandas as pd
import matplotlib.pyplot as plt
#Forming data for multi-index formating
data={
    "Subject":["Math"] * 10 + ["Science"] * 10,
    "Grade":[85, 95, 76, 95, 100, 98, 73, 89, 91, 100, 68, 93, 100, 93, 95, 85, 82, 94, 95, 90]
    }

df = pd.DataFrame(data)
#finding the average grades for Math and Science
avg_df = df.groupby("Subject").mean()
#printing StudentID and assignment for the average
print("sarfie5786")
print(avg_df)

#making the bar graph
plt.figure()
plt.bar(avg_df.index, avg_df["Grade"], width=0.5)
plt.xlabel("Average Grade by Subject")
plt.show()
