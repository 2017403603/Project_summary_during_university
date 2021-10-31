package com.hspjava.singleinstance;

public class zixue {
    public static void main(String[] args) {
        leader lj = leader.getinstance();
        System.out.println(lj);
    }
}

class leader {
    private String name;
    private static leader lhc = new leader("李航程");

    private leader(String name) {
        this.name = name;
    }

    public static leader getinstance() {
        return lhc;
    }
}

class cgg {
    private String name;

    private cgg(String name) {
        this.name = name;
    }

    private static cgg lhc;

    public static cgg getInstance() {
        if (lhc == null) {
            lhc = new cgg("李航程");
        }
        return lhc;
    }
}

class Hero {
    private String name;
    
    public static final int TEXT_SCORE=100;

    private Hero(String name) {
        this.name = name;
    }

    private static Hero hero = new Hero("钢铁侠");

    public static Hero getInstance() {
        return hero;
    }
}