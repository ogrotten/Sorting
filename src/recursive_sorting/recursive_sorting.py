arr = [3,22,17,1,40,8,31,137, 12, 4, 19, 20, 2, 9]

print(len(arr),len(arr)//2)
print(arr[:len(arr)//2])
print(arr[len(arr)//2:])

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
	elements = len( arrA ) + len( arrB )
	merged_arr = [0] * elements
	# TO-DO
	
	return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

	half = arr[:len(arr)//2]

	if len(arr) == 1:
		return arr
		# print(arr, end = " ")

	first = merge_sort(arr[:len(arr)//2])
	last = merge_sort(arr[len(arr)//2:])

	print(arr)

	return arr

merge_sort(arr)

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
