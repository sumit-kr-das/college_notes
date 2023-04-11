def linear_search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1


if __name__ == "__main__":
    arr = [5, 40, 7, 12, 55]
    ele = 70
    print(linear_search(arr, ele))