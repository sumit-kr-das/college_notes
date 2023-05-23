echo "Enter a number: "
read n
temp=$n
sum=0
while [ $n -ne 0 ]
do
    rev=$(( $n%10 ))
    sum=$(( $sum*10+$rev ))
    n=$(( $n/10 ))
done

if [ $sum -eq $temp ]
then
    echo "This is an armstrong number $sum"
else
    echo "This is not an armstrong number $sum"
fi