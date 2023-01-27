def calculatePay():
    # This first line is provided for you
    try:
        hrs = float(input("Enter Hours:"))
    except ValueError:
        print("Error, please enter numeric input")
        return
    try:
        rate = float(input("Enter Rate:"))
    except ValueError:
        print("Error, please enter numeric input")
        return
    if hrs > 40:
        ot = (hrs - 40)*(rate * 1.5)
        pay = (40 * rate) + ot
    else:
        pay = hrs * rate

    print(f"Pay: {pay}")
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
