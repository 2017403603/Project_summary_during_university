<%@ page import="java.util.HashMap" %>
<%@ page import="java.util.Map" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: ASUS
  Date: 2021/8/9
  Time: 15:26
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
       <%
         request.setAttribute("arr", new String[]{"17369427320","15200985480","123456110"});
       %>
       <c:forEach items="${requestScope.arr}" var="eachitem">
           ${eachitem}
       </c:forEach>

       <%
         Map<String,Object> map = new HashMap<String,Object>();
         map.put("key1", "value1");
         map.put("key2", "value2");
         map.put("key3", "value3");
         request.setAttribute("map", map);
       %>
       <hr>
       <c:forEach items="${requestScope.map}" var="entry">
           ${entry.value}
       </c:forEach>
</body>
</html>
