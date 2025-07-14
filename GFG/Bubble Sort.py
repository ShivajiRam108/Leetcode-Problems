class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr 
x = Solution()
print(x.bubbleSort([64, 34, 25, 12, 22, 11, 90]))  # Output: [11, 12, 22, 25, 34, 64, 90]
print(x.bubbleSort([5, 1, 4, 2, 8]))  # Output: [1, 2, 4, 5, 8]
print(x.bubbleSort([3, 0, 2, 5, -1, 4, 1]))  # Output: [-1, 0, 1, 2, 3, 4, 5]