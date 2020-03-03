'''
Check to see if a string contains only digits.

Created on Jan 11, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''
import re

def containsOnlyDigits(testString):
    retVal = True
    regEx = re.compile('\D')    # matches any non-digit character (opposite is \d which matches any digit character 0-9)
    
    # return false if we find any non-digit characters
    if regEx.search(testString):
        retVal = False
        
    return retVal
    
def main():
    testStr = "857448"
    testStr2 = "ascii943"
    testStr3 = "ascii"
    
    print containsOnlyDigits(testStr)
    print containsOnlyDigits(testStr2)
    print containsOnlyDigits(testStr3)

if __name__ == '__main__':
    main()
    