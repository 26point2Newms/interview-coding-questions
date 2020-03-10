<?php
  /*
  Count the vowels and consonants in a string. We'll use the Merriam-Webster
  Dictionary definition of a consonant as "a letter representing a consonant,
  usually used in English of any letter except a, e, i, o, and u".

  Created on March 4, 2020
  @author: Charles Newman (https://github.com/26point2Newms)
  */

  define("VOWELS", array('a','e','i','o','u'));
  define("DIGITS", array('0','1','2','3','4','5','6','7','8','9'));

  $srcString = "InterviEw Questions";

  // Remove spaces and convert to lower case
  $srcString = str_replace(" ", "", strtolower($srcString));
  
  $vowelCount = countVowels($srcString);
  $consonantCount = countConsonants($srcString);

  printf("\n\t%d vowels and %d consonants!\n", $vowelCount, $consonantCount);

  function countVowels($str)
  {

    $vowelCount = 0;

    $strArray = str_split($str);

    foreach ($strArray as $char)
    {
      if (in_array($char, VOWELS))
        $vowelCount++;
    }
    
    return $vowelCount;
  } 

  function countConsonants($str)
  {
    $consonantCount = 0;

    $strArray = str_split($str);

    foreach ($strArray as $char)
    {
      if (!in_array($char, VOWELS) && !in_array($char, DIGITS))
        $consonantCount++;
    }
  
    return $consonantCount;
  }
?>
