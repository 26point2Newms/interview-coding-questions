<?php
/*
  Determine if one number is evenly divisible by another.

  Created on March 4, 2020
  @author: Charles Newman (https://github.com/26point2Newms)
*/

  $testNum = 1234;
  $operand = 2;

  if (isDivisibleBy($testNum, $operand))
    printf("\n\t%d is divisible (is a factor of) %d\n", $testNum, $operand);
  else
    printf("\t%d is NOT divisible (is NOT a factor of) %d\n", $testNum, $operand);

  function isDivisibleBy($num, $oper)
  {
    return (($num % $oper) == 0);
  }
?>

