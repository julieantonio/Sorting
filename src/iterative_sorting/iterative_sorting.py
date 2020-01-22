# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(arr1)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        iter = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                iter = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if iter == False:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr