# this is a program to show bubble sort

def bubble_sort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == '__main__':
    array = list(map(int, input().split()))
    bubble_sort(array)
    for element in array:
        print(element, end=" ")
