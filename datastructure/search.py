"""
    Searching algorithms are essential tools in computer science
    used to locate specific items within a collection of data.
    These algorithms are designed to efficiently navigate 
    through data structures to find the desired information, 
    making them fundamental in various applications such as 
    databases, web search engines, and more.
"""

import math


class LinearSearch:
    def linear_search(self, array: list, N: int, key) -> int:
        '''
            :param list array: Array of Elements
            :param int N: Number of elements
            :param key: Element to search

            :return i: Array index of the element

            Linear Search is a method for searching an element in a 
            collection of elements. In Linear Search, each element 
            of the collection is visited one by one in a sequential 
            fashion to find the desired element.
            Linear Search is also known as Sequential Search.
        '''
        for i in range(0, N):
            if array[i] == key:
                return i
        return -1



    def sentinel_linear_search(self, array: list, n: int, key) -> int:
        '''
            :param list array: Array of Elements
            :param int n: Number of elements
            :param key: Element to search

            :return i: Array index of the element

            Sentinel linear search is a variation of the standard 
            linear search algorithm used to find a target value in 
            an array or list. The basic idea behind this algorithm 
            is to add a sentinel value at the end of the array which 
            is equal to the target value we are looking for. This 
            helps to avoid checking the array boundary condition 
            during each iteration of the loop, as the sentinel value 
            acts as a stopper for the loop.
        '''
        # Last element of the array
        last = array[n - 1]

        # Element to be searched is
        # placed at the last index
        array[n - 1] = key
        
        i = 0
        while (array[i] != key):
            i += 1

        # Put the last element back
        array[n - 1] = last

        if ((i < n - 1) or (array[n - 1] == key)):
            return i
        else:
            return -1


class BinarySearch:
    '''
        Binary Search Algorithm is a searching algorithm used 
        in a sorted array by repeatedly dividing the search 
        interval in half. The idea of binary search is to use 
        the information that the array is sorted and reduce 
        the time complexity to O(log N). 
    '''
    def recursive_binary_search(self, array: list, low: int, high:int, key) -> int: 
        '''
            :param list array: Sorted Array of Elements
            :param int low: Left Index of Array
            :param int high: Right Index of Array
            :param key: Element to search

            :return mid: Array index of the element

            Binary search is a search algorithm used to find 
            the position of a target value within a sorted array. 
            It works by repeatedly dividing the search interval 
            in half until the target value is found or the 
            interval is empty. The search interval is halved 
            by comparing the target element with the middle 
            value of the search space.
        '''
        array = sorted(array)
        # Check base case for the recursive function
        if low <= high:  
    
            mid = (low + high) // 2  
    
            # If element is available at the middle itself then return the its index  
            if array[mid] == key:   
                return mid   
        
            # If the element is smaller than mid value, then search moves  
            # left sublist1  
            elif array[mid] > key:   
                return self.recursive_binary_search(array, low, mid - 1, key)
        
            # Else the search moves to the right sublist1  
            else:   
                return self.recursive_binary_search(array, mid + 1, high, key)   
    
        else:   
            # Element is not available in the list1  
            return -1
        
    def iterative_binary_search(self, array: list, N: int, key) -> int:
        '''
            :param list array: Sorted Array of Elements
            :param int N: Number of elements
            :param key: Element to search

            :return int mid: Array index of the element
        '''
        array = sorted(array)
        low = 0
        high = N - 1
        mid = 0

        while low <= high:
            # for get integer result
            mid = (high + low) // 2

            # Check if n is present at mid
            if array[mid] < key:
                low = mid + 1

            # If n is greater, compare to the right of mid
            elif array[mid] > key:
                high = mid - 1

            # If n is smaller, compared to the left of mid
            else:
                return mid

        # element was not present in the list, return -1
        return -1
    
    def meta_binary_search(self, array: list, N: int, key) -> int:
        '''
            :param list array: Sorted Array of Elements
            :param int N: Number of elements
            :param key: Element to search

            :return int pos: Array index of the element
        '''
        array = sorted(array)
        # Set number of bits to represent
        # lg = int(math.log2(n-1)) + 1

        # largest array index
        while ((1 << lg) < N - 1):
            lg += 1

        pos = 0
        for i in range(lg - 1, -1, -1):
            if (array[pos] == key):
                return pos

            # Incrementally construct the
            # index of the target value
            new_pos = pos | (1 << i)

            # find the element in one
            # direction and update position
            if ((new_pos < N) and
                    (array[new_pos] <= key)):
                pos = new_pos

        # if element found return
        # pos otherwise -1
        return (pos if (array[pos] == key) else -1)
    

