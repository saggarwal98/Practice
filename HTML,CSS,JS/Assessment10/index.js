function SumOfSeries(){
        var curr=1
        var prev=0
        sum=0
        for(;curr<=100;){
            sum=sum+curr
            var temp=curr
            var curr=curr+prev
            var prev=temp
        }
        document.getElementById("result").innerHTML=sum
        console.log(curr)
}