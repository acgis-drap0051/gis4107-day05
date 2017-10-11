#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MCE
#
# Created:     08/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def main():
    if len(sys.argv)!=2:
        print 'Usage: ex7.py' + testValue

#def test():
    #Test_isITrue
    #sys.exit()

def isItTrue(testValue):
    print "Type is " + type(testValue)
    if testValue == "True":
        return testValue + " is true"

    else:
        return testValue + " is false"

def Test_isITrue():
    print isItTrue(" ")
    print isItTrue(' ')
    print isItTrue(Great)
    print isItTrue(0)
    print isItTrue(1)
    print isItTrue(-3)

#if __name__ == '__main__':
    #main()
