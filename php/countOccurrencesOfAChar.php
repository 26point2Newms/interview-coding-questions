<?php
  /*
  Count occurrences of a given character in a string.

  Created on March 3, 2020
  @author: Charles Newman (https://github.com/26point2Newms)
  */

  $testStr = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...";

  // Method #1: Looping over the characters
  printf("\n\tUsing looping method: %d\n", countOccurrences(strtolower($testStr), "i"));

  // Method #2: Use the built in substr_count function
  printf("\n\tUsing built in function: %d\n", substr_count(strtolower($testStr), "i"));

  function countOccurrences($targetStr, $targetChar)
  {
    $occurrences = 0;

    $targetStrArray = str_split($targetStr);

    foreach ($targetStrArray as $char)
    { 
      if ($char == $targetChar)
        $occurrences++;
    }
    
    return $occurrences;
  }
?>

