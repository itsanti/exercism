<?php

function from($date) {
	$date->add(new DateInterval('PT'.pow(10, 9).'S'));
	return $date;
}
