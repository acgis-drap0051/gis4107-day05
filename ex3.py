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
    test_isPointOnLine()

def isPointOnLine(x, y, m, b):
    if y == m * x + b:
        return True
    else:
        return False

def test_isPointOnLine():
    print isPointOnLine(2,3,4,4)
    print isPointOnLine(2,6,2,2)

if __name__ == '__main__':
    main()