function o(a){
    a=20;
    return function(){
        console.log(a);
    }
}
let s=o(10);
console.log(s);