<%@ page import="com.atgui.pojo.Person" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.Map" %>
<%@ page import="java.util.HashMap" %><%--
  Created by IntelliJ IDEA.
  User: ASUS
  Date: 2021/8/8
  Time: 15:28
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
      <%
          Person person = new Person();
          person.setId(1);
          person.setPhones(new String[]{"17369427320","15200985480","110"});
          List<String> cities = new ArrayList<String>();
          cities.add("北京");
          cities.add("上海");
          cities.add("深圳");
          person.setCities(cities);
          Map<String,Object> map =new HashMap<>();
          map.put("key1", "value1");
          map.put("key2", "value2");
          map.put("key3", "value3");
          person.setMap(map);


          pageContext.setAttribute("p", person);

      %>
      输出person：${p}<br>
      输出person的id属性:${p.id}<br>
      输出person的phones数组属性值:${p.phones[1]}<br>
      输出person的cities集集合的元素值:${p.cities}<br>
      输出person的Map的映射属性:${p.map["key1"]}<br>

</body>
</html>
