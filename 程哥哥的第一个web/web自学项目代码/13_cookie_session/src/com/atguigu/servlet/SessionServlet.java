package com.atguigu.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

public class SessionServlet extends BaseServlet {
    protected void setAttribute(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.getSession().setAttribute("key1", "value1");
        resp.getWriter().write("已经向Session中保存了数据");

    }
    protected void getAttribute(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Object key1value=req.getSession().getAttribute("key1");
        resp.getWriter().write("从Session中获取出key1的数据是"+key1value);

    }
    protected void createOrGetsession(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        HttpSession session = req.getSession();
        boolean isNew=session.isNew();
        String id=session.getId();
        resp.getWriter().write("得到的Session的id是："+id + "<br>");
        resp.getWriter().write("这个Session是否是新创建的："+ isNew + "<br>");
    }
}
