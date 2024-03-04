target = int(input())
list_1 = [1, 4, 5, 6, 7, 8, 9, 10, 11]


# def binary():
sorted(list_1)
length = len(list_1)
left = 0
right = length - 1
while left <= right:
    mid = (right - left) // 2 + left
    if target == list_1[mid]:
        print(mid)
        break
    elif target < list_1[mid]:
        right = mid - 1
    elif target > list_1[mid]:
        left = mid + 1
    else:
        print("Эдеменет не найден")
