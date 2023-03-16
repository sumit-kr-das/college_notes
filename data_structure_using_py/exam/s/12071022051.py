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
        [11,66,44, 55, 22, 33, 88, 99, 77],
        [11,22,33,44,55]
    ]
    for ele in tests:
        insertion_sort(ele)
        print(ele)