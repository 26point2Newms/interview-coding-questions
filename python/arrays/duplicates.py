'''
Return True if any value in a list appears at least twice,
return False otherwise.

Created on Aug 27, 2020

@author: Charles Newman (https://github.com/26point2Newms)
'''

def hasDuplicates(items):
	'''
	Shooting for O(n) or linear time complexity we'll 
	iterate through the list once add the item to a
	dictionary using it as a key with a count of 1.
	If we see the item again, we'll increment it's count. 
	If the item count we just increments is >= 2, we're done.
	'''

	lookup = dict()

	for i in items:
		key = str(i)
		if not key in lookup:
			lookup[key] = 1
		else:
			lookup[key] += 1
			if lookup[key] >=2:
				return True
	return False

def main():
	lst = [1,2,3,1]
	print(str(lst)+" contains dups? " + str(hasDuplicates(lst)))

if __name__ == '__main__':
	main()
  