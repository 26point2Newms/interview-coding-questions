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
	If we see the item again we're done.
	'''

	lookup = dict()

	for i in items:
		key = i
		if not key in lookup:
			lookup[key] = 1
		else:
			# We could simply return True here right away because 
			# we now know the value has occurred previously, but 
			# if we wish to enhance this code later to return 
			# the number of occurances of the duplicates we 
			# would increment the count like this:
			lookup[key] += 1
			return True
	return False

def main():
	lst = [1,2,3,47,91,15,72,77,47,42]	
	lst2 = [489,24,156,55,15,12,888,987,21,22]
	print(str(lst)+" contains dups? " + str(hasDuplicates(lst)))
	print(str(lst2)+" contains dups? " + str(hasDuplicates(lst2)))

if __name__ == '__main__':
	main()
  