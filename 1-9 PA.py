name = input("What is your name?\n")
sID = input("What is your Student ID?\n")
unladenSwallow = input("What is the airspeed velocity of an unladen swallow?\n")

#getting our variables
var1 = int(input("Please enter a first whole number: "))
var2 = int(input("Please enter a second whole number: "))

math1 = var1 * var2
math2 = var1 - var2
math3 = float(var1 / var2)

print(f"The result of {var1} times {var2} is: {math1}")
print(f"The result of {var1} minus {var2} is: {math2}")
print(f"The result of {var1} divided by {var2} is: {math3:.2f}")

if var1 > var2:
    print("The first number is larger than the second number.")
elif var1 <var2:
    print("The first number is less than the second number.")

print(f"{name}")
print(f"{sID}")
print("I- I don't know that!")
