import sys

array = [20,5,21,6,23,7,34,999,56]

def selectionSort(array):
    for i in range(len(array)):
        ixDes = i
        for j in range(i+1,len(array)):
            if array[ixDes]>array[j]: #compare if index one of the array with all the elements of the array
                ixDes=j #now the index will have the value of the last element in the array used to compare
        array[i], array[ixDes] = array[ixDes], array[i] #swap

selectionSort(array)
print("Sorted array: ")
for i in range(len(array)):
    print("%d" %array[i]),