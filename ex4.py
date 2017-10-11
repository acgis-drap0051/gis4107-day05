#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MCE
#
# Created:     03/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    test_whatIsMyVar()

def whatIsMyVar(myVar):
    if myVar %2:
     if myVar**3!=27:
        myVar += 4
        return myVar
     else:
        myVar /= 1.5
        return myVar
    else:
        if myVar <= 10:
            myVar *= 2
            return myVar
        else:
            myVar -= 2
            return myVar

def test_whatIsMyVar():
    print "Expect: 5 Actual: " + str(whatIsMyVar(1))
    print "Expect: 2 Actual: " + str(whatIsMyVar(3))
    print "Expect: 4 Actual: " + str(whatIsMyVar(2))
    print "Expect: 10 Actual: " + str(whatIsMyVar(12))

if __name__ == '__main__':
    main()