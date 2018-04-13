
$(function () {
    if({{error_name}}== 1){
        $(".username").val("{{uname}}");
        $(".username").next().html("用户名错误").show();
    }
    if({{error_pwd}}== 1){
        $(".username").val("{{uname}}");
        $(".password").val("{{pwd}}");
        $(".password").next().html("密码错误").show();
    }
});

// function login() {
//         $.ajax({url:"/user/login_handle/",type:"POST",data:$("#login_form").serialize(), success:function (data) {
//             if(data.status === "success"){  // 登录信息正确
//                 window.location.href = "{%url 'user:index'%}"
//             }
//             if(data.status === "name_error"){
//                 $("#uname").val(data.uname);
//                 $("#uname").next().html("用户名错误").show();
//             }
//             if(data.status === "pwd_error"){
//                 $("#uname").val(data.uname);
//                 $("#pwd").val(data.pwd);
//                 $("#pwd").next().html("密码错误").show();
//             }
//         }, dataType:"json"})
//     }