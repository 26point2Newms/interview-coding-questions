'''
Determine if one number is evenly divisible by another.

Created on Jan 20, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''

def isDivisibleBy(leftOperand, rightOperand):
    return (leftOperand % rightOperand) == 0

def main():
    testNumber = 1234
    rOperand = 2
    
    isDivisible = isDivisibleBy(testNumber, rOperand)
    
    if isDivisible == True:
        print str(testNumber) + " is divisible (is a factor of) " + str(rOperand)
    else:
        print str(testNumber) + " is NOT divisible (is NOT a factor of) " + str(rOperand)
    
if __name__ == '__main__':
    main()
    