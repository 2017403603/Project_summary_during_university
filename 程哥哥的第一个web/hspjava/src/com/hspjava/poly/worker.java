package com.hspjava.poly;

public class worker extends Employee {
    public worker(String name, double monthSalary) {
        super(name, monthSalary);
    }
    public void work(){
        System.out.println("普通工人"+getName() + "正在工作");
    }

    @Override
    public double getAnnual() {
        return super.getAnnual();
    }
}
