# Selection Sort in Python
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
# Space: O(n)

def selection_sort(arr):
    size = len(arr)
    # if array is empty
    if (size == 0):
        return
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        # if i is already min value, then dont swap
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    tests = [
        [11,10,4,2,88],
        [],
        [4,9,66,0,44],
        [451,452,453,454],
        [1]
    ]
    for ele in tests:
        selection_sort(ele)
        print(ele)
