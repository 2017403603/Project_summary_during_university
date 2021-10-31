package com.atguigu.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class RequestAPIServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //super.doGet(req, resp);
        System.out.println("URI->:"+req.getRequestURI());
        System.out.println("URI->:"+req.getRequestURL());
        System.out.println("客户端IP地址:"+req.getRemoteHost());
        System.out.println("请求头User-Agent==>>:"+req.getHeader("User-Agent"));
    }
}
