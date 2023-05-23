def Merge(A,B): # O(n)
    C=[]
    a=len(A)    
    b=len(B)
    i,j=0,0
    while i+j<a+b:
        if i==a:
            C.append(B[j])
            j+=1
        elif j==b:
            C.append(A[i])
            i+=1
        elif A[i]<=B[j]:
            C.append(A[i])
            i+=1
        elif A[i]>B[j]:
            C.append(B[j])
            j+=1

    return C

def Merge_Sort(A):  # T(n)= 1 + 1 + T(n/2) + T(n/2) + O(n) = 2T(n/2) + cn
    if len(A)<2:
        return A
    else:
        mid=len(A)//2
        L=Merge_Sort(A[0:mid])         # Left Half
        R=Merge_Sort(A[mid:len(A)])    # Right Half 
        return(Merge(L,R))

ll=[25,5,35,20,15,40,50]
print(Merge_Sort(ll))



        
