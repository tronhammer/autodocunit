<?php
	/**
	 * Test Function For AutoDocUnit
	 *
	 * This will be the preliminary test function for the 
	 * AutoDocUnit program.
	 *
	 * @param Int $int ==#{54}# Test string that will be used for bs.
	 * @param String $filename ==#{"main.py"}# Test string that will be used for bs.
	 *
	 * @return Bool $ret ==#{true}# if verify works, False if verification fails.
	 **/
	function test_func($filename, $int){
		
		return file_exists($filename);
	}
	
	/**
	 * Second Test Function For AutoDocUnit
	 *
	 * This will be another the preliminary test function for the 
	 * AutoDocUnit program. In all honesty, it is to double check
	 * that the compiler doesn't miss a single piece
	 *
	 * @param Int $int ==#{54}# Test string that will be used for bs.
	 * @param Object $item ==#{"testo": "presto"}# Test string that will be used for bs.
	 *
	 * @return Bool $ret ==#{true}# if verify works, False if verification fails.
	 **/
	function second_test_func($int, $item){
		
		return true;
	}
	
