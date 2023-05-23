# *
# * *
# * * *
# * * * *
# * * * * *

rows=5
for ((i=1; i<=rows; i++))
do
    for ((j=1; j<=i; j++))
    do
        echo -n "* "
    done
    echo
done
# .......................................................
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num=1
for ((i=1; i<=5; i++))
do
    for ((j=1; j<=i; j++))
    do
        echo -n "$num "
        num=$(( num + 1 ))
    done
    num=1
    echo
done
# .....................................................
# * * * * *
# * * * *
# * * *
# * *
# *

for ((i=5; i>=1; i--))
do
    for(( j=1; j<=i; j++ ))
    do
        echo -n "* "
    done
    echo
done
# ............................................................................
#        *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

row=5
for ((i=1; i<=row; i++))
do
    for ((j=1; j<=row-i; j++))
    do
        echo -n "  "
    done
    for ((j=1; j<=2*i-1; j++))
    do
        echo -n "* "
    done
    echo 
done