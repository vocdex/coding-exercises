
def heap_playground():
    # heapq is a binary heap implementation with min-heap property.
    # heapify() function is used to convert a regular list to a heap. It is done in-place.
    import heapq
    list1 = [10,19,25,5,4,12]
    heapq.heapify(list1)
    print(list1) # [4, 5, 12, 19, 10, 25]
    heapq.heappush(list1, 2)
    print(list1) # [2, 5, 4, 19, 10, 25, 12]
    heapq.heappop(list1)
    print(list1) # [4, 5, 12, 19, 10, 25]

def topKFrequent(nums, k):
    """
    Given a non-empty array of integers, return the k most frequent elements.
    """
    from collections import Counter
    from heapq import heappush, heappop
    counts = Counter(nums)
    min_heap = []
    for num, freq in counts.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)
    top_k_frequent = [num for freq, num in min_heap]
    return top_k_frequent

def findKthLargest(nums, k):
    import heapq
    # Keep min_heap list of size k. If the size is bigger than k, pushpop new element
    min_heap = []

    for num in nums:
        if len(min_heap)<k:
            heapq.heappush(min_heap,num)
        else:
            heapq.heappushpop(min_heap,num)
    return min_heap[0]


    
if __name__ == "__main__":
    # nums = [1,1,1,2,2,3,3,3,3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    # k = 2
    # print(topKFrequent(nums, k)) # [1, 2]
    nums = [3,2,1,5,6,4]
    k = 1
    print(findKthLargest(nums,k))
    