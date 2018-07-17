#bubble sort 
#bubbles the largest value to the top

my_list = [12, 5, 13, 8, 9, 65]

def bubble_sort(arr):
    sorted = True
    length = len(arr)-1
    while not sorted:
        sorted = True
        for index, value in enumerate(arr[:length]):
            if arr[index] > arr[index+1]:
                sorted = False
                arr[index], arr[index+1] = arr[index+1], arr[index]
    return arr
    
print(bubble_sort(my_list))
