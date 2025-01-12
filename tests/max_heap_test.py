import unittest
import src.maxheapq.max_heap as max_heap


# Test case class
class TestMaxHeap(unittest.TestCase):
    def test_create_heap(self):
        max_heap1 = max_heap.create_heap()
        self.assertEqual(max_heap1.size(), 0)
        self.assertTrue(max_heap1.is_empty())

    def test_make_heap(self):
        max_heap1 = max_heap.make_heap([7, 2, 4, 1, 9, 3])
        self.assertEqual(max_heap1.size(), 6)
        self.assertFalse(max_heap1.is_empty())
        self.assertEqual(max_heap1.array, [9, 7, 4, 1, 2, 3])

    def test_heap_operations(self):
        max_heap1 = max_heap.make_heap([7, 2, 4, 1, 9, 3])

        max_heap1.insert(5)  # key < root
        self.assertEqual(max_heap1.array, [9, 7, 5, 1, 2, 3, 4])

        max_heap1.delete_max()
        self.assertEqual(max_heap1.array, [7, 4, 5, 1, 2, 3])

        max_heap1.insert(10)  # key > root
        self.assertEqual(max_heap1.array, [10, 4, 7, 1, 2, 3, 5])

        self.assertEqual(max_heap1.size(), 7)
        self.assertFalse(max_heap1.is_empty())

        max_heap1.replace(0)
        self.assertEqual(max_heap1.array, [7, 4, 5, 1, 2, 3, 0])

        max_heap1.increase_key(0,10)
        self.assertEqual(max_heap1.find_max(), 10)
        self.assertEqual(max_heap1.array, [10, 4, 7, 1, 2,3,5])

        max_heap1.decrease_key(10,0)
        self.assertEqual(max_heap1.find_max(), 7)
        self.assertEqual(max_heap1.array, [7, 4, 5, 1, 2, 3, 0])

        max_heap2 = max_heap.make_heap([7, 2, 4, 1, 9, 3, 9])
        max_heap2.delete(9)
        self.assertEqual(max_heap2.size(), 5)
        self.assertEqual(max_heap2.array, [7, 3, 4, 1, 2])

        max_heap3 = max_heap.make_heap([9, 9, 9, 1, 9, 9, 9])
        max_heap3.delete(9)
        self.assertEqual(max_heap3.size(), 1)
        self.assertEqual(max_heap3.array, [1])

    def test_merge_heap(self):
        max_heap1 = max_heap.make_heap([7, 2, 4, 1, 9, 3])
        max_heap2 = max_heap.make_heap([-7, -1, 0, -4, -2, -3, 6])
        new_merged_heap1 = max_heap.merge(heap1=max_heap1, heap2=max_heap2)
        self.assertEqual(new_merged_heap1.size(), 13)
        self.assertEqual(new_merged_heap1.find_max(), 9)

        self.assertEqual(max_heap1.array, [9, 7, 4, 1, 2, 3])
        self.assertEqual(max_heap2.array, [6, -1, 0, -4, -2, -3, -7])
        self.assertEqual(
            new_merged_heap1.array, [9, 7, 6, 1, 2, 3, 4, -1, 0, -4, -2, -3, -7]
        )

        new_merged_heap2 = max_heap.merge(heap1=max_heap2, heap2=max_heap1)
        self.assertEqual(new_merged_heap2.size(), 13)
        self.assertEqual(new_merged_heap2.find_max(), 9)
        self.assertEqual(
            new_merged_heap2.array, [9, 7, 3, 6, 4, 2, -7, -4, -1, -2, 1, 0, -3]
        )


if __name__ == "__main__":
    unittest.main()
