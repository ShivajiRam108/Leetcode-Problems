/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    let res = 0;
    for(let i of s){
        res ^= i.charCodeAt(0);
    }
    for(let j of t){
        res ^= j.charCodeAt(0);
    }
    return String.fromCharCode(res);
}
console.log(findTheDifference("abcd","abcde"))