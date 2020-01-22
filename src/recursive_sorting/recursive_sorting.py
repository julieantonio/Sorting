# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    # starting at beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            # merged_arr.append(arrA.pop(0))
            merged_arr.append(arrA[0])
            # instead of pop, maybe better slice?
            arrA = arrA[1:]
        else:
            #merged_arr.append(arrB.pop(0))
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
    if len(arrA) == 0:
        for x in arrB:
            merged_arr.append(x)
        # [merged_arr.append(x) for x in arrB]
    else:
        [merged_arr.append(x) for x in arrA]

    return merged_arr

# print(merge([1, 3, 5, 67, 89], [2, 4, 24, 35, 52, 100]))
import profile
# profile.run('merge([1, 3, 5, 67, 89], [2, 4, 24, 35, 52, 100])')

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    half = len(arr)//2
    rhs = arr[:half]
    lhs = arr[half:]
    if len(arr) == 1:
        return arr
    return merge(merge_sort(lhs), merge_sort(rhs))

print(merge_sort([5, 10, 6, 72, 55, 22, 3]))
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
