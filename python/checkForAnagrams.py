'''
Check to see if two strings are an anagram of each other.
An anagram is a word, phrase, or name formed by rearranging the letters 
of another, such as "cinema" formed from "iceman".

Created on Jan 11, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''
def charsMatch(firstString, secondString):
    allMatch = True
    
    # is each character in the first string in the second string
    for c in firstString:
        if not c in secondString:
            allMatch = False
            break
        
    return allMatch

def charsCount(firstStr, secondStr):
    charDict = {}
    for c in firstStr:
        if len(charDict) == 0 or not c in charDict:
            charDict[c] = 1
        else:
            charDict[c] += 1
            
    charDict2 = {}
    for c in secondStr:
        if len(charDict2) == 0 or not c in charDict2:
            charDict2[c] = 1
        else:
            charDict2[c] += 1

    for c in firstStr:
        if charDict[c] != charDict2[c]:
            return False
    return True

def anagramCheck(firstString, secondString):
    
    isAnagram = True
    
    # check the length, if different, it's not an anagram
    if len(firstString) != len(secondString):
        isAnagram = False
    # each character in the 2nd string should be in the first and vice versa
    elif not charsMatch(firstString, secondString) or not charsMatch(secondString, firstString):
        isAnagram = False
    # next we need to check the individual character counts in both strings
    elif not charsCount(firstString, secondString):
        isAnagram = False
    return isAnagram
    
def main():
    str1 = "desserts"
    str2 = "stressed"
    #str1 = "aacc"
    #str2 = "ccac"
    
    print(anagramCheck(str1, str2))

if __name__ == '__main__':
    main()
    