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
    test_getFeatureType()

def getFeatureType(featureCode):
    if featureCode == 1:
        return "Point"
    if featureCode == 2:
        return "Polyline"
    if featureCode == 3:
        return "Polygon"

def test_getFeatureType():
    print "expect point"
    print getFeatureType(1)
    print "expect Polyline"
    print getFeatureType(2)
    print "expect Polygon"
    print getFeatureType(3)

if __name__ == '__main__':
    main()

