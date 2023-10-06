function facto(n){
    if (n==1){
        return 1
    }
    else{
        return n*facto(n-1)
    }
}
console.log(facto(5))

function facto2(n){
    let res=1
    let i=2
    while(i<=n){
        res*=i
        i++;
    }
    return res
}
console.log(facto2(5))