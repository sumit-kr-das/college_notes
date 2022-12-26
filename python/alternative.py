def alternative(ll, i):
    if i >= len(ll):
        return;
    print(ll[i],end=" ")
    alternative(ll, i+2)

def alternate(ll,i):
    l =[]
    if i >= len(ll):
        return l
    l.append(ll[i])
    ll = alternate(ll, i+2)
    for i in ll:
        l.append(i)
    return l


ll = [1,2,3,4,5,6,7,8,9,10, 11]
alternative(ll,0)
print()
print(alternate(ll,0))
