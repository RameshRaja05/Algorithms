// let basket=[12,45,90,7,1,4,6,88,13]
// basket.sort(function(a,b){
//     console.log(b-a)
//     return b-a;//descending for asc return a-b

// });
// console.log(basket)
// let names=['ramesh','raja','arun','bool']
// names.sort((a,b)=>a.localeCompare(b))
// console.log(names)

function bubblesort(arr){
    n=arr.length
    for(let i=0;i<n;i++){
        for(let j=0;j<n;j++){
            if (arr[j]>arr[j+1]){
              let t=arr[j]
              arr[j]=arr[j+1]
              arr[j+1]=t
            }
        }
    }
    return arr
}
a=[12,3,4,5,6,90,100,34,56,78]
console.log(bubblesort(a)) //o(n^2)
