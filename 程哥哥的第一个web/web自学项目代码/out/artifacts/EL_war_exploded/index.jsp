<%--
  Created by IntelliJ IDEA.
  User: ASUS
  Date: 2021/8/8
  Time: 15:18
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>$Title$</title>
  </head>
  <body>
         <%
         pageContext.setAttribute("key1", "keyvalue1");
         pageContext.setAttribute("key2", "keyvalue2");
         %>
         ${pageScope.key1}
  </body>
</html>
