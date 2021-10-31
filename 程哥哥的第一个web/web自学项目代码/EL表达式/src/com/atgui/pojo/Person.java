package com.atgui.pojo;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class Person {
    private int id;
    private String[] phones;
    private List<String> cities;
    private Map<String,Object> map;

    public Person() {
    }

    public Person(int id, String[] phones, List<String> cities, Map<String, Object> map) {
        this.id = id;
        this.phones = phones;
        this.cities = cities;
        this.map = map;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String[] getPhones() {
        return phones;
    }

    public void setPhones(String[] phones) {
        this.phones = phones;
    }

    public List<String> getCities() {
        return cities;
    }

    public void setCities(List<String> cities) {
        this.cities = cities;
    }

    public Map<String, Object> getMap() {
        return map;
    }

    public void setMap(Map<String, Object> map) {
        this.map = map;
    }

    @Override
    public String toString() {
        return "person{" +
                "id=" + id +
                ", phones=" + Arrays.toString(phones) +
                ", cities=" + cities +
                ", map=" + map +
                '}';
    }
}
