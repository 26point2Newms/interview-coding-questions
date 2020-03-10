<?php
  /*
    Reverse the words in a string.
    Given a string (a sentence) such as "THIS IS AN INTERVIEW", 
    reverse each word in the string, such as "SIHT SI NA WEIVRETNI"

    Created on March 10, 2020 
    @author: Charles Newman (https://github.com/26point2Newms)
  */

  $src = "SIHT SI NA WEIVRETNI";
  $reversedWords = [];

  // Split the string on spaces and create an array of words
  $wordsArray = explode(" ", $src);

  // Iterate over the words and reverse each one
  foreach ($wordsArray as $word) 
  {
    $reversedWords[] = strrev($word);
  }

  $output = implode(" ", $reversedWords);
  echo $output;

?>
    
