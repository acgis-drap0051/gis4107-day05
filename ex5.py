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
    test_isDivisibleBy()

def isDivisibleBy(numerator, denominator):
    n = str(numerator);
    print n.isdigit()
    d = str(denominator);
    print d.isdigit()

def test_isDivisibleBy():
    print isDivisibleBy(8,2)

if __name__ == '__main__':
    main()