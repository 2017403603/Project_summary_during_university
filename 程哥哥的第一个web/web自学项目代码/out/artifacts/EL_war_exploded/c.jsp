<%--
  Created by IntelliJ IDEA.
  User: ASUS
  Date: 2021/8/8
  Time: 18:04
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%--       <%=request.getScheme()%>--%>
       1.协议:${pageContext.request.scheme}<br>
       2.服务器ip:${pageContext.request.serverName}<br>
       3.服务器端口:${pageContext.request.serverPort}<br>
       4.获取工程路径:${pageContext.request.contextPath}<br>
       5.获取请求方法:${pageContext.request.method}<br>
       6.获取客户端IP地址:${pageContext.request.remoteHost}<br>
       7.回去会话的id编号:${pageContext.session.id}<br>
</body>
</html>
