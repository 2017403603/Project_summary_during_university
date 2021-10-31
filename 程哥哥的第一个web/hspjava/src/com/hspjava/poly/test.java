package com.hspjava.poly;

public class test {
    public static void main(String[] args) {
        worker tom = new worker("tom", 1000);
        manager smith = new manager("smith", 2000, 100000);
        test test1 = new test();
        test1.showEmpAnnual(tom);
        test1.showEmpAnnual(smith);
        test1.testWork(tom);
        test1.testWork(smith);
    }
    public void showEmpAnnual(Employee e){
        System.out.println(e.getAnnual());
    }
    public void testWork(Employee e){
        if(e instanceof worker){
            ((worker)e).work();
        }
        else if(e instanceof manager){
            ((manager)e).manage();
        }
    }
}
