def quick_sort_function(arr, start, end):
    if start < end:
        i = -1
        pivot = arr[end]
        for j in range(end):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[end] = arr[end], arr[i+1]
        pi = i+1
        quick_sort_function(arr, start, pi-1)
        quick_sort_function(arr, pi+1, end)


if __name__ == '__main__':
    array = list(map(int, input().split()))
    length = len(array)-1
    quick_sort_function(array, start=0, end=length)
    for element in array:
        print(element, end=' ')
