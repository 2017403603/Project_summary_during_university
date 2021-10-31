<%--
  Created by IntelliJ IDEA.
  User: ASUS
  Date: 2021/8/7
  Time: 17:30
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
    <style type="text/css">
        .mt{
            width: 650px;
            border:1px solid red;
        }
    </style>
</head>
<body>
       <h1 align="center">9x9乘法口诀表</h1>
       <table class="mt" align="center">
       <%
          for(int i=1;i<=9;i++){ %>
           <tr class="mt">
              <%for(int j=1;j<=i;j++){%>
               <th class="mt">
              <%=j + "x" + i + "=" + i*j%>
               </th>
       <%}%>
           </tr>
       <%}%>
       </table>
</body>
</html>
