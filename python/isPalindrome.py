'''
Determine if a string is a palindrome.
A palindrome is a word, phrase, or sequence that reads the 
same backward as forward, e.g., "madam" or "nurses run".

Created on Aug 4, 2020

@author: Charles Newman (https://github.com/26point2Newms)
'''

def isPalindrome(s: str) -> bool:
	validChars = "abcdefghijklmnopqrstuvwxyz0123456789"
	scrubbedStr = ""
	
	s = s.lower()
	
	for c in s:
		if c in validChars:
			scrubbedStr += c
	
	if scrubbedStr == scrubbedStr[::-1]:
		return True
	else:
		return False
		
def main():
	str = "A man, a plan, a canal: Panama"
	print(isPalindrome(str))

	str = "madam"
	print(isPalindrome(str))

	str = "nurses run"
	print(isPalindrome(str))

	str = "0P"
	print(isPalindrome(str))


if __name__ == '__main__':
	main()
	