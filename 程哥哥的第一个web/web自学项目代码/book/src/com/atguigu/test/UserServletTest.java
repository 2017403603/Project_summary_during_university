package com.atguigu.test;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class UserServletTest {
    public void login(){
        System.out.println("login()方法被调用了");
    }
    public void regist(){
        System.out.println("regist()方法被调用了");
    }
    public void updataUser(){
        System.out.println("updataUser()方法被调用了");
    }
    public void updataUserPassword(){
        System.out.println("updataUserPassword()方法被调用了");
    }

    public static void main(String[] args) {
        String action="login";
        try {
            Method method=UserServletTest.class.getDeclaredMethod(action);
            System.out.println(method);
            method.invoke(new UserServletTest());
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }
    }
}
