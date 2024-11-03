### Heaps

Heaps are a type of binary tree that satisfy the heap property. If it's a max-heap, the key at the root must be the maximum among all keys present in the heap.
If it's a min-heap, the key at the root must be the minimum among all keys present in the heap.

> Whenever a problem statement indicates that you’re looking for **some extreme element**, it’s worthwhile to think about whether a priority queue would be useful.

 - Access max/min element: O(1)
 - Insertion of an element: O(log n)
 - Remove max/min element: O(log n)
 - Heapify: O(n)

Insertion and deletion of elements rely on temporarily violating the heap property and then restoring it. This is done by swapping the element with its parent or child until the heap property is restored.

### Implementation
#### Python 
```python
import heapq
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
print(heap) # [5, 20, 10]
print(heapq.heappop(heap)) # 5
print(heap) # [10, 20]
```
#### Basic Operations
- `heapify(arr)`: Converts the list into a heap.
- `heappush(heap, ele)`: Pushes the element into the heap.
- `heappop(heap)`: Removes and returns the smallest element from the heap.
- `heapreplace(heap, ele)`: Replaces the smallest element with the new element.
- `nlargest(k, heap)`: Returns the k largest elements from the heap.
- `nsmallest(k, heap)`: Returns the k smallest elements from the heap.

#### Binary Tree Representation
Heaps can be represented as binary trees. The root element will be at the root of the tree. The left child of the root will be the left child of the root in the tree and the right child of the root will be the right child of the root in the tree.

#### Array Representation
Implementation of heaps using arrays: The root element will be at Arr[0]. For any given element at position i, its left child is at position 2i + 1 and right child at 2i + 2.
The parent of any element at position i is at position (i - 1) / 2.


#### Applications
Some examples include:
- Getting the kth smallest or largest element in an array.
- Finding the fastest way to get from one point to another in a graph(like Dijkstra's algorithm).

#### LeetCode Problems
- [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
