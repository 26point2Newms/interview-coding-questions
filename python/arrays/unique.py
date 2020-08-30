'''
Find the unique character in a non-empty array.
In other words, every character in the array is
duplicated (repeats) except for one.

Goal is linear time complexity of O(n).

Return the unique character.

Created on Aug 27, 2020

@author: Charles Newman (https://github.com/26point2Newms)
'''

def unique(items):
	'''
	Shooting for O(n) or linear time complexity we'll 
	iterate through the list once add the item to a
	dictionary using it as a key with a count of 1.
	If we see the item again, we'll pop it off (remove it)
	from the dictionary. At the end of our single iteration
	there should be only one item in the dictionary and we 
	want it's key, which is the unique item.
	'''

	lookup = dict()

	for n in items:
		key = str(n)
		if not key in lookup:
			lookup[key] = 1
		else:
			lookup.pop(key)
	return list(lookup.keys())[0]

def main():
	lst = [78,65,4,78,65,4,2,99,99]
	print("unique item in " + str(lst) + " is: " + str(unique(lst)))

if __name__ == '__main__':
	main()
  