def quickSort(array):
    if len(array)<= 1:
        return array
    pivot=array[-1]
    i=0
    while (array[i]!=pivot) or (pivot in array[i+1:]):
        if array[i]>pivot:
            array.append(array.pop(i))
        else:
            i+=1
    return quickSort(array[:i])+[pivot]+quickSort(array[i+1:])

print(quickSort([1,2,3,4,5,6,7,8,9]))
