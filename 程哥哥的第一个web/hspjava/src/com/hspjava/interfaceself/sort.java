package com.hspjava.interfaceself;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * @author 程哥哥
 * @version 1.0
 */
public class sort {
    public static void main(String[] args) {
        List list = new ArrayList<>();
        list.add(new Person("小明",30));
        list.add(new Person("小王",24));
        list.add(new Person("小李",35));
        list.sort(new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Person per1= (Person)o1;
                Person per2= (Person)o2;
                return per2.getAge()-per1.getAge();
            }
        });
        for (Object p:list){
            System.out.println(p);
        }
    }
}
class Person{
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Person() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
