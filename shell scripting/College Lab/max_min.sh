#! /bin/bash
echo "Enter three number"
read -a numbers

if [[ ${numbers[0]} > ${numbers[1]} ]] && [[ ${numbers[0]} > ${numbers[2]} ]]
then
    echo "Number ${numbers[0]} is big"
    if [[ ${numbers[0]} < ${numbers[1]} ]] && [[ ${numbers[0]} < ${numbers[2]} ]]
    then
        echo "Number ${numbers[0]} is small"
    elif [[ ${numbers[1]} < ${numbers[0]} ]] && [[ ${numbers[1]} < ${numbers[2]} ]]
    then
        echo "Number ${numbers[1]} is small"
    fi
elif [[ ${numbers[1]} > ${numbers[0]} ]] && [[ ${numbers[1]} > ${numbers[2]} ]]
then
    echo "Number ${numbers[1]} is big"
    if [[ ${numbers[0]} < ${numbers[1]} ]] && [[ ${numbers[0]} < ${numbers[2]} ]]
    then
        echo "Number ${numbers[0]} is small"
    elif [[ ${numbers[1]} < ${numbers[0]} ]] && [[ ${numbers[1]} < ${numbers[2]} ]]
    then
        echo "Number ${numbers[1]} is small"
    fi
else
    echo "Number ${numbers[2]} is big"
        if [[ ${numbers[0]} < ${numbers[1]} ]] && [[ ${numbers[0]} < ${numbers[2]} ]]
    then
        echo "Number ${numbers[0]} is small"
    elif [[ ${numbers[1]} < ${numbers[0]} ]] && [[ ${numbers[1]} < ${numbers[2]} ]]
    then
        echo "Number ${numbers[1]} is small"
    fi
fi