def ternary_search(array: list, left: int, right: int, key) -> int:
    '''
        :param list array: Sorted Array of Elements
        :param int left: Left Index of Array
        :param int right: Right Index of Array
        :param key: Element to search

        :return mid: Array index of the element

        Ternary search is a search algorithm that is 
        used to find the position of a target value 
        within a sorted array. It operates on the 
        principle of dividing the array into three 
        parts instead of two, as in binary search. 
        The basic idea is to narrow down the search 
        space by comparing the target value with 
        elements at two points that divide the array 
        into three equal parts.
    '''
    array = sorted(array)
    if (right >= left):

        # Find the mid1 and mid2
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if key is present at any mid
        if (array[mid1] == key):
            return mid1

        if (array[mid2] == key):
            return mid2

        # Since key is not present at mid,
        # check in which region it is present
        # then repeat the Search operation
        # in that region
        if (key < array[mid1]):

            # The key lies in between l and mid1
            return ternary_search(array, left, mid1 - 1, key)

        elif (key > array[mid2]):

            # The key lies in between mid2 and r
            return ternary_search(array, mid2 + 1, right, key)

        else:

            # The key lies in between mid1 and mid2
            return ternary_search(array, mid1 + 1, mid2 - 1, key)

    # Key not found
    return -1


def jump_search(array: list, N: int, key) -> int:
    '''
        :param list array: Array of Elements
        :param int N: Number of elements
        :param key: Element to search

        :return prev: Array index of the element

        Like Binary Search, Jump Search is a searching 
        algorithm for sorted arrays. The basic idea is 
        to check fewer elements (than linear search) by 
        jumping ahead by fixed steps or skipping some 
        elements in place of searching all elements.
    '''
    array = sorted(array)
    # Finding block size to be jumped
    step = math.sqrt(N)

    # Finding the block where element is present (if it is present)
    prev = 0
    while array[int(min(step, N)-1)] < key:
        prev = step
        step += math.sqrt(N)
        if prev >= N:
            return -1

    # Doing a linear search for x in block beginning with prev.
    while array[int(prev)] < key:
        prev += 1

        # If we reached next block or end of array, element is not present.
        if prev == min(step, N):
            return -1

    # If element is found
    if array[int(prev)] == key:
        return prev

    return -1


def interpolation_search(array: list, low: int, high: int, key):
    '''
        :param list array: Sorted Array of Elements
        :param int low: Left Index of Array
        :param int high: Right Index of Array
        :param key: Element to search

        :return pos: Array index of the element

        The Interpolation Search is an improvement over 
        Binary Search for instances, where the values in 
        a sorted array are uniformly distributed. 
        Interpolation constructs new data points 
        within the range of a discrete set of known 
        data points. Binary Search always goes to the 
        middle element to check. On the other hand, 
        interpolation search may go to different locations 
        according to the value of the key being searched. 
        For example, if the value of the key is closer to 
        the last element, interpolation search is likely to 
        start search toward the end side.
    '''
    array = sorted(array)
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (low <= high and key >= array[low] and key <= array[high]):

        # Probing the position with keeping
        # uniform distribution in mind.
        pos = low + ((high - low) // (array[high] - array[low]) * (key - array[low]))

        # Condition of target found
        if array[pos] == key:
            return pos

        # If x is larger, x is in right subarray
        if array[pos] < key:
            return interpolation_search(array, pos + 1, high, key)

        # If x is smaller, x is in left subarray
        if array[pos] > key:
            return interpolation_search(array, low, pos - 1, key)
    return -1


def exponential_search(array: list, n: int, key) -> int:
    '''
        :param list array: Array of Elements
        :param int n: Number of elements
        :param key: Element to search

        :return mid: Array index of the element
    '''
    array = sorted(array)
    # IF x is present at first location itself
    if array[0] == key:
        return 0

    # Find range for binary search j by repeated doubling
    i = 1
    while i < n and array[i] <= key:
        i = i * 2

    # Call binary search for the found range
    return BinarySearch.recursive_binary_search(array, i // 2, min(i, n-1), key)


def fibMonaccian_search(array: list, n: int, key) -> int:
    '''
        :param list array: Array of Elements
        :param int n: Number of elements
        :param key: Element to search

        :return i: Array index of the element
    '''
    array = sorted(array)
    # Initialize fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    # fibM is going to store the smallest
    # Fibonacci Number greater than or equal to n
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Marks the eliminated range from front
    offset = -1

    # while there are elements to be inspected.
    # Note that we compare arr[fibMm2] with x.
    # When fibM becomes 1, fibMm2 becomes 0
    while (fibM > 1):

        # Check if fibMm2 is a valid location
        i = min(offset+fibMMm2, n-1)

        # If x is greater than the value at
        # index fibMm2, cut the subarray array
        # from offset to i
        if (array[i] < key):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        # If x is less than the value at
        # index fibMm2, cut the subarray
        # after i+1
        elif (array[i] > key):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        # element found. return index
        else:
            return i

    # comparing the last element with x */
    if (fibMMm1 and array[n-1] == key):
        return n-1

    # element not found. return -1
    return -1


