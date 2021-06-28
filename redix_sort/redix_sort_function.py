def redix_sort_function(arr):
    maximum = max(arr)
    n = 1
    while maximum // n > 0:
        count = [0 for _ in range(10)]
        for i in range(len(arr)):
            count[((arr[i] // n) % 10)] += 1
        j = 0
        for ind, value in enumerate(count):
            while value > 0:
                arr[j] = ind
                j += 1
                value -= 1
        n *= 10


if __name__ == '__main__':
    array = list(map(int, input().split()))
    redix_sort_function(array)
    for element in array:
        print(element, end=' ')