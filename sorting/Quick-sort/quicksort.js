//lemuto's partition
var time1=performance.now()
function quicksort(arr,left,right){
    debugger;
    if (left<right){
        let partition_pos=partition(arr,left,right)
        quicksort(arr,left,partition_pos-1)
        quicksort(arr,partition_pos+1,right)
       
    }
}
function partition(arr,left,right){
    let pivot=arr[right]
    let small_index=left-1
    for(let i=left;i<right;i++){
        if(arr[i]<pivot){
            small_index+=1
            swap(arr,i,small_index) 
           
    
        }

}
swap(arr,right,small_index+1)
return small_index+1
}
function swap(arr,first,second){  
  
    let temp=arr[first]
    arr[first]=arr[second]
    arr[second]=temp
}
var time2=performance.now()
console.log(`lemuto implementation${time2-time1}`)
const a = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
quicksort(a,0,a.length-1)
console.log(a)

//hoar's implementation
var time3=performance.now()
function quicksort2(arr,low,high){
    if (low<high){
        let partitionpos2=partition2(arr,low,high)
        quicksort2(arr,low,partitionpos2)
        quicksort2(arr,partitionpos2+1,high)
    }
}
function partition2(arr,low,high){
    let pivot=arr[low]
    let i=low
    let j=high
    while(true){
        while(arr[i]<pivot){
            i+=1
        }
        while(arr[j]>pivot){
            j-=1
        }
        if(i>=j){
            return j
        }
        swap(arr,i,j)
    }
}
var time4=performance.now()
console.log(`hoar's implementation${time4-time3}`)
const b = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
quicksort2(b,0,b.length-1)
console.log(a)
