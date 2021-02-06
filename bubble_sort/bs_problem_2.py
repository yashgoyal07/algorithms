
def bubble_sort_ind_arr(arr):
    length = len(arr)
    ind_arr = [i for i in range(length)]
    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ind_arr[j], ind_arr[j+1] = ind_arr[j+1], ind_arr[j]
    return ind_arr


len_ = int(input())
array = list(map(int, input().split()))

result = bubble_sort_ind_arr(array)

for element in result:
    print(element, end=" ")


