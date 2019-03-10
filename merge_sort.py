def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        mid = int(len(seq)/2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])

        new_seq = merge_sorted_list(left_half, right_half)
        return new_seq

def merge_sorted_list(sorted_a, sorted_b):
    length_a, length_b = len(sorted_a), len(sorted_b)
    new_sorted_seq = list()
    a = b = 0

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1

    if a <length_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])
    return new_sorted_seq

def test_merge_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    assert merge_sort(seq) == sorted(seq)
