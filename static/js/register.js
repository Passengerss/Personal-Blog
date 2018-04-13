$(function () {
        var name_exist_error = true;
        var name_out_length_error = true;
        var pwd_out_length_error = true;
        var email_format_error = true;

        // 判断用户名
        $("#username").blur(
            function () {
                name_check();
            }
        );

        // 密码长度
        $("#password").blur(
            function () {
                password_length_check();
            }
        );
        // 两次输入密码不一样
        $("#cpassword").blur(
            function () {
                password_repeat_check();
            }
        );
        // 邮箱格式验证
        $("#email").blur(
            function () {
                email_format_check();
            }
        );

        function name_check() {
            var name = $("#username").val();
            var name_length = $("#username").val().length;
            if(name_length===0){
                    $("#username").next().html("用户名不能为空").show();
                    name_out_length_error = true;
                }
            else{
                if(name_length>10){
                    $("#username").next().html("最多包含10个字符").show();
                    name_out_length_error = true;
                }
                else{
                    name_out_length_error = false;
                    $.get("/user/register_exist/"+name,function (data) {
                        if(data.status===1){ // 存在
                            $("#username").next().html("用户名已存在").show();
                            name_exist_error = true;
                        }
                        else {
                                $("#username").next().html("").hide();
                                name_exist_error = false;
                        }
                    });

                }
            }
        }

        function password_length_check() {
                var pwd = $("#password").val();
                var pwd_length = $("#password").val().length;
                if(pwd == ""){
                    $("#password").next().html("密码不能为空").show();
                    pwd_out_length_error = true;
                }
                if(pwd_length<8){
                    $("#password").next().html("密码长度不能低于8位").show();
                    pwd_out_length_error = true;
                }
                else{
                    $("#password").next().html("").hide();
                    pwd_out_length_error = false;
                }
            }

        function password_repeat_check() {
            var pwd = $("#password").val();
            var cpwd = $("#cpassword").val();
            if(pwd !== cpwd){
                $("#cpassword").next().html("两次输入的密码不一致，请重新输入").show();
                pwd_out_length_error = true;
            }
            else {
                $("#password").next().html("").hide();
                pwd_out_length_error = false;
            }
        }

        function email_format_check(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($("#email").val())) {
			$("#email").next().hide();
			email_format_error = false;
		}
		else {
			$("#email").next().html('你输入的邮箱格式不正确').show();
			email_format_error = true;
		}

	    }

	    // 提交
        $("#reg_form").submit(function (){
            name_check();
            password_length_check();
            password_repeat_check();
            email_format_check();
            if(name_exist_error == false && name_out_length_error==false && pwd_out_length_error==false && email_format_error==false){
                return true;
            }
            else {
                return false;
            }
        });
    });