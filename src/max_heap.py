"""
max_heap.py

A max-heap implemetation in python.
https://en.wikipedia.org/wiki/max_heap(data_structure)

"""

import copy

# Supports heap with key type as only int or float
key = int
arr_idx = int


class MaxHeap:

    def __init__(self):
        self.array = []

    def size(self) -> int:
        return len(self.array)

    def is_empty(self) -> bool:
        return len(self.array) == 0

    def find_max(self) -> key:
        try:
            return self.array[0]
        except IndexError:
            raise IndexError("cannot find max on empty heap")

    def insert(self, k: key):
        self.array.append(k)
        self._sift_up(len(self.array) - 1)

    def delete_max(self) -> key:
        try:
            max_key = self.array[0]
            last = self.array.pop()
            self.replace(last)
            return max_key
        except IndexError:
            raise IndexError("cannot pop on empty heap")

    def replace(self, k: key):
        try:
            if k < self.array[0]:
                self.array[0] = k
                self._sift_down()
            else:
                self.array[0] = k
        except IndexError:
            raise IndexError("cannot replace on empty heap, use push instead")

    def _increase_key(self, old_key: key, new_key: key):
        for idx, key in enumerate(self.array):
            if key == old_key:
                self.array[idx] = new_key
                self._sift_up(idx)

    def _decrease_key(self, old_key: key, new_key: key):
        for idx, key in enumerate(self.array):
            if key == old_key:
                self.array[idx] = new_key
                self._sift_down(idx)

    def _delete(self, del_key: key):
        for idx, key in enumerate(self.array):
            if key == del_key:
                last_key = self.array.pop()
                self.array[idx] = last_key
                self._sift_down(idx)

    def _swap_keys(self, i: arr_idx, j: arr_idx):
        t_key = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = t_key

    def _sift_up(self, idx: arr_idx):
        if idx == 0:
            return
        parent_idx = int(idx / 2) if idx % 2 == 1 else int(idx / 2 - 1)
        if self.array[idx] > self.array[parent_idx]:
            self._swap_keys(idx, parent_idx)
            self._sift_up(parent_idx)
        else:
            return

    def _sift_down(self, idx: arr_idx = 0):
        try:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            child_idx = (
                left_idx if self.array[left_idx] >= self.array[right_idx] else right_idx
            )
            if self.array[idx] < self.array[child_idx]:
                self._swap_keys(idx, child_idx)
                self._sift_down(child_idx)

        except IndexError:
            return


"""Operations related to creation of binary heap"""


def create_heap() -> MaxHeap:
    return MaxHeap()


def make_heap(array: list[int]) -> MaxHeap:
    heap = MaxHeap()
    heap.array = array
    len_arr = len(heap.array)
    i = int(len_arr / 2) if len_arr % 2 == 1 else len_arr / 2 - 1
    i = len(heap.array) - 1
    while i >= 0:
        heap._sift_down(i)
        i -= 1
    return heap


# Merge or Union of two heaps,
# heap1 and heap2 are immutable, read-only according to definition
def merge(heap1: MaxHeap, heap2: MaxHeap) -> MaxHeap:
    if heap2.is_empty():
        new_heap = copy.deepcopy(heap1)
        return new_heap
    if heap1.is_empty():
        new_heap = copy.deepcopy(heap2)
        return new_heap
    heap = make_heap(heap1.array + heap2.array)
    return heap


# Meld of two heaps
# create new heap by joining both heaps, heap1 and heap2
# but they should become invalid according to definition
# def meld(heap1: MaxHeap, heap2: MaxHeap) -> MaxHeap:
#     return MaxHeap()
