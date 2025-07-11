set1={1,2,3,4,5}
set2={4,5,6,7,8}

#method: add
set1.add(6)
print("After adding 6 to set1:", set1)

#method: remove
set1.remove(1)
print("After removing 1 from set1:", set1)

#method: union
set_union = set1.union(set2)
print("Union of set1 and set2:", set_union)

#method: pop
popped_element = set1.pop()
print("Popped element from set1:", popped_element)

#method: update
set1.update({9, 10})
print("After updating set1 with {9, 10}:", set1)