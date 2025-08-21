class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j + 1 ] = key 
        return arr 
x = Solution()
print(x.insertionSort([12, 11, 13, 5, 6]))  # Output: [5, 6, 11, 12, 13]
print(x.insertionSort([5, 2, 9, 1, 5, 6]))   # Output: [1, 2, 5, 5, 6, 9]
print(x.insertionSort([3, 0, 2, 5, -1, 4, 1]))  # Output: [-1, 0, 1, 2, 3, 4, 5]
print(x.insertionSort([4, 3, 2, 1]))  # Output: [1, 2, 3, 4]
print(x.insertionSort([1, 2, 3, 4]))  # Output: [1, 2, 3, 4]
print(x.insertionSort([]))  # Output: []