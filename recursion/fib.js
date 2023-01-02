//fib using without using array
function fib(n){
    let [prev,cur,sum]=[0,1,0]
    if (n<2){
        return n
    }
    else{
        let i=2
        while(i<n+1){
            sum=prev+cur
            prev=cur
            cur=sum
            i++;
        }
    }
    return sum
}
console.log(fib(5))
//fib using array
function fib2(n){
    let arr=[0,1]
    if (n<2){
        return n
    }
    else{
        for(let i=2;i<=n;i++){
            arr.push(arr[i-1]+arr[i-2])

        }
    }
    return arr[n]
}
console.log(fib2(12))
//fib using recursion

function fib3(n){
    if (n<2){
        return n

    }
    else{
        return fib3(n-1)+fib(n-2)
    }
}

console.log(fib3(13))