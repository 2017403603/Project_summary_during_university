<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: ASUS
  Date: 2021/8/9
  Time: 14:33
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
       保存之前：${requestScope.abc}<br>
       <c:set scope="request" var="abc" value="abcvalue"/>
       保存之后：${requestScope.abc}<br>

       <c:if test="${12==12}">
           <h1>12等于12</h1>
       </c:if>

       <%
          request.setAttribute("height", 178);
       %>
       <c:choose>
           <c:when test="${requestScope.height>190}">
               <h2>小巨人2</h2>
           </c:when>
           <c:when test="${requestScope.height>180}">
               <h2>很高</h2>
           </c:when>
           <c:when test="${requestScope.height>170}">
               <h2>还可以</h2>
           </c:when>
           <c:otherwise>
               <h2>剩下的</h2>
           </c:otherwise>
       </c:choose>
       <c:forEach begin="1" end="10" var="i">
           ${i}
       </c:forEach>
</body>
</html>
