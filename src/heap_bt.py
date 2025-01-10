"""
max_heap.py

A max-heap implemetation in python.
https://en.wikipedia.org/wiki/max_heap(data_structure)

"""

import copy
import math
from max_heap import *

def print_heap(heap: MaxHeap):
    n = heap.size()
    h = math.log(n+1, 2)
    h = int(math.ceil(h))
    final_list = list()
    final_level_len= 2 ** (h-1)
    initial_list = list()
    i=0
    while i < final_level_len:
        initial_list.append(2*i)
        i = i+1
    final_list.append(initial_list)
    

    while True:
        new_list = list()
        first_list = final_list[0]
        len_first_list = len(first_list)
        if len_first_list == 1:
            break
        for i in range(0,len_first_list,2):
            k = (first_list[i] + first_list[i+1])/2
            new_list.append(int(k))
        final_list.insert(0, new_list)
  
    j = 0
    w = 2 * final_level_len
    for i in range(0,h):
        first_list = final_list[i]
        print_list = list()
        for  c in range(0,w):
            if c in first_list:
                if j < n:
                    print_list.append(heap.array[j])
                    j = j+1
                else :
                    break
            else:
                print_list.append(" ")

        buf_str = str()
        for elem in print_list:
            buf_str = buf_str + str(elem)
        print(buf_str)

if __name__ == "__main__":
    #print_heap(make_heap([9, 7, 4, 1, 2, 3]))
    max_heap1 = make_heap([7, 2, 4, 1, 9, 3])
    max_heap2 = make_heap([7, 1, 0, 4, 2, 3, 6])
    new_merged_heap1 = merge(heap1=max_heap1, heap2=max_heap2)
    print_heap(max_heap1)
    print()
    print_heap(max_heap2)
    print()
    print_heap(new_merged_heap1)