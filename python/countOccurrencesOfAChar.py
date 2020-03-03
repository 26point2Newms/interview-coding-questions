'''
Count occurrences of a given character in a string

Created on Jan 17, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''

def countOccurrences(targetStr, targetChar):
    occurrences = 0
    
    for c in targetStr:
        if c == targetChar:
            occurrences += 1
            
    return occurrences
        
def main():
    
    testStr = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
    
    # Method #1: Looping over the characters
    print countOccurrences(testStr.lower(), 'i')
    
    # Method #2: using the built in count() function in Python
    print testStr.lower().count('i')
    
    

if __name__ == '__main__':
    main()
    