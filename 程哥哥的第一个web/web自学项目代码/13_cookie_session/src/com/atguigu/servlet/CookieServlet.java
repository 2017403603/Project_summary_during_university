package com.atguigu.servlet;

import com.atguigu.utils.CookieUtils;

import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class CookieServlet extends BaseServlet {

    protected void testPath(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Cookie cookie =new Cookie("path1", "path1");
        cookie.setPath(req.getContextPath()+"/abc");
        resp.addCookie(cookie);
        resp.getWriter().write("创建了一个带有Path路径的cookie");
    }
    protected void life3600(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Cookie cookie =new Cookie("life3600", "life3600");
        cookie.setMaxAge(60*60);
        resp.addCookie(cookie);
    }
    protected void deleteNow(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Cookie cookie =CookieUtils.findCookie("key2", req.getCookies());
        if(cookie != null){
            cookie.setMaxAge(0);
            resp.addCookie(cookie);
            resp.getWriter().write("key2的cookie已删除");
        }
    }
    protected void defaultLife(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Cookie cookie =new Cookie("defaultLife", "defaultLife");
        cookie.setMaxAge(-1);
        resp.addCookie(cookie);
    }
    protected void updataCookie(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Cookie cookie =new Cookie("key2", "newvalue2");
        resp.addCookie(cookie);
        resp.getWriter().write("key2的Cookie值已经修改");
    }

    protected void getCookie(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Cookie[] cookies = req.getCookies();
        for (Cookie cookie : cookies) {
            resp.getWriter().write("Cookie["+cookie.getName()+"="+cookie.getValue()+"]<br/>");
        }
        if(CookieUtils.findCookie("key2", cookies) != null){
            resp.getWriter().write("找到了需要的Cookie");
        }
    }

    protected void createCookie(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Cookie cookie =new Cookie("key1", "value1");
        resp.addCookie(cookie);
        Cookie cookie1 =new Cookie("key2", "value2");
        resp.addCookie(cookie1);
        resp.getWriter().write("Cookie创建成功");
    }
}
