<?php
$numbers = [];

$i = 1;
// Picks 6 numbers
while($i <= 6)
{
// Numbers will be picked between 1 and 45
    $number = mt_rand(0, 45);

    if(!in_array($number, $numbers))
    {
        array_push($numbers, $number);
        $i++;
    }
}

sort($numbers);

echo implode(" - ", $numbers);
