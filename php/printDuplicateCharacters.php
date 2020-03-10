<?php
  /*
  Print duplicate characters in a string.
  If string is "Javascript", output would be "a"

  Created on March 7, 2020
  @author: Charles Newman (https://github.com/26point2Newms)
  */

  $srcString = "hippopotomonstrosesquippedaliophobia";

  printf("\n\tDuplicate characters in '%s' are:\n", $srcString);
  print_r(findDuplicateChars($srcString));

  printf("\n\tDuplicate characters with their count in '%s' are:\n", $srcString);
  print_r(findDuplicateCharsWithCount($srcString));


  function findDuplicateCharsWithCount($srcStr)
  {
    $dupChars = [];
    $charsRead = [];
    $charsReadDictionary = [];

    $srcStrArray = str_split($srcStr);

    foreach ($srcStrArray as $char)
    {
      // Look in the list of characters we've read and add it to our duplicate list if it's not already in there
      if (count($charsRead) > 0 && in_array($char, $charsRead))
      {
        if (!in_array($char, $dupChars))
        {
           $dupChars[] = $char;

           // Set it's count to 2 because this is the 2nd time we've read that character
           $charsReadDictionary[$char] = 2;
        }
        else
          $charsReadDictionary[$char] += 1;
      }
      else
        $charsRead[] = $char;
    }
    
    return $charsReadDictionary;
  }
  
  function findDuplicateChars($srcStr)
  {
    $dupCharsList = [];
    $charsRead = [];
  
    $srcStrArray = str_split($srcStr);

    foreach ($srcStrArray as $char)
    {
      // Look in the characters list we've read and add it to our duplicate list if it's not already there
      if (in_array($char, $charsRead) && !in_array($char, $dupCharsList))
        $dupCharsList[] = $char;
      else
        $charsRead[] = $char;
    }
  
    return $dupCharsList;
  }

?>


