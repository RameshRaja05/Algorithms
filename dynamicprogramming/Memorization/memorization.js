function addto80(n){
    return n+80
}
function memorize(n){
    let cache={}
    return (function(n){
        if(n in cache){
            return cache[n]
        }
        else{
            console.log("it takes")
            cache[n]=n+80
            return cache[n]
        }
    })
}
let mem=memorize()
console.log(mem(5))
console.log(mem(5))