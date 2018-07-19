test = [3, 8, 9, 7, 6]

def solution(A):
    unique = set()
    for item in A:
        if item in unique:
            return item
            unique.add(A)

test = {}
for items in test.values():
    print itme