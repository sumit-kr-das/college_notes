# with range

echo "Enter the starting number: "
read start
echo "Emter the Ending number"
read end



for ((i=$start; i<=$end; i++))
do
    # calculate range
    powNum=$i
    # echo ${tempSum}
    pow=0
    while [ $powNum -ne 0 ]
    do
        pow=$((pow+1))
        powNum=$((powNum/10))
    done
# echo "pow is ${pow}"
    sum=0
    tempSum=$i
    num=$i
            while [ $num -ne 0 ]
        do
            rem=$((num % 10))
            sum=$((sum+rem**pow))
            num=$((num/10))
        done

        if [[ $sum == $tempSum ]]
        then 
            echo "This is a armstrong ${sum}"
            fi

done

