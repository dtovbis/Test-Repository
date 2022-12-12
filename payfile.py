#This function calculates the salary given a number of hours worked and the rate of pay.
#It gives time and a half for >40 hours a week.
def payrate(hrs,rt):
    try:
        if hrs > 40:
            pyv= 40*rt+(hrs-40)*(rt*1.5)
        else :
            pyv= hrs*rt
        return ("Pay: " + str(pyv)) 
    except:
        return "Please enter a numeric value"
totalpay=payrate(45,10)
print(totalpay)