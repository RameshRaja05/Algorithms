function insertionsort(arr){
    const n=arr.length
    for(let i=1;i<n;i++){
        const key=arr[i]
        let j=i-1;
        while(j>=0 &&key<arr[j]){
            console.log(arr)
            arr[j+1]=arr[j]
            j-=1
        }
        arr[j+1]=key
    }
    return arr
}
let a=[123,56,89,5,1,2]
insertionsort(a)