def rev(st, i):
    if(i == 0):
        return st[i];
    return st[i] + rev(st,i-1)

ll= [1,2]
l = []
l.append(3)
l.insert(ll)
