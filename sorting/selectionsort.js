function selectionsort(arr){
    for(let i=0;i<arr.length;i++){
        let min_idx=i
        let t=arr[min_idx]

        for(let j=i+1;j<arr.length;j++){
            if (arr[j]<arr[min_idx]){
                min_idx=j
            }
        }
        arr[i]=arr[min_idx]
        arr[min_idx]=t
    }
    return arr
}
let a=[12,2,3,4,5,6,7,9]
console.log(selectionsort(a))