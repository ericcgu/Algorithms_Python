#time complexity: O(log n) 

def binarysearch(sequence, value):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < value:
            low = mid + 1
        elif value < sequence[mid]:
            high = mid - 1
        else:
            return sequence[mid]
    return -1

def binary_search_recur(seq, val):
    if len(arr) == 0:
        return False
    else:
        mid = len(seq) // 2

        if seq[mid] == val:
            return True
        else:
            if val < seq[mid]:
                binary_search_recur(seq[:mid], val)
            else:
                binary_search_recur(seq[mid:], val)
