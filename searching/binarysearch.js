const a=[10,101,450,3800,5689,10000]


var time1=performance.now()
function binarysearch(arr,key,low,high){
    if(low<=high){
        let mid=Math.floor(low+(high-low)/2)
        if(key==arr[mid]){
            return true
        }
        else if(key>arr[mid]){
            return binarysearch(arr,key,mid+1,high)
        }
        else if(key<arr[mid]){
            return binarysearch(arr,key,low,mid-1)

        }
        
    }
    return false
}
var time2=performance.now()
console.log(`recursive way of doing bs${time2-time1}`)
console.log(binarysearch(a,10000,0,a.length-1))

var time3=performance.now()
function binarysearch2(arr,key){
    let low=0
    let high=arr.length
    while(low<=high){
        let mid=Math.floor(low+(high-low)/2)
        if(arr[mid]===key){
            return true
        }
        else if(arr[mid]>key){
            high=mid-1
        }
        else if(arr[mid]<key){
            low=mid+1
        }
    }
    return false

}
var time4=performance.now()
console.log(`iterative way of doing bs${time4-time3}`)
console.log(binarysearch2(a,10000))
let rec=time2-time1
let iter=time4-time3
console.log(whichbest(rec,iter))
function whichbest(per1,per2){
    if(per2>per1){
        return per1
    }
    return per2
}