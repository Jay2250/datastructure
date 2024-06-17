'''
    A Sorting Algorithm is used to rearrange a given 
    array or list of elements according to a comparison 
    operator on the elements. The comparison operator 
    is used to decide the new order of elements in the 
    respective data structure.
'''

def selection_sort(array: list, N: int) -> list:
    '''
        :param list array: Array of elements
        :param N: Number of elements

        :return list array: Sorted Array of elements
    '''
    
    for i in range(N-1):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, N):
            if array[min_idx] > array[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


def bubble_sort(arr: list, N: int) -> list:
    '''
        :param list arr: Array of elements
        :param N: Number of elements

        :return list arr: Sorted Array of elements
    '''
    # Traverse through all array elements
    for i in range(N):
        swapped = False

        # Last i elements are already in place
        for j in range(0, N-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    
    return arr


def insertion_sort(arr: list, N:int) -> list:
    '''
        :param list arr: Array of elements
        :param N: Number of elements

        :return list arr: Sorted Array of elements
    '''
    # Traverse through 1 to len(arr)
    for i in range(1, N):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(array: list) -> list:
    '''
        :param list array: Array of elements

        :return list array: Sorted Array of elements
    '''
    if len(array) > 1:
        mid = len(array) // 2  # Finding the mid of the array
        left = array[:mid]  # Dividing the array elements
        right = array[mid:]  # into 2 halves

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        #  data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


def quicksort(arr: list):
    '''
        :param list arr: Array of elements

        :return list array: Sorted Array of elements

        Quick Sort with first element as Pivot element.
    '''
    if len(arr) <= 1:

        return arr

    else:

        pivot = arr[0]

        left = [x for x in arr[1:] if x < pivot]

        right = [x for x in arr[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)


