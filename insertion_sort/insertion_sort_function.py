def insertion_sort_function(arr):
    length = len(arr)
    for i in range(1, length):
        current_value = arr[i]
        position = i
        while position > 0 and current_value < arr[position - 1]:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value


if __name__ == '__main__':
    array = list(map(int, input().split()))
    insertion_sort_function(array)
    for element in array:
        print(element, end=" ")
