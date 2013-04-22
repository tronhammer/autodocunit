<?php
include_once('/Users/apple/Sites/autodocunit/tests/funcs.php');

/*
     Test Function For AutoDocUnit
     This will be the preliminary test function for the AutoDocUnit program.
*/
function _autodocunit_test_func(){
     $ret = test_func("main.py", 54);
     return $ret == true;
}


/*
     Second Test Function For AutoDocUnit
     This will be another the preliminary test function for the AutoDocUnit program. In all honesty, it is to double check that the compiler doesn't miss a single piece
*/
function _autodocunit_second_test_func(){
     $ret = second_test_func(54, json_decode('{"testo": "presto"}'));
     return $ret == true;
}


echo json_encode(array("_autodocunit_test_func" => _autodocunit_test_func(),"_autodocunit_second_test_func" => _autodocunit_second_test_func()));
