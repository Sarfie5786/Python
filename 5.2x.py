#importing the graph function and randomization function
import matplotlib.pyplot as plt
import numpy as np
import random

#creating the function to run in the loop to form the graph
def update_graph(reading_numbers, temperatures):
    plt.clf()
    
    plt.plot(reading_numbers, temperatures, marker="o")
    
    plt.xlabel("Reading")
    plt.ylabel("Temperature")
    plt.title("5.2x Code Challenge")
    plt.xticks(np.arange(1,21,1))
    plt.grid()
    
#creating the lists to hold the data
reading_numbers=[]
temperatures=[]
#turning on interactive graphing
plt.ion()
#the for loop to create the data
for reading in range(1,21):
    temperature=random.randint(60,90)
    reading_numbers.append(reading)
    temperatures.append(temperature)

    print(f"The {reading}'s temperature is {temperature} degrees.")
    
    update_graph(reading_numbers, temperatures)
    #pausing the program to give it time to reset before the next loop
    plt.pause(0.5)

#turning off interactive graphing
plt.ioff()
#show me the prize!
plt.show()
