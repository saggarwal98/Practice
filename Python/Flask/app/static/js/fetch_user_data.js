$("document").ready(function(){
    $.get("/fetch_user_data",{user_email:},function(data,status){
        $("#div1").html(data)
    })
});