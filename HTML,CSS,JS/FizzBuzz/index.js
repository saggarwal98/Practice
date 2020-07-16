window.onload=function(){
    var inputspace=document.getElementById("inputspace")
    var list=document.getElementById("list")
    document.getElementById("submitbtn").onclick=function(){
        // console.log(inputspace.value)
        var listcontent=""
        for(let i=1;i<=inputspace.value;i++){
            // console.log(i)
            let temp=""
            if(i % 3 === 0) temp+="Fizz"
            if(i % 5 === 0) temp+="Buzz"
            if(temp === "") temp=i
            listcontent+=`<li>${temp}</li>`
        }
        list.innerHTML=listcontent
    }
}