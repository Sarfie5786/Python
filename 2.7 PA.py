#Sara Fields, 8/5/2026, 2.7 Performance Assessment - Decisions, Loops, Processing, Output Formatting
name = input("What is your name? ")
studentID = input("What is your Student Id? ")
color = input("What is your favorite color? ")
print("Ah. Alright then. On you go.")
print(f"Welcome to my performance assessment, {name}.\n")
#now to the actual assessment
number = 6
counter = 0
guess = 0
while guess != number:
    guess = int(input("Please guess a number between 1 and 10..."))
    counter = counter + 1
    if number > guess:
        print("You guessed too low.")
        
    elif number < guess:
        print("You guess too high.")
        
print(f"Congratulations, {name}! You guess the number in {counter} tries!\n")
#setting up the while loop for increments
cycle = 0
inc = 0
print("Outcome from the 'while' loop:")
while cycle != 5:
    cycle = cycle + 1
    inc = number + cycle
    print(f"{number} incremented by {cycle} is {inc}")
#a space for good measure
print(" ")
#setting up the for loop for increments
cycle = 0
inc = 0
for num in range(1, 6):
    cycle = cycle+1
    inc = number+cycle
    print(f"{number} incremented by {cycle} is {inc}")
