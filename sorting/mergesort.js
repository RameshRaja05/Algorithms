// function mergesort(arr){
//     if(arr.length==1){
//         return arr
//     }
//     else{
//         let low=0;
//         let high=arr.length;
//         let mid=Math.floor(low+(high-low)/2)
//         let left=arr.slice(0,mid)
//         let right=arr.slice(mid,high)
//         return merge(mergesort(left),mergesort(right))
//     }
// }
// function merge(left,right){
//     let i=j=0
//     let res=[]
//     while(i<left.length &&j<right.length){
//         if(left[i]<=right[j]){
//             res.push(left[i])
//             i+=1
//         }
//         else{
//             res.push(right[j])
//             j+=1
//         }
       
//     }
//     return res.concat(left.slice(i).concat(right.slice(j)))

// }
// let a=[239,12,34,45,90,4,200,58]
// console.log(mergesort(a))

function mergesort2(arr){
    if (arr.length>1){
        const high=arr.length;
        const low=0;
        const mid=Math.floor(low+(high-low)/2);
        let left=arr.slice(0,mid);
        let right=arr.slice(mid);
        mergesort2(left)
        mergesort2(right)
    
    let i=j=k=0
    while(i<left.length && j<right.length){
        if(left[i]<=right[j]){
            arr[k]=left[i]
            i+=1
        }
        else{
            arr[k]=right[j]
            j+=1
        }
        k+=1
    }
    while(i<left.length){
        arr[k]=left[i]
        i+=1
        k+=1

    }
    while(j<right.length){
        arr[k]=right[j]
        j+=1
        k+=1
    }

}
}
let a=[239,12,34,45,90,4,200,58]
mergesort2(a)
console.log(a)//o(n*logn)