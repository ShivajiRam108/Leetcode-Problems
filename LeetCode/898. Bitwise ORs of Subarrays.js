/**
 * @param {number[]} arr
 * @return {number}
 */
var subarrayBitwiseORs = function(arr) {
    let res = new Set()
    let prev = new Set()
    for(let i of arr){
        let cur = new  Set()
        cur.add(i)
        for(let j of prev){
            cur.add(j | i)
        }
        for(let k of cur){
            res.add(k)
        }
        prev = cur 
    }
    return res.size;
}
console.log(subarrayBitwiseORs([0])) // 1
console.log(subarrayBitwiseORs([1,1,2])) // 3
console.log(subarrayBitwiseORs([1,2,4])) // 6 
