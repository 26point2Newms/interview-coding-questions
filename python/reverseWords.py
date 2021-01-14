'''

Reverse the words in a string

Given a string (a sentence) such as "THIS IS AN INTERVIEW", 
reverse each word in the string, such as "SIHT SI NA WEIVRETNI"

Created on Jan 11, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''

def reverseString(targetStr):
    # 1)  Brut Force Method:
    '''
    revStr = ""
    i = len(targetStr) - 1
    
    while i >=0:
        revStr += targetStr[i]
        i -= 1
        
    return revStr
    '''

    # 2) Using Python's slicing notation
    '''
    Slicing is a way of getting subsets of data structures. 
    The basic notation is: [start:stop:step] 
    The default for start is none or 0. 
    The default stop is the end of your data structure. 
    Using a positive number references from the first element, 
    a negative number references from last element in your structure.
    
    So for example, given this list: mylist=[1,2,3,4,5,6,7,8,9]
    This syntax: mylist[2:8:3] would return "[3,6]"
    '''

    return targetStr[::-1]
        
def main():
    src = "SIHT SI NA WEIVRETNI"
                
    # The default arg for split is (" ", 1) meaning 1 whitespace character
    # this creates a list of words in the sentence
    strList = src.split()
    
    resultStr = ""
    
    # Iterate over the list of words and reverse each one
    srcLen = len(src) - 1
    
    for i, wrd in enumerate(strList):
        resultStr += reverseString(wrd)
        # only add a whitespace separator if it's not the last word
        if i < srcLen :
            resultStr += " "
    
    print("src=" + src)
    print("reversed=" + resultStr)
        
if __name__ =="__main__":
    main()
 