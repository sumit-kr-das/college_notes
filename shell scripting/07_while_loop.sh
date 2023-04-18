#! /bin/bash

n=1
arr=()

while [ $n -ne 5 ]
do
    read arr[n]
    (( n++ ))
done

while [ $n -ne "${#arr[@]}" ]
do
    echo "${arr[n]}"
    (( n++ ))
done