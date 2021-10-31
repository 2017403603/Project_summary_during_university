<%@ page import="java.util.List" %>
<%@ page import="com.atguigu.pojo.Student" %>
<%@ page import="java.util.ArrayList" %><%--
  Created by IntelliJ IDEA.
  User: ASUS
  Date: 2021/8/7
  Time: 18:10
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
    <style>
        table{
            border: 1px red solid;
            width: 600px;
            border-collapse: collapse;
        }
    </style>
</head>
<body>
       <%
           List<Student> studentList = new ArrayList<Student>();
           for(int i=0;i<10;i++){
               studentList.add(new Student(i+1,"name"+(i+1),18+(i+1),"123456"+i));
           }
       %>

       <table>
           <tr>
               <td>编号</td>
               <td>姓名</td>
               <td>年龄</td>
               <td>电话</td>
               <td>操作</td>
           </tr>
       <%
           for(Student student:studentList){
               %>
           <tr>
               <td><%=student.getId()%></td>
               <td><%=student.getName()%></td>
               <td><%=student.getAge()%></td>
               <td><%=student.getPhnoe()%></td>
               <td>删除、修改</td>
           </tr>
           <%
           }
       %>
       </table>
</body>
</html>
