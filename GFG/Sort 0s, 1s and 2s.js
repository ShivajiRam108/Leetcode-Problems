class Solution {
    // Function to sort an array of 0s, 1s, and 2s
    sort012(arr) {
        let left = 0 
        let mid = 0 
        let right = arr.length - 1
        while (mid <= right){
            if (arr[mid] == 0){
                [arr[left], arr[mid] ] = [arr[mid], arr[left]]
                left ++ 
                mid ++
            }else if(arr[mid] == 1){
                mid ++
            }else{
                [arr[mid], arr[right]] = [arr[right], arr[mid]]
                right --
            }
        }
        return arr
        
    }
}
let sort = new  Solution()
console.log(sort.sort012([0, 1, 2, 0, 1, 2])) // [0, 0, 1, 1, 2, 2]
console.log(sort.sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))  //  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
