<?php
  /*
  Check to see if two strings are an anagram of each other.
  An anagram is a word, phrase, or name formed by rearranging the letters 
  of another, such as "cinema" formed from "iceman".

  Created on March 3, 2020
  @author: Charles Newman (https://github.com/26point2Newms)
  */

  $str1 = "desserts";
  $str2 = "stressed";

  printf("\n\t'%s' and '%s' %s anagrams!\n", $str1, $str2, anagramCheck($str1, $str2) ? "are" : "are not");

  function anagramCheck($firstString, $secondString)
  {
    $isAnagram = true;

    // Check the length, if different, no anagram
    if (strlen($firstString) != strlen($secondString))
      $isAnagram = false;
    // Otherwise each character in the 2nd string should be in the first string and vice versa
    else if (!charsMatch($firstString, $secondString) || !charsMatch($secondString, $firstString))
      $isAnagram = false;

    return $isAnagram;
  }

  function charsMatch($firstString, $secondString)
  {
    $allMatch = true;

    // Is each character in the first string also in the second string?
    $str1Array = str_split($firstString);

    foreach ($str1Array as $char)
    {
      if (stripos($secondString, $char) == false)
      {
        $allMatch = false;
        break;
      }
      
      return $allMatch;
    }
  }
?>

