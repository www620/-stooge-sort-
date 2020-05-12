def s_sort(list0, left, right):
	if left + 2 > right:
		if list0[left] > list0[right]:
			list0[left], list0[right] = list0[right], list0[left]
		return list0
	n = (right - left + 1) // 3
	list0 = s_sort(list0, left, right - n)
	list0 = s_sort(list0, left + n, right)
	list0 = s_sort(list0, left, right - n)
	return list0

def stooge_sort(list0):
	return s_sort(list0, 0, len(list0) - 1)