package com.atguigu.dao;

import com.atguigu.pojo.Book;

import java.util.List;

public interface BookDao {

    public int addBook(Book book);
    public int DeleteBook(Integer id);
    public int UpdateBook(Book book);
    public Book QueryBookById(Integer id);
    public List<Book> QueryBooks();
    Integer queryForPageTotalCount();
    List<Book> queryForPageItems(int begin, int pageSize);
    Integer queryForPageTotalCountByPrice(int min, int max);
    List<Book> queryForPageItemsByPrice(int begin, int pageSize, int min, int max);
}
