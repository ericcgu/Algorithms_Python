#insertion sort 
#starts with a sorted array of one item and loops through array grabs the values and inserts
#into the sorted array
#Best: O(N), Worst:O(N^2)
my_list = [12, 5, 13, 8, 9, 65]

def insertion_sort(array):
    for index, value in enumerate(array):
        current_value = array[index]
        position = index

        while position > 0 and array[position-1] > current_value:
            array[position] = array[position-1] #shifting all elements
            position -= 1 
        array[position] = current_value
    return array

print(insertion_sort(my_list))