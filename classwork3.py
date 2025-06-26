import random
random_list = [random.randint(1, 100) for _ in range(15)]

list1 = random_list[0:5]
list2 = random_list[5:10]
list3 = random_list[10:15]

sum1=sum(list1)
sum2=sum(list2)
sum3=sum(list3)

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)

print("largest sum among three lists",max(sum1,sum2,sum3))