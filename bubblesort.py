#1.- compare elements
#2.- repeat until no swaps are required 

def bubbleSort(array):
    n=len(array) #an array with n ammount of numbers

    for i in range(n): #for every element in the array
        swap = False
        print(array)
        for j in range(0,n-i-1): 
            if array[j]>array[j+1]: #compare every elemenent of the array to the one next to it
                array[j],array[j+1]=array[j+1],array[j] #if it's bigger, swap them
                swap = True
        if not swap: break #stop when there's no more swaps
array = [190,1200,1,2,4,55,1000,6,800]

bubbleSort(array)

