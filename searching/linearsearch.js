function linearsearch(arr,key){
    for(let i=0;i<arr.length;i++){
        if (key===arr[i]){
            return i,arr[i]
        }
    }
    return false
}
const a=['god','zeus','ares','kratos','loki','thor','odin','atreus']
const key='loki'
console.log(linearsearch(a,key))

console.log(a.indexOf('odin'))
console.log(a.find(function(item){
    return item==='ares'
}))
console.log(a.findIndex(function(item){
    return item==='god'
}))