### 703. Kth Largest Element in a Stream

This problem asks us to design a class that can find the kth largest element in a stream of integers. The class should have an `add` method that adds an integer to the stream and a `kthLargest` method that returns the kth largest element in the stream.

#### Approach
The first thing that comes to mind is to use a heap to store the k largest elements in the stream. We can use a min heap to store the k largest elements. The min heap will store the k largest elements in the stream and the top element of the min heap will be the kth largest element in the stream.

Remember min-heap top element is the smallest element in the heap. So, if the heap size is k, the top element will be the kth largest element in the stream.

The first list given is used for constructing the heap. We cannot simply heapify this list because the list size can be greater than k. So, we need call "add" method for each element in the list.
Code:
```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums: 
            self.add(num) # Call add method for each element in the list

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val) # if heap size is less than k, keep pushing elements
        else:
            heapq.heappushpop(self.min_heap, val) # if heap size is equal to k, push and pop the top element. Remember, top element is the smallest element in the heap and we exactly want that top element.
        return self.min_heap[0]
```

#### Complexity Analysis
The time complexity for adding an element to the heap is O(log k) and the space complexity is O(k).
