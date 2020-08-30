'''
Print duplicate characters in a string

If string is "Javascript", output would be "a"

Created on Jan 11, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''

def findDuplicateCharsWithCount(srcStr):
    dupCharsList = []
    charsRead = []
    charsReadDict = {}  # Dictionary for keeping the duplicate character and the number of times we've seen it
    
    for c in srcStr:
        # Look in the characters we've read list and add it to our dup list if it's not already in there
        if c in charsRead and len(charsRead) > 0:
            if not c in dupCharsList:
                dupCharsList.append(c)
                # set it's count to 2 because this is the 2nd time we've read that character
                charsReadDict[c] = 2
            else:
                charsReadDict[c] = charsReadDict[c] + 1
        else:
            charsRead.append(c)
            
    return charsReadDict


def findDuplicateChars(srcStr):
    dupCharsList = []
    charsRead = []
    
    for c in srcStr:
        # Look in the characters we've read list and add it to our dup list if it's not already in there
        if c in charsRead and not c in dupCharsList:
            dupCharsList.append(c)
        else:
            charsRead.append(c)
            
    return dupCharsList
    
    
def main():
    srcString = "hippopotomonstrosesquippedaliophobia"
    print(str(findDuplicateChars(srcString.lower())))
    print(str(findDuplicateCharsWithCount(srcString.lower())))
    
if __name__ == '__main__':
    main()
    