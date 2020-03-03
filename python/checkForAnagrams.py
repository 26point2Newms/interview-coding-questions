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
            break;
        
    return allMatch
    
def anagramCheck(firstString, secondString):
    
    isAnagram = True
    
    # check the length, if different, it's not an anagram
    if len(firstString) != len(secondString):
        isAnagram = False
    # each character in the 2nd string should be in the first and vice versa
    elif not charsMatch(firstString, secondString) or not charsMatch(secondString, firstString):
        isAnagram = False

    return isAnagram
    
def main():
    str1 = "desserts"
    str2 = "stressed"
    
    print anagramCheck(str1, str2)

if __name__ == '__main__':
    main()
    