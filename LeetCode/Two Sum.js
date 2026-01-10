/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // two pointer approach
   let left = 0 ; 
   let right = nums.length - 1; 
   for(let i = 0 ; i < nums.length-1; i++){
    for(let j = i+ 1; j < nums.length; j ++){
        if(nums[i] + nums[j] == target){
            return [i, j];
        };
    };
   };
 
};

// heap map approach
var twoSum = function(nums, target) {
    const numMap = new Map();
    for(let i = 0; i < nums.length; i++){
        const complement = target - nums[i];
        if(numMap.has(complement)){
            return [numMap.get(complement), i];
        }
        numMap.set(nums[i], i);

    }
    return [ -1, -1 ];
};





console.log(twoSum([2,7,11,15], 9)) // [0, 1]
console.log(twoSum([3,2,4], 6)) // [1, 2]
console.log(twoSum([3,3], 6)) // [0, 1]