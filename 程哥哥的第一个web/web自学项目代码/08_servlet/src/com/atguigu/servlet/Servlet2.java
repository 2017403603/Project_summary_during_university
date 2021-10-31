package com.atguigu.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class Servlet2 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //super.doGet(req, resp);
        String username = req.getParameter("username");
        System.out.println("在Servlet2(柜台2)中查看参数（材料）："+username);
        Object key1=req.getAttribute("key1");
        System.out.println("柜台1是否有章："+key1);
        System.out.println("Servlet2处理自己的业务");

    }
}
