package com.hspjava.jdkyuan;

public class Innerclass {
    public static void main(String[] args) {
        Cellphone cellphone = new Cellphone();
        cellphone.alarmclock(new Bell() {
            @Override
            public void ring() {
                System.out.println("臭宝我好想你");
            }
        });
    }
    interface Bell{
        public void ring();
    }
    static class Cellphone{
        public void alarmclock(Bell bell) {
            bell.ring();
        }
    }
}
