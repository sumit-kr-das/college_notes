# Assignment c1
a=10
b=12
try:
    print(a/b)
    print("This won't be printed")
    print('10'+10)
except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("You divided by 0")

# Assignment c2
# with open('first.txt','r') as firstfile, open('second.txt','w') as secondfile:
# 	for line in firstfile:
# 			secondfile.write(line)
