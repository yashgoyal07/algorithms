def count_sort_function(arr):
    maximum = max(arr)
    count = [0 for _ in range(maximum+1)]
    for i in range(len(arr)):
        count[arr[i]] += 1
    index = 0
    for ind, element in enumerate(count):
        while element > 0:
            arr[index] = ind
            index += 1
            element -= 1


if __name__ == '__main__':
    array = list(map(int, input().split()))
    count_sort_function(array)
    for item in array:
        print(item, end=' ')
