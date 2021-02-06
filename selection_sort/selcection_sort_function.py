def selection_sort(arr):
    length = len(arr)
    for i in range(length-1):
        maximum = float('-inf')
        for j in range(length-i):
            if arr[j] > maximum:
                maximum = arr[j]
                max_ind = j
        arr[max_ind], arr[j] = arr[j], arr[max_ind]


if __name__ == '__main__':
    array = list(map(int, input().split()))
    selection_sort(array)
    for element in array:
        print(element, end=' ')
