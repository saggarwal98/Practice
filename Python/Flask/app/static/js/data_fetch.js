$("document").ready(function(){
    $.get("/data_fetch",function(data,status){
        // console.log(data)
        newobj=JSON.parse(data)
        str=`<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
        <th>Gender</th>
    </tr>`
        for(i of newobj){
            name=i["name"]
            age=i["age"]
            gender=i['gender']
            str+=`
    <tr>
        <td>`+name+`</td>
        <td>`+age+`</td>
        <td>`+gender+`</td>
    </tr>`}
        str+=`
</table>`
        console.log(str)
        // $("#table1").html(str)
        // // $("table").append(str)
        $("#div1").html(str)
    })
});