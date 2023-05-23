# fibonacci up to given number

n1=0
n2=1
nextTerm=$((n1+n2))
echo "Enter your number: "
read n
echo -n "${n1} ${n2} "
while [ $nextTerm -le $n ]
do
    echo -n "${nextTerm} "
    n1=${n2}
    n2=${nextTerm}
    nextTerm=$((n1+n2))
done
