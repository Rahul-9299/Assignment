nums = list(input("Enter numbers separated by spaces: "))

largest = nums[0]
smallest = nums[0]
for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest number:", largest)
print("Smallest number:", smallest)