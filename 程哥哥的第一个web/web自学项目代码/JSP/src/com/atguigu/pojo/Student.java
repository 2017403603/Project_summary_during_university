package com.atguigu.pojo;

public class Student {
    private Integer id;
    private String name;
    private Integer age;
    private String phnoe;

    public Student() {
    }

    public Student(Integer id, String name, Integer age, String phnoe) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.phnoe = phnoe;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getPhnoe() {
        return phnoe;
    }

    public void setPhnoe(String phnoe) {
        this.phnoe = phnoe;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", phnoe='" + phnoe + '\'' +
                '}';
    }
}
