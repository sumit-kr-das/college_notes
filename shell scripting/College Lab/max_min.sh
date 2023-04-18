#! /bin/bash
echo "Enter three number"
read -a numbers

if [[ ${numbers[0]} > ${numbers[1]} ]] && [[ ${numbers[0]} > ${numbers[2]} ]]
then
    echo "Number ${numbers[0]} is big"
elif [[ ${numbers[1]} > ${numbers[0]} ]] && [[ ${numbers[1]} > ${numbers[2]} ]]
then
    echo "Number ${numbers[1]} is big"
else
    echo "Number ${numbers[2]} is big"
fi