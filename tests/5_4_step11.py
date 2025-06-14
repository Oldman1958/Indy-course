"""
На вход программе поступает список из целых чисел.
Ваша задача — вывести True, если элементы в списке отсортированы по неубыванию.
В противном случае выведите False.
"""

nums = list(map(int, input().split()))
flag = True
for i in range(1, len(nums)):
    if nums[i - 1] > nums[i]:
        flag = False
        break
print(flag)
