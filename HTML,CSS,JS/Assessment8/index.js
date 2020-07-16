// window.onload=function(){
//     var Cars={
//         "Innova":{
//             Price:900000,
//             Year:2016
//         },
//         "Dzire":{
//             Price:700000,
//             Year:2017
//         },
//         "i20":{
//             Price:500000,
//             Year:2013
//         },
//         "i10":{
//             Price:400000,
//             Year:2016
//         }}
//         document.getElementById("SelectCar").onchange=function displayCarDetails(){
//             var name=document.getElementById("SelectCar").value
//             var ind=-1
//             Object.keys(Cars).forEach((key,index)=>{
//                 if(name==key){
//                     ind=index
//                     // console.log(ind)
//                 }
//             })
//             // console.log(ind)
//             if(ind>-1){
//                 var price=Object.values(Cars)[ind].Price
//                 var year=Object.values(Cars)[ind].Year
//                 // console.log(year)
//                 // Object.values(Cars).forEach(value=>console.log(value))
//                 // var price=Cars[ind][0]
//                 // var year=Cars[ind][1]
//                 var str=name+"-"+price+"-"+year
//                 document.getElementById("CarDetail").innerHTML=str
//             }
//         }
// }
let carDetails =[["Innova",900000,2016],["Dzire",700000,2017],["i20",500000,2013],["i10",400000,2016]]




function displayCarDetails(){
    var name=document.getElementById("SelectCar").value
    var ind=-1
    for(let i=0;i<carDetails.length;i++){
        if(name==Cars[i][0]){
            ind=i
            break
        }
    }
    var str=name+"-"+carDetails[ind][1]+"-"+carDetails[ind][2]
    document.getElementById("CarDetail").innerHTML=str
}


