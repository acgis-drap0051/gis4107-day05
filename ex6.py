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
    testisNumeric()

def isNumeric(testString):
    if testString[0] == "-":
        a=testString[1:]
        if a.isnumeric():
                return "Is numeric"
        else:
            return "Is not numeric"
    if testString.isnumeric():
     return "Is numeric"
    else:
     return "Is not numeric"


def testisNumeric():
    print isNumeric(u" ")
    print isNumeric(u"10")
    print isNumeric(u"-10")
    print isNumeric(u"m")
    print isNumeric(u"1")


if __name__ == '__main__':
    main()