# Insertion Sort in Python
# Time Complexity: 
    # best case ->O(n)
    # average case ->O(n^2)
    # worst case ->O(n^2)
# Auxiliary Space: O(1)
# Space: O(n)

def insertion_sort(ele):
    for i in range(1, len(ele)):
        anchor = ele[i]
        j = i - 1
        while j >= 0 and anchor < ele[j]:
            ele[j+1] = ele[j]
            j = j - 1
        ele[j+1] = anchor

if __name__ == '__main__':
    tests = [
        [11,10,4,2,88],
        [],
        [4,9,66,0,44],
        [451,452,453,454],
        [1]
    ]
    for ele in tests:
        insertion_sort(ele)
        print(ele)