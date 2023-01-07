const url = "/api"
const para = document.querySelector('#write')
let count = 3
const str = `Redirect in ${count} seconds ...`
const timeIn = setInterval(()=>{
    count--
    document.querySelector('#write').innerHTML = `Redirect in ${count} seconds ...`
    if(count === 0 ){
        clearInterval(timeIn)
        window.location = url
    }
},1000)
