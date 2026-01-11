/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    k = 1; 
    for(i= 1; i < nums.length; i++){
        if(nums[i] != nums[i-1]){
            nums[k] = nums[i]
            k ++
        }
    }
    return k // unique elements
    return nums.slice(0,k)  // array with unique elements
    
}

console.log(removeDuplicates([1,1,2])) // [1,2]
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) // [0,1,2,3,4]