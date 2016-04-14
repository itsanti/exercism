<?php

/**
 * @param $a string nucleic acid
 * @param $b string nucleic acid
 * @return int Hamming distance
 */
function distance($a, $b)
{   
	if ($a == $b) {
		return 0;
	}
	
	if(strlen($a) != strlen($b)) {
		throw new InvalidArgumentException( 'DNA strands must be of equal length.' );
	}

	$diff = array_map(function($a, $b){
		return $a != $b;
	}, str_split($a), str_split($b));

	return array_reduce($diff, function($sum, $item){
		return $sum +  $item;
	}, 0);
}

assert(7 == distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'));
