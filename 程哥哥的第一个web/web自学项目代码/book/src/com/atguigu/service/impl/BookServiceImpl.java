package com.atguigu.service.impl;

import com.atguigu.dao.BookDao;
import com.atguigu.dao.impl.BookDaoImpl;
import com.atguigu.pojo.Book;
import com.atguigu.pojo.Page;
import com.atguigu.service.BookService;

import java.util.List;

public class BookServiceImpl implements BookService{
    private BookDao bookDao= new BookDaoImpl();
    @Override
    public void addBook(Book book) {
        bookDao.addBook(book);
    }

    @Override
    public void deleteBookById(Integer id) {
        bookDao.DeleteBook(id);
    }

    @Override
    public void updateBook(Book book) {
        bookDao.UpdateBook(book);
    }

    @Override
    public Book queryBookById(Integer id) {
        return bookDao.QueryBookById(id);
    }

    @Override
    public List<Book> queryBooks() {
        return bookDao.QueryBooks();
    }

    @Override
    public Page<Book> page(int pageNo, int pageSize) {
        Page<Book> page = new Page<Book>();

        page.setPageNo(pageNo);
        page.setPageSize(pageSize);
        Integer pageTotalCount=bookDao.queryForPageTotalCount();
        page.setPageTotalCount(pageTotalCount);
        Integer pageTotal=pageTotalCount/pageSize;
        if(pageTotalCount%pageSize>0){
            pageTotal++;
        }
        page.setPageTotal(pageTotal);

        if(pageNo<1) pageNo=1;
        if(pageNo>pageTotal) pageNo=pageTotal;

//        System.out.println("实际是"+pageNo+"页");

        int begin=(pageNo-1)*pageSize;
        List<Book> items=bookDao.queryForPageItems(begin, pageSize);
        page.setItems(items);
        return page;
    }

    @Override
    public Page<Book> pageByPrice(int pageNo, int pageSize, int min, int max) {
        Page<Book> page = new Page<Book>();
        Integer pageTotalCount=bookDao.queryForPageTotalCountByPrice(min,max);
        page.setPageTotalCount(pageTotalCount);
        Integer pageTotal=pageTotalCount/pageSize;
        if(pageTotalCount%pageSize>0){
            pageTotal++;
        }
        page.setPageTotal(pageTotal);
        if(pageNo<1) pageNo=1;
        if(pageNo>pageTotal) pageNo=pageTotal;
        page.setPageNo(pageNo);
        page.setPageSize(pageSize);

        int begin=(pageNo-1)*pageSize;
        List<Book> items=bookDao.queryForPageItemsByPrice(begin, pageSize,min, max);
        page.setItems(items);
        return page;
    }


}
