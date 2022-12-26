print("Enter the range :")
n=int(input())
num1=0
num2=1
print(num1)
print(num2)
for i in range(n-2):
    temp=num1+num2
    num1=num2
    num2=temp
    print(temp)




'''for reverse print in renge function

 (reversed(range(1,11,1))
 '''
