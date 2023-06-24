<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Clock</title>
    <style>
        body{
            background-color: black;
        }

        .Clock{ 
            background-color: blue;
            border:10px solid yellow;
            margin:7px 3px;
            position:absolute;
            color:lime;
            top:50%;
            left:50%;
            transform: translatex(-50%) translatey(-50%);
            font-size:60px;
            font-family: Orbitron;
            letter-spacing: 8px;
           
        }
    </style>
</head>
<body>
    <div id="DigitalClock" class="Clock"></div>
    <script type="text/javascript">
    function showTime(){          //for reloading per second
        var date = new Date();
        var hr= date.getHours();
        var min=date.getMinutes();
        var sec=date.getSeconds();
        var session="AM";
        /*var dt=date.getDate();
        var mth=date.getMonth();
        var yr=date.getFullYear();*/
        var dt=date.toDateString();

        if (hr==0){
            hr=12;  //12 hr format
            session="AM"
        }
        if (hr>12){
           hr-=12;   // 12 hr now Format now 
           session="PM";
        }
        if (hr<10){
            hr="0"+hr
        }
        if (min<10){
            min="0"+min;
        }
        if (sec<10){
            sec="0"+sec;  //it written also as-> s=(s<10)?"0"+s:s;
        }

        document.getElementById("DigitalClock").innerHTML = hr+":"+min+":"+sec+"|"+ session+"<hr>"+"<br>"+ dt;

        //document.getElementById("DigitalClock").innerHTML=dt +"/"+ mth +"/"+yr;
    
    
        setTimeout(showTime,1000);
    }
    
    showTime();
    </script>
    
</body>
</html>
