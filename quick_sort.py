def quick_sort(array):
    size = len(array)
    if size < 2:
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(1,size) if array[i] <= pivot and pivot_idx != i]
    large_part = [array[i] for i in range(1,size) if array[i] > pivot and pivot_idx != i]
    return quick_sort(less_part) + [pivot] + quick_sort(large_part)

    
    
def test_quick_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    assert quick_sort(seq) == sorted(seq)

def quicksort_inplace(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot+1, end)
def partition(array, beg, end):
    pivot_i = beg
    pivot = array[pivot_i]
    left = beg + 1
    right = end - 1
    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while right >= left and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[pivot_i], array[right] = array[right], array[pivot_i]
    return right

def test_partition():
    assert partition([2,5,7,1,3],0,5) == 1
    assert partition([1,2,3,4], 0, 4) == 0
    assert partition([4,3,2,1],0,4)== 3


'''
2,5,7,1,3
2,1,7,5,3
1,2,7,5,3
1,2,3,5,7



4,3,2,1
1,3,2,4

1,2,3,4
'''
def test_quicksort_inplace():
    l = [4,2,6,4,7,5,7,1,8]
    #assert quicksort_inplace(l,0,9) == sorted(l)
    quicksort_inplace(l,0,9)
    assert l == sorted(l)
'''

[1,2,3,4]

