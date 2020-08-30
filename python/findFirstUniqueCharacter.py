'''

Find the first non-repeated (unique) character in a given string. For example, "Aardvark" would return "d".
"Morning" should return "M". 

Created on Jan 11, 2017

@author: Charles Newman (https://github.com/26point2Newms)
'''

def findFirstUniqueChar(testString):
	retVal = ''
	
	charDict = {}
	
	for c in testString:
		if len(charDict) == 0 or not c in charDict:
			charDict[c] = 1
		else:
			charDict[c] += 1
			
	# 2nd pass: look for the first character with a count of 1 in the dictionary
	for c in testString:
		if charDict[c] == 1:
			retVal = c
			break
			
	return retVal

def main():
	testStr = "aardvark"
	print(findFirstUniqueChar(testStr))
	testStr2 = "TARAMASALATA"
	print(findFirstUniqueChar(testStr2))

if __name__ == '__main__':
	main()
	