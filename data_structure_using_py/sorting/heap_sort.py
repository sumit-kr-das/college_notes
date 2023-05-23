def heapify(ll, n, i):
	max_indx = i 
	lc = 2 * i + 1
	rc = 2 * i + 2

	if lc < n and ll[i] < ll[lc]:
		max_indx = lc

	if rc < n and ll[max_indx] < ll[rc]:
		max_indx = rc

	if max_indx != i:
		(ll[i], ll[max_indx]) = (ll[max_indx], ll[i])
		heapify(ll, n, max_indx)


def Heap_Sort(ll):
	n = len(ll)
	for i in range(n // 2 - 1, -1, -1): # From first non_leaf node
		heapify(ll, n, i)

	for i in range(n - 1, 0, -1):
		ll[i], ll[0] = ll[0], ll[i]
		heapify(ll, i, 0)


ll = [11,22,33,44,55,66,77,88,99]
h=Heap_Sort(ll)
print("Sorted List",ll)

