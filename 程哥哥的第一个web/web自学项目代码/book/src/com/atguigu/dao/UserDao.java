package com.atguigu.dao;

import com.atguigu.pojo.User;

public interface UserDao {

    public User queryUserByUsername(String user);

    public User queryUserByUsernameAndPassword(String username,String password);

    public int SaveUser(User user);

}
