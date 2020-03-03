'''

Prints a fibonacci series for up to n items. For example, 20 items would reveal:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

Created on Jan 20, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def main():
    numbersInTheSequence = 30
    
    print([fibonacci(i) for i in range(numbersInTheSequence)])
        
if __name__ == '__main__':
    main()
    