def Partition_1(arr,lb,ub):     # O(n), as the loop iterates (ub-lb+1) times, size of the list
    pivot = arr[lb]
    i = lb
    j = ub
    while i < j:
        while i <= j and arr[i] <=pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[lb] = arr[lb], arr[j]
    return j


def Partition_2(arr,lb,ub):           # O(n)
    pivot = arr[lb]
    i = lb+1
    for j in range(lb+1,ub+1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i-1], arr[lb] = arr[lb], arr[i-1]
    return i-1    


def Partition_3(arr, lb, ub):         # O(n)
    pivot = arr[ub]
    i = lb - 1
    for j in range(lb, ub):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[ub] = arr[ub], arr[i+1]
    return i+1

def Quick_Sort(arr,lb,ub):
    if lb<ub:
        p=Partition_3(arr,lb,ub)  # p=Partition_1(arr,lb,ub) or p=Partition_2(arr,lb,ub)
        Quick_Sort(arr,lb,p-1)
        Quick_Sort(arr,p+1,ub)

#arr=[]
#arr=[33,11,44,77,55,22,66]
#arr=[77,66,55,44,33,22,11]
arr=[11,22,33,44,55,66,77]
Quick_Sort(arr,0,len(arr)-1)
print(arr)


'''
Time Complexity

Best Case: Pivot chosen, divides list into two nearly equal-sized sub-lists at each recursive step
Average Case: Pivot chosen, divides list into roughly two equal-sized sub-lists at each recursive step

T(n) = 1, n<=1
T(n) = 1 + O(n) + T(n/2) + T(n/2), n>1
     = 2T(n/2) + cn
     = 2[T(n/4) + cn/2] + cn
     = 2T(n/2^2) + 2cn
     ......
     = kT(n/2^k) + kcn

     let n=2^k
Therefore,
T(n) = k + c*n*logn (Base 2)
     = O(nlogn)



Worst Case: When list is either sorted/reversely sorted and pivot chosen as the first/last element

T(n) = 1, n<=1
T(n) = 1 + O(n) + 1 + T(n-1), n>1
     = T(n-1) + cn
     = [T(n-2) + c(n-1)] + cn
     = T(n-2) + c[n+(n-1)]
     ......
     = T(n-k) + c[n+(n-1)+.....+(n-k+1)]

     let n-k=1
Therefore,
T(n) = T(1) + c[n+(n-1)+.....+(n-k+1)]
     = O(n^2)
'''
