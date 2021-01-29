# https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/min-max-difference/

from bubble_sort.bubble_sort_function import bubble_sort

t = int(input())
while t:
    length, number = map(int, input().split())
    arr = list(map(int, input().split()))
    bubble_sort(arr)
    diff = length - number
    result = sum(arr[number:]) - sum(arr[:diff])
    print(result)
    t -= 1
