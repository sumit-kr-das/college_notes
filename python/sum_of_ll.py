def sumLL(l1, l2):
    ll = []
    if(len(l1) == 0 and len(l2) == 0):
        return ll
    
    if(len(l1) != 0):
        ll.append(l1[0])
    if(len(l2) != 0):
        ll.append(l2[len(l2)-1])
        
    return ll + sumLL(l1[1:], l2[:len(l2)-1])
    

l1 = [1,2,3,4]
l2 = ['a','b', 'c', 'd', 'e', 'f']
print(l1)
print(l2)
print("After appending: ", sumLL(l1, l2))
