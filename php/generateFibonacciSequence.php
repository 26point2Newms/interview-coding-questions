<?php
/*
  Prints a fibonacci series for up to n items. For example, 20 items would reveal:
  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

  Created on March 4, 2020 
  @author: Charles Newman (https://github.com/26point2Newms)
*/

  define("NUMBERS_IN_SEQUENCE", 30);

  for ($i = 0; $i < NUMBERS_IN_SEQUENCE; $i++)
  {
    printf("%d", fibonacci($i));
    if ($i < (NUMBERS_IN_SEQUENCE - 1))
      printf(", ");
  }

  function fibonacci($n)
  {
    if ($n == 0 || $n == 1)
      return $n;
    else
      return fibonacci($n - 1) + fibonacci($n - 2);
  }
?>

