function getAge(){
    // console.log("Button clicked")
    var dob=document.getElementById("dob").value
    var i=dob.slice(0,4)
    var curr=new Date()
    var year=curr.getFullYear()
    if(year<=i){
        str="Wrong date!!"
        document.getElementById("showresults").innerHTML=str
    }
    else{
        var diff=year-i
        str="You are "+diff+" year(s) old!!"
        document.getElementById("showresults").innerHTML=str
    }
}