def binary_search(arr, ele):
    start = 0
    end = len(arr) - 1
    mid = 0
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    arr = [3, 4, 5, 6, 7]
    ele = 7
    print(binary_search(arr, ele))
