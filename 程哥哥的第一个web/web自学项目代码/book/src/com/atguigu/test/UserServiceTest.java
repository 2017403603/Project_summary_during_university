package com.atguigu.test;

import com.atguigu.pojo.User;
import com.atguigu.service.UserService;
import com.atguigu.service.impl.UserServiceImpl;
import org.junit.Test;

import static org.junit.Assert.*;

public class UserServiceTest {

    UserService userService =new UserServiceImpl();
    @Test
    public void registUser() {
        userService.registUser(new User(null,"cgg123","jsdx110","ucas.com"));
        userService.registUser(new User(null,"lj123","jsdx110","jsu.com"));
    }

    @Test
    public void login() {
        System.out.println(userService.login(new User(null,"lj123","jsdx110","jsu.com")));
    }

    @Test
    public void existsUsername() {
        if(userService.existsUsername("cgg123")){
            System.out.println("用户名存在！！");
        }
        else{
            System.out.println("用户名可用！！");
        }
    }
}