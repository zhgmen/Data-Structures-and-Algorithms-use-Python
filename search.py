def linear_search(value,iterable):
    for key,value in enumerate(iterable):
        if value == value:
            return key

    return -1

def linear_search_recusive(array, value):
    if len(array) == 0:
        return -1
    index = len(array-1)
    if array[index] == value:
        return index
    return linear_search_recusive(array[:index],value)

def binary_search(sorted_array, value):
    if not sorted_array:
        return -1
    beg = 0
    end = len(sorted_array)-1
    mid = int((beg+end)/2)
    if sorted_array[mid] == value:
        return mid
    elif sorted_array[mid] > value:
        end = mid - 1
    else:
        beg = mid + 1

def binary_search(sorted_array, beg, end, val):
    if beg >= end:
        return -1
    mid = int((beg+end)/2)
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        binary_search(sorted_array,beg,mid-1,val)
    else:
        binary_search(sorted_array,mid+1,end,val)

