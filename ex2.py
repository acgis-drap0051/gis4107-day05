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
    test_isPointInBox()

def isPointInBox(x, y, xmin, ymin, xmax, ymax):
    if x > xmin and x < xmax and y > ymin and y < ymax:
        return True
    else:
        return False

def test_isPointInBox():
    print isPointInBox(2,3,1,1,5,5)
    print isPointInBox(1,3,2,2,5,5)
    print isPointInBox(2,3,2,2,5,5)


if __name__ == '__main__':
    main()

