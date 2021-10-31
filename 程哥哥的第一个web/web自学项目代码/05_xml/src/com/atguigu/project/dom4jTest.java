package com.atguigu.project;

import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;
import org.junit.Test;

import java.awt.print.Book;
import java.math.BigDecimal;
import java.util.List;

public class dom4jTest {
    @Test
    public void test1() throws Exception {
        SAXReader saxReader = new SAXReader();
        try {
            Document document=saxReader.read("src/books.xml");
            System.out.println(document);
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
    //读取
    @Test
    public void test2() throws Exception {
        SAXReader saxReader = new SAXReader();
        Document document=saxReader.read("src/books.xml");
        Element rootElement = document.getRootElement();
        //System.out.println(rootElement);
        List<Element> books=rootElement.elements("book");
        for(Element book : books){
            //System.out.println(book.asXML());
            Element nameElement = book.element("name");
            //System.out.println(nameElement.asXML());
            String nameText = nameElement.getText();
            String priceText=book.elementText("price");
            String authorText = book.elementText("author");
            //System.out.println(priceText+authorText);
            String snvalue = book.attributeValue("sn");
            System.out.println(new book(snvalue,nameText,new BigDecimal(priceText),authorText).toString());
        }
    }
    @Test
    public void test3(){
        book booklhc=new book("SN85231","JAVA入门到放弃",new BigDecimal(10.00),"李航程");
        System.out.println(booklhc);

    }
}
