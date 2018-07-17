#selection sort 
#creates a sorted and unsorted. moves the max from the unsorted to the sorted array

my_list = [12, 5, 13, 8, 9, 65]

def selection_sort(array):
    for index, value in enumerate(array):
        #find the minimum element
        minimum = min(array[index:])
        minimum_index = array.index(minimum)
        print(minimum, minimum_index)
        #swap
        array[index],array[minimum_index] = array[minimum_index], array[index]
    return array

print(selection_sort(my_list))

