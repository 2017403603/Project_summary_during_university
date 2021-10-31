package com.hspjava.interfaceself;

import java.util.*;

/**
 * @author 程哥哥
 * @version 1.0
 */

public class hashset {
    public static void main(String[] args) {
        Map hashmap = new HashMap();
        hashmap.put(1,new Empolyee("小明",60.0,new Empolyee().newMyDate(1998, 12, 17)));
        hashmap.put(2,new Empolyee("小王",80.0,new Empolyee().newMyDate(1999, 11, 27)));
        hashmap.put(3,new Empolyee("小明",60.0,new Empolyee().newMyDate(1998, 12, 17)));

        Set keyset = hashmap.keySet();
        for (Object key : keyset){
            Empolyee empolyee = (Empolyee) hashmap.get(key);
            System.out.println(empolyee);
        }
        Set entrySet = hashmap.entrySet();
        for (Object key : entrySet) {
            Map.Entry entry = (Map.Entry) key;
            System.out.println(entry.getValue());
        }

        Iterator iterator = entrySet.iterator();
        while (iterator.hasNext()) {
            Map.Entry entry = (Map.Entry) iterator.next();
            System.out.println(entry.getValue());
        }
    }


}
class Empolyee{
    private String name;
    private double sal;
    private MyDate mydate;

    public Empolyee() {
    }

    public Empolyee(String name, double sal, MyDate mydate) {
        this.name = name;
        this.sal = sal;
        this.mydate = mydate;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getSal() {
        return sal;
    }

    public void setSal(double sal) {
        this.sal = sal;
    }

    public MyDate getMydate() {
        return mydate;
    }

    public void setMydate(MyDate mydate) {
        this.mydate = mydate;
    }

    public MyDate newMyDate(int year,int month,int day){
        return new MyDate(year, month, day);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Empolyee empolyee = (Empolyee) o;
        return Objects.equals(name, empolyee.name) &&
                Objects.equals(mydate, empolyee.mydate);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, mydate);
    }

    @Override
    public String toString() {
        return "Empolyee{" +
                "name='" + name + '\'' +
                ", sal=" + sal +
                ", mydate=" + mydate +
                '}';
    }

    class MyDate{
        int year;
        int month;
        int day;

        public MyDate(int year, int month, int day) {
            this.year = year;
            this.month = month;
            this.day = day;
        }

        public int getYear() {
            return year;
        }

        public void setYear(int year) {
            this.year = year;
        }

        public int getMonth() {
            return month;
        }

        public void setMonth(int month) {
            this.month = month;
        }

        public int getDay() {
            return day;
        }

        public void setDay(int day) {
            this.day = day;
        }

        @Override
        public String toString() {
            return "MyDate{" +
                    "year=" + year +
                    ", month=" + month +
                    ", day=" + day +
                    '}';
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            MyDate myDate = (MyDate) o;
            return year == myDate.year &&
                    month == myDate.month &&
                    day == myDate.day;
        }

        @Override
        public int hashCode() {
            return Objects.hash(year, month, day);
        }
    }
}