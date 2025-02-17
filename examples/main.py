from maxheapq import max_heap

# from maxheapq_snow import max_heap_tree

# create an empty max heap
heap = max_heap.create_heap()

print(heap.array)  # []
print(heap.size())  # 0
print(heap.is_empty())  # True

# make a heap from a int list
heap = max_heap.make_heap([7, 2, 4, 1, 9, 3])

print(heap.array)  # [9, 7, 4, 1, 2, 3]
print(heap.size())  # 6
print(heap.is_empty())  # False

# max_heap_tree.print_bt(heap)

#    9
#  7   4
# 1 2 3

# insert and delete_max
heap.insert(5)  # key < root
print(heap.array)  # [9, 7, 5, 1, 2, 3, 4]
# max_heap_tree.print_bt(heap)
#    9
#  7   5
# 1 2 3 4

heap.delete_max()
print(heap.array)  # [7, 4, 5, 1, 2, 3]
# max_heap_tree.print_bt(heap)
#    7
#  4   5
# 1 2 3

heap.insert(10)  # key > root
print(heap.array)  # [10, 4, 7, 1, 2, 3, 5]
# max_heap_tree.print_bt(heap)

#    10
#  4   7
# 1 2 3 5

# replaces the root key of max heap
heap.replace(0)
print(heap.array)  # [7, 4, 5, 1, 2, 3, 0]
# max_heap_tree.print_bt(heap)

#    7
#  4   5
# 1 2 3 0

# increase key method below find all keys with 0 and replace it with 10
# in the heap
heap.increase_key(0, 10)
print(heap.find_max())  # 10
print(heap.array)  # [10, 4, 7, 1, 2,3,5]
# max_heap_tree.print_bt(heap)

#    10
#  4   7
# 1 2 3 5


# decrease key method below find all keys with 10 and replace it with 0
# in the heap
heap.decrease_key(10, 0)
print(heap.find_max())  # 7
print(heap.array)  # [7, 4, 5, 1, 2, 3, 0]
# max_heap_tree.print_bt(heap)

#    7
#  4   5
# 1 2 3 0

# delete deletes all keys with value 9
heap = max_heap.make_heap([7, 2, 4, 1, 9, 3, 9])
heap.delete(9)
print(heap.size())  # 5
print(heap.array)  # [7, 3, 4, 1, 2]
# max_heap_tree.print_bt(heap)

#    7
#  3   4
# 1 2

heap = max_heap.make_heap([9, 9, 9, 1, 9, 9, 9])
heap.delete(9)
print(heap.size())  # 1
print(heap.array)  # [1]
# max_heap_tree.print_bt(heap)

# 1

# merge two heaps
heap1 = max_heap.make_heap([7, 2, 4, 1, 9, 3])
# max_heap_tree.print_bt(heap1)

#    9
#  7   4
# 1 2 3

heap2 = max_heap.make_heap([-7, -1, 0, -4, -2, -3, 6])
# max_heap_tree.print_bt(heap2)

#    6
#  -1   0
# -4 -2 -3 -7

new_merged_heap = max_heap.merge(heap1, heap2)
# max_heap_tree.print_bt(new_merged_heap)

#                  9
#         7                      6
#   1          2          3          4
# -1    0    -4    -2    -3    -7
