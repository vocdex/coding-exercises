## [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/) 
## Description
This problem is an extension of Binary Search problem for 2D matrix. The matrix is sorted in such a way that the first element of each row is greater than the last element of the previous row. The problem is to search for a target element in the matrix. If the target element is found, return True, otherwise return False.

### Trick 1
The matrix row and columns are sorted, so this already hints that we can use Binary Search here.
The way to realize it is by treating the 2D matrix as a 1D array. We can convert the 2D matrix into a 1D array by using the formula:
```python
row = mid // cols
col = mid % cols
```
where cols is the number of columns in the matrix. This allows us to write a member of flattened 1D array as matrix[row][col]. Why do we want this? Because we want to access the value of the mid element in the 1D array and compare it with the target element and we can only do so if we know the row and column index of the mid element.

### Trick 2
The next trick is to use Binary Search to find the target element in the 1D array. The Binary Search algorithm is the same as the one we use for a 1D array. The only difference is that we need to convert the mid index into row and column indexes.

### Trick 3
The last trick is to handle the edge case when the matrix is empty. If the matrix is empty, return False.