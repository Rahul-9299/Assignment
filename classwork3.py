import random

random_list = [random.randint(1, 100) for _ in range(15)]

list1 = random_list[0:5]
list2 = random_list[5:10]
list3 = random_list[10:15]

sum1 = sum(list1)
sum2 = sum(list2)
sum3 = sum(list3)

print("List 1:", list1, "Sum:", sum1)
print("List 2:", list2, "Sum:", sum2)
print("List 3:", list3, "Sum:", sum3)

if sum1 >= sum2 and sum1 >= sum3:
    print(f"Largest sum is {sum1} and it is in List 1")
elif sum2 >= sum1 and sum2 >= sum3:
    print(f"Largest sum is {sum2} and it is in List 2")
else:
    print(f"Largest sum is {sum3} and it is in List 3")
