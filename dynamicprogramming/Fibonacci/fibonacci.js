let calc=0
function dpfibonacci(n){
    let cache={0:0,1:1,2:1}
    return function fib(n){
        if(n in cache){
            return cache[n]
        }
        else{
            cache[n]=fib(n-1)+fib(n-2)
            return cache[n]
        }
    }
}
const mem=dpfibonacci()
console.log(mem(1000))

const fib=(n)=>{
    const res=Math.floor((((1+Math.sqrt(5))**n)-((1-Math.sqrt(5)))**n)/(2**n*Math.sqrt(5)))
    return res
}
console.log(fib(100)) //time complexity o(1)
                    //space cpmplexity o(1)
                    //however it's not a readable solution