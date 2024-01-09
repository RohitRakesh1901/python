list1 = [2,4,6,8,8]
set1 = set(list1)
list2 = list(set1)
print(list1)
print(set1)
print(list2)
list2.sort()
print(list2)
print()

list1 = [2,12,4,14,12]
array = []
[array.append(x)for x in list1 if x not in array]
print(array)

