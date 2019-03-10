import random
def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):

        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    print seq

def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
                
def test_select_sort():
    seq = list(range(0))
    random.shuffle(seq)
    select_sort(seq)
    assert seq == sorted(seq)
def insert_sort(seq):
    n = len(seq)
    for i in range(1,n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value
        
