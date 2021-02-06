def merge_sort_function(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        first_part = arr[:mid]
        second_part = arr[mid:]
        merge_sort_function(first_part)
        merge_sort_function(second_part)
        i = 0
        j = 0
        k = 0
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


if __name__ == '__main__':
    array = list(map(int, input().split()))
    merge_sort_function(array)
    for element in array:
        print(element, end=' ')
    print()

