<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>尚硅谷会员注册页面</title>
	<%@include file="/pages/common/head.jsp"%>
	<style type="text/css">
		.login_form{
			height:420px;
			margin-top: 25px;
		}

	</style>
	<script type="text/javascript">
		$(function () {

			$("#username").blur(function () {
				var username=this.value;

				$.getJSON("http://localhost:8080/book/userServlet","action=ajaxExistUsername&username="+username,function (data) {
					if (data.isExistusername){
						$("span.errorMsg").text("用户名已经存在！");
					}
					else{
						$("span.errorMsg").text("用户名可用！");
					}
				})
			})

			$("#code_img").click(function () {
				this.src="${basePath}kaptcha.jpg";
			})
			$("#sub_btn").click(function () {
				//username
				var usernameText=$("#username").val();
				var usernamePatt=/^\w{5,12}$/;
				if(!usernamePatt.test(usernameText)){
					$("span.errorMsg").text("用户名不合法！");
					return false;
				}
				//password
				var passwordText=$("#password").val();
				var passwordPatt=/^\w{5,12}$/;
				if(!passwordPatt.test(passwordText)){
					$("span.errorMsg").text("密码不合法！");
					return false;
				}
				//rep
				var repwdText=$("#repwd").val();
				if(repwdText!=passwordText){
					$("span.errorMsg").text("确认密码和密码不一致！");
					return false;
				}
				//email
				var emailText = $("#email").val();
				var emailPatt=/^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
				if(!emailPatt.test(emailText)){
					$("span.errorMsg").text("邮箱格式不合法！");
					return false;
				}
				//yanzheng
				var codeText=$("#code").val();
				codeText=$.trim(codeText); 
				if(codeText==null||codeText==""){
					$("span.errorMsg").text("验证码不能为空！");
					return false;
				}
				//xiaochu
				$("span.errorMsg").text("");
			});
		});
	</script>
</head>
<body>
		<div id="login_header">
			<img class="logo_img" alt="" src="static/img/logo.gif" >
		</div>
		
			<div class="login_banner">
			
				<div id="l_content">
					<span class="login_word">欢迎注册</span>
				</div>

				<div id="content">
					<div class="login_form">
						<div class="login_box">
							<div class="tit">
								<h1>注册尚硅谷会员</h1>
								<span class="errorMsg">
									${requestScope.msg}
								</span>
							</div>
							<div class="form">
								<form action="userServlet" method="post">
									<input type="hidden" name="action" value="regist">
									<label>用户名称：</label>
									<input class="itxt" type="text" placeholder="请输入用户名"
										   autocomplete="off" tabindex="1" name="username"
										   value="${requestScope.username}" id="username"/>
									<br />
									<br />
									<label>用户密码：</label>
									<input class="itxt" type="password" placeholder="请输入密码" autocomplete="off" tabindex="1" name="password" id="password" />
									<br />
									<br />
									<label>确认密码：</label>
									<input class="itxt" type="password" placeholder="确认密码" autocomplete="off" tabindex="1" name="repwd" id="repwd" />
									<br />
									<br />
									<label>电子邮件：</label>
									<input class="itxt" type="text" placeholder="请输入邮箱地址" autocomplete="off"
										   tabindex="1" name="email"
										   value="${requestScope.email}" id="email" />
									<br />
									<br />
									<label>验证码：</label>
									<input class="itxt" type="text" name="code" style="width: 150px;" id="code"/>
									<img alt="" src="kaptcha.jpg" id="code_img" style="float: right;margin-right:40px;width:80px;height: 40px">
									<br />
									<br />
									<input type="submit" value="注册" id="sub_btn" />
									
								</form>
							</div>
						</div>
					</div>
				</div>
			</div>
		<%@include file="/pages/common/footer.jsp"%>
</body>
</html>