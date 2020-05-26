arr = [3,22,17,1,40,8,31,137, 12, 4, 19, 20, 2, 9]
#		  -	      -                       -

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( first, last ):
	# elements = len( arrA ) + len( arrB )
	# merged_arr = [0] * elements
	# # TO-DO
	combined = []
	put = None
	while len(first) > 0 and len(last) > 0:
		if first[0] < last[0]:
			combined.append(first[0])
			del first[0]
		else:
			combined.append(last[0])
			del last[0]

	if len(first):
		combined.extend(first)
		del first[0]
	elif len(last):
		combined.extend(last)
		del last[0]

	return combined


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

	# half = arr[len(arr)//2]

	if len(arr) <= 1:
		return arr

	first = merge_sort(arr[:len(arr)//2])
	last = merge_sort(arr[len(arr)//2:])

	return merge(first, last)

# print(len(arr))
# print(len(merge_sort(arr)))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
	# TO-DO

	return arr

def merge_sort_in_place(arr, l, r): 
	# TO-DO

	return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

	return arr
