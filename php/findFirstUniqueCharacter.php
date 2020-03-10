<?php
  /*
  Find the first non-repeated (unique) character in a given string. 
  For example, "Aardvark" would return "d". "Morning" should return "M". 

  Created on March 4, 2020
  @author: Charles Newman (https://github.com/26point2Newms)
  */

  $testStrings = array("Aardvark", "TARAMASALATA");

  foreach ($testStrings as $str)
  {
    printf("\n\tFirst unique character in %s is %s.\n", $str, findFirstUniqueChar(strtolower($str)));
  }

  function findFirstUniqueChar($testString)
  {
    $returnVal = '';
    $charDictionary = [];

    $testStringArray = str_split($testString);

    // 1st pass: add the number of character occurances to an associative array (dictionary)
    foreach ($testStringArray as $char)
    {
      if (count($charDictionary) == 0 || !array_key_exists($char, $charDictionary))
        $charDictionary[$char] = 1;
      else
        $charDictionary[$char] += 1;
    }

    // 2nd pass: look for the first character with a count of 1 in the dictionary
    foreach($testStringArray as $char)
    {
      if ($charDictionary[$char] == 1)
      {
        $returnVal = $char;
        break;
      }
    }

    return $returnVal;
}
?>

