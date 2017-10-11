#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      MCE
#
# Created:     04/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    testisDivisibleBy()

def isDivisibleBy(numerator,denominator):
    y = numerator.isdigit()
    x = denominator.isdigit()
    if y == True and x == True:
        if int(numerator)%int(denominator):
            return str(numerator) + " Dividing by " + str(denominator) + " has a remainder"
        else:
            return str(numerator) + " is divisible by " + str(denominator) + " with no remainder"

    else:
     return "Both arguments must be numeric"


def testisDivisibleBy():
    print isDivisibleBy("10","5")
    print isDivisibleBy("9","5")
    print isDivisibleBy("m","5")

if __name__ == '__main__':
    main()