'''
Find the intersection of two lists which can contain duplicates.
Output should be the intersection of the lists and each element 
in the result should appear as many times as it shows in both lists.

For example:

listA = [4,9,5]
listB = [9,4,9,8,4]
intersection will be [4,9]

listA = [1,2,2,1]
listB = [2,2]
intersection will be [2,2] because that element appears twice in 
each list.

Created on Aug 27, 2020

@author: Charles Newman (https://github.com/26point2Newms)
'''

def intersection(list1, list2):

	'''
	We'll use a dictionary to store each item (the key) and
	how many times we see it in the first list.
	Then we'll iterate over the second list and if an item
	(the key) is in the dictionary, it means it's also in
	the first list so we'll add it to our result list, 
	decrement the count (number of times we've seen it)
	and if the count reaches zero, we'll remove it from 
	the dictionary.
	'''

	match = dict()
	
	for n in list1:
		if n in match:
			match[n] += 1
		else:
			match[n] = 1
	
	returnVal = []
	for n in list2:
		if n in match:
			returnVal.append(n)
			match[n] -= 1
			if match[n] == 0:
				match.pop(n)
	return returnVal

def main():
	listA = [4,9,5]
	listB = [9,4,9,8,4]	
	print("Intersection of listA: " + str(listA) + " and listB: " + str(listB) + 
			" is: " +  str(intersection(listA, listB)))

	listA = [1,2,2,1]
	listB = [2,2]
	print("Intersection of listA: " + str(listA) + " and listB: " + str(listB) + 
			" is: " +  str(intersection(listA, listB)))

if __name__ == '__main__':
	main()
  