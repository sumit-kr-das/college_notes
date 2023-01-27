f = open(r"F:\COLLEGE NOTES\python\file_handeling\data.txt",'r')
w1 = open('abc.txt','w')

for i in f:
    w1.write(i)