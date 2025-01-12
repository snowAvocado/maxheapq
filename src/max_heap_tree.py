"""
max_heap.py

A max-heap implemetation in python.
https://en.wikipedia.org/wiki/max_heap(data_structure)

"""

import copy
import math
from max_heap import *


def print_heap(heap: MaxHeap):
    heap_size = heap.size()
    height_float = math.log(heap_size + 1, 2)
    height = int(math.ceil(height_float))
    final_list = list()
    final_level_len = 2 ** (height - 1)
    initial_list = list()
    i = 0
    while i < final_level_len:
        initial_list.append(2 * i)
        i = i + 1
    final_list.append(initial_list)

    while True:
        new_list = list()
        first_list = final_list[0]
        len_first_list = len(first_list)
        if len_first_list == 1:
            break
        for i in range(0, len_first_list, 2):
            k = (first_list[i] + first_list[i + 1]) / 2
            new_list.append(int(k))
        final_list.insert(0, new_list)

    j = 0
    w = 2 * final_level_len
    for i in range(0, height):
        first_list = final_list[i]
        print_list = list()
        for c in range(0, w):
            if c in first_list:
                if j < n:
                    print_list.append(heap.array[j])
                    j = j + 1
                else:
                    break
            else:
                print_list.append(" ")

        buf_str = str()
        for elem in print_list:
            buf_str = buf_str + str(elem)
        print(buf_str)
