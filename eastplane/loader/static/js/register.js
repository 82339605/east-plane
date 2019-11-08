// $(function(){
//   window.registStatus = 1;
//   $("input[name='username']").blur(function(){
//     //如果文本框内没有任何东西则返回
//     if($(this).val().trim().length == 0)
//       return;
//     //如果文本框内有数据的话则发送ajax请求判断数据是否存在
//     $.get(
//       '/check_repeat/',
//       {'uname':$(this).val()},
//       function(data){
//         $("#check").html(data.msg);
//         //为registStatus赋值，以便在提交表单时使用
//         window.registStatus = data.status;
//         console.log("data.status:"+data.status);
//       },'json'
//     );
//   });
//   /**2.为#formReg表单元素绑定submit事件*/
//   $("#formReg").submit(function(){
//     //判断registStatus的值，决定表单是否要被提交
//     console.log('registStatus:'+registStatus);
//     if(window.registStatus == 0)
//       return false;
//     else{
//     return true;}
//   });
// });
$(function () {
    window.regStatus = 0
    $("input[name='login']").blur(function () {
      if($(this).val().trim().length == 0){
        return
      }
      $.get('/check_repeat/',{'lname':$(this).val()},function (value) {
            $('#comment').html(value.msg)
            window.regStatus = value.status
      },'json')
    })
    $("#formReg").submit(function () {
        if(window.regStatus == 0){
            return false
        }
        else{
            return true
        }
    })
})