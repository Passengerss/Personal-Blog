    $(function () {
         function timer() {
            var now = new Date();   //
            var year = now.getFullYear();
            var month = now.getMonth()+1; // 从0-11
            var date = now.getDate();
            var week = now.getDay();  // 星期天为0
            var hour = now.getHours();
            var minute = now.getMinutes();
            var second = now.getSeconds();
            var real_time = "   "+year+" 年 "+handle(month)+" 月 "+handle(date)+" 日 " +handleweek(week)+"    "+handle(hour)+":"+handle(minute)+":"+handle(second);
            $(".clock").html(real_time)
         }
         timer();
         setInterval(timer,1000);
         function handleweek(week_num) {
            switch (week_num){
                case 0: return"星期天"; break;
                case 1: return"星期一"; break;
                case 2: return"星期二"; break;
                case 3: return"星期三"; break;
                case 4: return"星期四"; break;
                case 5: return"星期五"; break;
                case 6: return"星期六";
            }
        }
        function handle(num) {
            if(num < 10){
                num = "0"+num;
            }
            return num;
        }
        /* 监听div内容变化*/
        $(".clock").bind('DOMNodeInserted', function() {
            change_color();
        });
        function change_color() {
            var r = Math.floor(Math.random()*256);
            var g = Math.floor(Math.random()*256);
            var b = Math.floor(Math.random()*256);
            var clock_color = `rgb(${r},${g},${b})`;
            $(".clock").css("color",clock_color);
        }
    });