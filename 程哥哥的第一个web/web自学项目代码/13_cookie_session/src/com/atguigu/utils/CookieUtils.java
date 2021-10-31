package com.atguigu.utils;

import javax.servlet.http.Cookie;

public class CookieUtils {
    public static Cookie findCookie(String name,Cookie[] cookies){
        if(name==null||cookies.length == 0||cookies==null){
            return null;
        }
        for (Cookie cookie : cookies) {
            if(name.equals(cookie.getName())){
                return cookie;
            }
        }
        return null;
    }
}
