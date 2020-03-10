<?php
  /*
  Check to see if a string contains only digits.

  Created on March 3, 2020
  @author: Charles Newman (https://github.com/26point2Newms)
  */

  $stringsToTest = array("847283765910", "ascii943", "ascii", "342865w");

  foreach ($stringsToTest as $str)
  {
    printf("\n\t'%s' %s", $str, containsOnlyDigits($str) ? "\tcontains only digits!" : "\tdoes NOT contain only digits!");
  }
  
  printf("\n");

  function containsOnlyDigits($testString)
  {
    // Match any non-digit character (opposite is \d which matches any digit character 0-9)
    return !preg_match("/\D/", $testString);
  }
?>

