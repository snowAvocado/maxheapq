# maxheapq

This project implements heap data structure, specifically **max binary heap** described on [wikipedia](https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap)

The purpose is to implement my own version and compare with 
already existing [heapq](https://docs.python.org/3/library/heapq.html), by default **heapq** implements min heap but we implement max heap here, hence the name **maxheapq**


in max heap, the element with highest priority or value will be at the first index of the underhood array, which can be seen as a complete binary tree, where **i** is index of Parent, with indices **2 * i+ 1**, **2 * i+ 2** as children of the parent

Some basic operations or usage:
```

heap = max_heap.make_heap([7, 2, 4, 1, 9, 3]) 
[9, 7, 4, 1, 2, 3]


print(heap)

   9    
 7   4  
1 2 3 


heap.find_max()
9

heap.insert(5)  
[9, 7, 5, 1, 2, 3, 4]

heap.delete_max()
[7, 4, 5, 1, 2, 3]

heap.insert(10)
[10, 4, 7, 1, 2, 3, 5]

heap.size() ==  7
True

heap.is_empty()
False

heap.replace(0)
[7, 4, 5, 1, 2, 3, 0]

```