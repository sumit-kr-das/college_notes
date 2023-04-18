#! /bin/bash
word=b
if [[ $word == "a" ]] 
then
    echo "This is a"
elif [[ $word == "b" ]]
then
    echo "This is b"
else
    echo "This is not a and b"
fi