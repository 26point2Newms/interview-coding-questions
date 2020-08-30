'''
Count the vowels and consonants in a string.

Created on Jan 13, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''

VOWELS = "aeiou"
DIGITS = "0123456789"

def countVowels(srcStr):
    vowelCount = 0
    
    for c in srcStr:
        if c in VOWELS:
            vowelCount += 1
            
    return vowelCount

def countConsonants(srcStr):
    consonantCount = 0
    
    for c in srcStr:
        if not c in VOWELS and not c in DIGITS:
            consonantCount += 1
            
    return consonantCount 
        
    
def main():
    srcString = "InterviEw Questions"
    
    # Remove spaces and convert to lower case
    srcString = srcString.replace(" ", "").lower()
    
    vowelCount = countVowels(srcString)
    consonantCount = countConsonants(srcString)
    
    print(str(vowelCount) + " vowels and " + str(consonantCount) + " consonants.")
    
if __name__ == '__main__':
    main()
    