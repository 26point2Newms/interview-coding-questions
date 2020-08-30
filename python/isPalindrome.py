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
	#str = "0P"
	print(isPalindrome(str))

if __name__ == '__main__':
	main()
	