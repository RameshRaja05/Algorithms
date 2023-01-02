function rev(s){
    if (s===''){
        return ''
    }
    else{
        return rev(s.substr(1))+s.charAt(0)
    }
}
console.log(rev('Mom'))

function rev2(s){
    let n=s.length
    let arr=[]
    for(let i=n-1;i>=0;i--){
        arr.push(s[i])

    }
    return arr.join('')
}
console.log(rev2('Mom'))

function rev3(s){
    let ar=s.split('')
    let revarr=[]
    function addtoarr(arr){
        if(arr.length>0){
            revarr.push(ar.pop())
            addtoarr(ar)
        }

    }
    addtoarr(ar)
    return revarr.join('')
}
console.log(rev3('Mom'))