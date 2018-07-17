#bubble sort 
#bubbles the largest value to the top

my_list = [12, 5, 13, 8, 9, 65]

def bubble_sort(arrayay):
    sorted = False
    length = len(arrayay)-1
    while not sorted:
        sorted = True
        for index, value in enumerate(array[:length]):
            if array[index] > array[index+1]:
                sorted = False
                array[index], array[index+1] = array[index+1], array[index]
    return array
    
print(bubble_sort(my_list))