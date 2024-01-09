list1 = [2,12,4,14,12]
list2 = []
for i in range(0,len(list1),1):
    if list1[i] not in list2:
        list2.append(list1[i])
print(list2)

def remdup1(list1):
    list2 = []
    for num1 in list1:
        if num1 not in list2:
            list2.append(num1)
    return list2
list1 = [2,12,4,14,12]
print(remdup1(list1))


