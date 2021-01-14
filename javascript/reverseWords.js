/*
Reverse the words in a string.

Given a string (a sentence) such as "THIS IS AN INTERVIEW", 
reverse each word in the string, such as "SIHT SI NA WEIVRETNI"

Created on Jan 12, 2021

@author: Charles Newman (https://github.com/26point2Newms)
*/

const input = "THIS IS AN INTERVIEW";

function reverseString(str) {
    /* 
	Reverses a string in place. Note that Javascript does not have
	a built-in reverse method on the string object.

	How it works (given the input "THIS"):
    1) The split() method returns a new array, i.e. ["T", "H", "I", "S"].
    2) The reverse() method reverses the array, i.e. ["S", "I", "H", "T"]
	3) The join() method joins all elements of the array into a string, i.e, "SIHT"
	
    In this case we are chaining these together because the methods return
    the item we want to call the next method on.
    */
    return str.split("").reverse().join("");
}

/*
Using the reverseString() method above, we can do this in one line.

The split() method will split a string into an array of substrings given the separator ' '.
So for example, calling split(' ') on a string containing "one two three" will 
create the array ["one", "two", "three"].

The Array.map() method creates a new array populated with the results of calling
the provided function on every element in the calling array.

The => syntax is called an Arrow Function with the left side of the =>
being the function argument and the right side the expression of the function.
*/

console.log(input.split(' ').map(str => reverseString(str)).join(' '));