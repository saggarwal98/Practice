#!/bin/bash
function greeter(){
    local NAME=$1
    echo "Hello $NAME"
    $2
}
goodbye(){
    echo "see you soon"
}
greeter Shubham goodbye