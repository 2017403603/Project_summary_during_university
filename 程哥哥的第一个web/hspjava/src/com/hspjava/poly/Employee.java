package com.hspjava.poly;

public class Employee {
    private String name;
    private double monthSalary;

    public Employee(String name, double monthSalary) {
        this.name = name;
        this.monthSalary = monthSalary;
    }

    public double getAnnual(){
        return getMonthSalary()*12.0;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getMonthSalary() {
        return monthSalary;
    }

    public void setMonthSalary(double monthSalary) {
        this.monthSalary = monthSalary;
    }
}
