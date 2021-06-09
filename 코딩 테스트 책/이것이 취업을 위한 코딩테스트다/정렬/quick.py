


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start

    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left +=1
            
        while right > start  and array[right] >= array[pivot]:
            right -= 1


        if left >  right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        


        