package com.atguigu.web;

import com.atguigu.pojo.User;
import com.atguigu.service.UserService;
import com.atguigu.service.impl.UserServiceImpl;
import com.atguigu.utils.WebUtils;
import com.google.gson.Gson;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class UserServlet extends BaseServlet {
    private UserService userService = new UserServiceImpl();

    protected void login(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String username = req.getParameter("username");
        String password = req.getParameter("password");
        User loginUser=userService.login(new User(null,username, password,null));
        if(loginUser == null){
            //System.out.println("用户名或密码错误！！！");
            req.setAttribute("msg", "用户名或密码错误！！！");
            req.setAttribute("username",username);
            req.getRequestDispatcher("/pages/user/login.jsp").forward(req, resp);
        }
        else {
            req.getSession().setAttribute("user", loginUser);
            req.getRequestDispatcher("/pages/user/login_success.jsp").forward(req, resp);
        }
    }


    protected void logout(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.getSession().invalidate();
        resp.sendRedirect(req.getContextPath());
    }

    protected void regist(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String token = (String)req.getSession().getAttribute("KAPTCHA_SESSION_KEY");
        req.getSession().removeAttribute("KAPTCHA_SESSION_KEY");

        String username=req.getParameter("username");
        String password=req.getParameter("password");
        String email=req.getParameter("email");
        String code=req.getParameter("code");

        User user=WebUtils.copyParmToBean(req.getParameterMap(), new User());

        if(token!=null&&token.equalsIgnoreCase(code)){
            if(userService.existsUsername(username)){
                req.setAttribute("msg", "用户名已存在！！！");
                req.setAttribute("username", username);
                req.setAttribute("email", email);
                //System.out.println("用户名["+username+"]已存在");
                req.getRequestDispatcher("/pages/user/regist.jsp").forward(req, resp);
            }
            else{
                userService.registUser(new User(null,username,password,email));
                req.getRequestDispatcher("/pages/user/regist_success.jsp").forward(req, resp);
            }
        }
        else{
            req.setAttribute("msg", "验证码错误！！！");
            req.setAttribute("username", username);
            req.setAttribute("email", email);
            //System.out.println("验证码["+code+"]错误！！");
            req.getRequestDispatcher("/pages/user/regist.jsp").forward(req, resp);
        }
    }


    protected void ajaxExistUsername(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String username= req.getParameter("username");
        boolean isExistusername = userService.existsUsername(username);
        Map<String,Object> resultmap = new HashMap<>();
        resultmap.put("isExistusername",isExistusername);

        Gson gson = new Gson();
        String json= gson.toJson(resultmap);
        resp.getWriter().write(json);
    }

}
