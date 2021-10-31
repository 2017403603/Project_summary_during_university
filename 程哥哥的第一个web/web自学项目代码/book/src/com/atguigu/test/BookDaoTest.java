package com.atguigu.test;

import com.atguigu.dao.BookDao;
import com.atguigu.dao.impl.BookDaoImpl;
import com.atguigu.pojo.Book;
import com.atguigu.pojo.Page;
import org.junit.Test;

import java.math.BigDecimal;

public class BookDaoTest {
    private BookDao bookDao = new BookDaoImpl();
    @Test
    public void addBook() {
        bookDao.addBook(new Book(null,"程哥哥为什么这么帅","李航程",new BigDecimal(99.99),100000,0,null));
    }

    @Test
    public void deleteBook() {
        bookDao.DeleteBook(21);
    }

    @Test
    public void updateBook() {
        bookDao.UpdateBook(new Book(21,"程哥哥为什么这么帅","cgg",new BigDecimal(99.99),100000,0,null));
    }

    @Test
    public void queryBookById() {
        System.out.println(bookDao.QueryBookById(21));
    }

    @Test
    public void queryBooks() {
        for(Book queryBook:bookDao.QueryBooks()){
            System.out.println(queryBook);
        }
    }

    @Test
    public void queryForPageTotalCount() {
        System.out.println(bookDao.queryForPageTotalCount());
    }

    @Test
    public void queryForPageTotalCountByPrice() {
        System.out.println(bookDao.queryForPageTotalCountByPrice(1, 999));
    }

    @Test
    public void queryForPageItemsByPrice() {
        for (Book queryForPageItem : bookDao.queryForPageItemsByPrice(0, Page.PAGE_SIZE,1,999)) {
            System.out.println(queryForPageItem);
        }
    }


    @Test
    public void queryForPageItems() {
        for (Book queryForPageItem : bookDao.queryForPageItems(8, Page.PAGE_SIZE)) {
            System.out.println(queryForPageItem);
        }
    }
}