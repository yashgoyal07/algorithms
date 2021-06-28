def bubble(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection(arr):
    length = len(arr)
    for i in range(length-1):
        maximum = arr[0]
        max_ind = 0
        for j in range(1, length-i):
            if arr[j] > maximum:
                maximum = arr[j]
                max_ind = j
        arr[max_ind], arr[j] = arr[j], arr[max_ind]


def insertion(arr):
    length = len(arr)
    for i in range(1, length):
        current_value = arr[i]
        position = i
        while current_value < arr[position-1] and position > 0:
            arr[position] = arr[position-1]
            position -= 1
        arr[position] = current_value


def merge(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        first_part = arr[:mid]
        second_part = arr[mid:]
        merge(first_part)
        merge(second_part)
        i, j, k = 0, 0, 0
        while i < len(first_part) and j < len(second_part):
            if first_part[i] < second_part[j]:
                arr[k] = first_part[i]
                i += 1
                k += 1
            else:
                arr[k] = second_part[j]
                j += 1
                k += 1

        while i < len(first_part):
            arr[k] = first_part[i]
            i += 1
            k += 1

        while j < len(second_part):
            arr[k] = second_part[j]
            j += 1
            k += 1


def quick(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        pi = i + 1
        quick(arr, low, pi-1)
        quick(arr, pi+1, high)


if __name__ == '__main__':
    array = list(map(int, input().split()))
    # bubble(array)
    # selection(array)
    # insertion(array)
    # merge(array)
    end = len(array) - 1
    start = 0
    quick(array, start, end)
    for element in array:
        print(element, end=' ')
