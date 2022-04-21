def addTimes():
    Time1 = float(input("Enter your first time in seconds: "))
    Time2 = float(input("Enter your second time in seconds: "))
    return Time1 + Time2

def subTimes():
    Time1 = float(input("Enter your first time in seconds: "))
    Time2 = float(input("Enter your second time in seconds: "))
    return Time1 - Time2

def divideTimes():
    Time1 = float(input("Enter your first time in seconds: "))
    Time2 = float(input("Enter your second time in seconds: "))
    return Time1 / Time2

def moduloTimes():
    Time1 = float(input("Enter your first time in seconds: "))
    Time2 = float(input("Enter your second time in seconds: "))
    return Time1 % Time2

def timeConversion(Time):
    minutes = int(Time/60)
    hours = int(Time/3600)
    days = int(Time/86400)
    remainingSecs = int(Time%60)
    remainingMins = int(minutes%60)
    remainingHrs = int(hours%24)
    print("The time converted from seconds is:", days, "days:", remainingHrs, "Hours:",
          remainingMins, "Minutes:", remainingSecs, "Seconds.")

myInput = 0
while myInput != 'q':
    print("""Choose (a) to add\nChoose (b) to substract\nChoose (c) to divide\nChoose (d) to modulo\nChoose 'q' to exit""")
    myInput = input("Choose your option: ")
    
    if myInput == 'a':
        # adding times
        timeConversion(addTimes())
        
    elif myInput == 'b':
        # adding times
        timeConversion(subTimes())
        
    elif myInput == 'c':
        # adding times
        timeConversion(divideTimes())
        
    elif myInput == 'd':
        # adding times
        timeConversion(moduloTimes())
        
    elif myInput == 'q':
        print("Exit Program")
        
    else:
        print("You have entered an invalid input")
