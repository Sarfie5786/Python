"""sarfie5786
3-6 performance assessment
8/12/2026"""

def functionOne():
    print("My StudentID is sarfie5786.")

def functionTwo():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a second number: "))
    num3 = num1 + num2
    print(f"The sum of {num1} and {num2} is {num3}.")
    return num3

def functionThree(biggusdickus):
    if biggusdickus > 5:
        print("The sum is greater than 5.")
    elif biggusdickus < 5:
        print("The sum is less than 5.")
    else:
        print("5 is right out.")

    sIDNum = 5786
    
    return sIDNum

#define what the main() function does
def main():
    #running functionOne to display studentID
    functionOne()
    #running functionTwo to get my num3 sum
    incontinentiaButtocks = functionTwo()
    #running functionThree using num3 sum to determine if it's less than or greater than 5
    lifeOfBrian = functionThree(incontinentiaButtocks)
    #printing the return value of functionThree, being the numeric part of my studentID
    print(f"functionThree returned the value of {lifeOfBrian}.")

main()
