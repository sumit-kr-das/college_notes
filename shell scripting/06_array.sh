#! /bin/bash

os=('windows' 'ubuntu' 'kali' 'mac')

os[3]="pop-os" # chenge the value os the particular index
unset os[3] # remove the particular index

# print all elements of the array
echo "${os[@]}" 
# print all indexes of the array
echo "${!os[@]}" 
# print 0th element of the array
echo "${os[0]}" 
# print length of the array
echo "${#os[@]}" 