class Solution {
    maxSubarraySum(arr) {
        let max1 = -Infinity
        let max2 = 0 
        for(var i = 0; i < arr.length; i++){
            max2 += arr[i]
            if(max1 > max2){
                max2 = max1
            }
            if(max2 < 0){
                max2 = 0
            }
        }
        return max2
        
    }
}
let x = new Solution()
console.log(x.maxSubarraySum([2, 3, -8, 7, -1, 2, 3])) // 11
console.log(x.maxSubarraySum([-2,-4])); // 0
console.log(x.maxSubarraySum([5, 4, 1, 7, 8])); // 25


// Time Complexity: O(n)
// Space Complexity: O(1)
