/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let n = x.toString()
    let left  = 0 
    let right = n.length - 1
    while(left < right){
        if(n[left] != n[right]){
            return false
        }
        left += 1
        right -= 1

    }
    return true 
}

console.log(isPalindrome(121)) // true
console.log(isPalindrome(-121)) // false
console.log(isPalindrome(10)) // false


