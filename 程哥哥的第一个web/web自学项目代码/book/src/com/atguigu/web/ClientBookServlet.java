package com.atguigu.web;

import com.atguigu.pojo.Book;
import com.atguigu.pojo.Page;
import com.atguigu.service.BookService;
import com.atguigu.service.impl.BookServiceImpl;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class ClientBookServlet extends BaseServlet {
    BookService bookService =new BookServiceImpl();
    protected void page(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //System.out.println("经过了前台的ClientBookServlet程序");
        int pageNo = Integer.parseInt(req.getParameter("pageNo")==null?"1":req.getParameter("pageNo"));
        int pageSize = Integer.parseInt(req.getParameter("pageSize")==null? Page.PAGE_SIZE.toString():req.getParameter("pageSize"));
        Page<Book> page = bookService.page(pageNo, pageSize);

        page.setUrl("client/bookServlet?action=page");

        req.setAttribute("page",page);
        req.getRequestDispatcher("/pages/client/index.jsp").forward(req, resp);
    }
    protected void pageByPrice(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //System.out.println("经过了前台的ClientBookServlet程序");
        int pageNo = Integer.parseInt(req.getParameter("pageNo")==null?"1":req.getParameter("pageNo"));
        int pageSize = Integer.parseInt(req.getParameter("pageSize")==null? Page.PAGE_SIZE.toString():req.getParameter("pageSize"));
        int min = Integer.parseInt(req.getParameter("min")==null?"0":req.getParameter("min"));
        int max = Integer.parseInt(req.getParameter("max")==null?"999999":req.getParameter("max"));
        Page<Book> page = bookService.pageByPrice(pageNo, pageSize, min, max);

        StringBuilder sb = new StringBuilder("client/bookServlet?action=pageByPrice");
        if(req.getParameter("min")!=null){
            sb.append("&min=").append(req.getParameter("min"));
        }
        if(req.getParameter("max")!=null){
            sb.append("&max=").append(req.getParameter("max"));
        }
        page.setUrl(sb.toString());

        req.setAttribute("page",page);
        req.getRequestDispatcher("/pages/client/index.jsp").forward(req, resp);
    }
}
