'''
Rotate the contents of an array, like a circular queue, n items
are removed from the end and added to the front, as if each item
falls off the end and goes to the front. This happens n times.

[56,3,22,78,5,1,9] and n = 3, result should be:
[5,1,9,56,3,22,78]

Created on Aug 27, 2020

@author: Charles Newman (https://github.com/26point2Newms)
'''

def rotate(nums, n) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""

	# We'll pop one off the back, and insert at the front
	for _ in range(0, n):
		nums.insert(0, nums.pop())


def main():
	nums = [56,3,22,78,5,1,9]
	print("before: " + str(nums))
	rotate(nums, 3)
	print("after: " + str(nums))

	nums = [654,78,951,324,654,84,87,98,65,32,21,0,1,2,3,8,4,5,4,6984,654,484654]
	print("before: " + str(nums))
	rotate(nums, 10)
	print("after: " + str(nums))

if __name__ == '__main__':
    main()
    