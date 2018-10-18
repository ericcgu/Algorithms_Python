# time complexity: O(log n)


def binarysearch(sequence, target):

    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < target:
            low = mid + 1
        elif sequence[mid] > target:
            high = mid - 1
        else:
            return sequence[mid]
    return -1


def binary_search_recursive(sequence, target):

    if len(sequence) == 0:
        return False
    else:
        mid = len(sequence) // 2

        if sequence[mid] == target:
            return True
        else:
            if target < sequence[mid]:
                binary_search_recursive(sequence[:mid], target)
            else:
                binary_search_recursive(sequence[mid:], target)
