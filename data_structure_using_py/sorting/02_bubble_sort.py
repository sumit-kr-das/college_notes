# Bubble Sort in Python
# Time Complexity: 
    # best case -> O(n)
    # average case -> O(n^2)
    # worst case -> O(n^2)
# Auxiliary Space: O(1)
# Space: O(n)

def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    tests = [
        [11,10,4,2,88],
        [],
        [4,9,66,0,44],
        [451,452,453,454],
        [1]
    ]
    for ele in tests:
        bubble_sort(ele)
        print(ele)