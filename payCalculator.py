def calculatePay():
    # This first line is provided for you
    try:
        hrs = float(input("Enter Hours:   "))
    except ValueError:
        hrs = float(input("Error, please enter a numeric value: "))
    try:
        rate = float(input("Enter Rate:   "))
    except ValueError:
        rate = float(input("Error, please enter a numeric value: "))
    if hrs > 40:
        otHours = hrs - 40
        print("Pay: " + str(rate * 40 + (otHours*1.5*rate) + "\n"))
    else:
        print("Pay: " + str(hrs * rate)+ "\n")
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
