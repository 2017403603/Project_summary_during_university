package com.hspjava.poly;

public class manager extends Employee{
    private double bonus;
    public manager(String name, double monthSalary, double bonus) {
        super(name, monthSalary);
        this.bonus = bonus;
    }
    public void manage(){
        System.out.println("经理"+getName()+"正在管理");
    }

    @Override
    public double getAnnual() {
        return super.getAnnual()+bonus;
    }
}
