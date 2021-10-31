package com.atguigu.utils;

import org.apache.commons.beanutils.BeanUtils;

import java.lang.reflect.InvocationTargetException;
import java.util.Map;

public class WebUtils {
    public static <T> T copyParmToBean(Map mapvalue, T bean){
        try {
            System.out.println("注入之前："+bean);
            BeanUtils.populate(bean,mapvalue);
            System.out.println("注入之后："+bean);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }
        return bean;
    }

}
