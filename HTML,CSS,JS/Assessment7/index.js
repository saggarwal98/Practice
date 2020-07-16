function callMe(){
    Passenger={name:"Arun",age:28,reservedStatus:true}
    // var n=document.getElementById("name")
    // var a=document.getElementById("age")
    // var rs=document.getElementById("reservedStatus")
    var namestr="Name:"+Passenger.name
    document.getElementById("name").innerHTML=namestr
    agestr="Age:"+Passenger.age
    document.getElementById("age").innerHTML=agestr
    rsstr="Reserved Status:"+Passenger.reservedStatus
    document.getElementById("reservedStatus").innerHTML=rsstr
}