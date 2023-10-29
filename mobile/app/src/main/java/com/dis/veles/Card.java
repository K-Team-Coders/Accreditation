package com.dis.veles;

public class Card {
    private String id; // id
    private String standart;  // обозначение стандарта
    private String product;  // название проукта
    private String code;  // ОКПД2/ТНВЕД
    private String ob;  // тех оборудование
    private String ob_gost;  // тех оборудование по госту
    private String sot;  // % оответствия
    public Card(String id, String standart, String product, String code, String ob, String ob_gost, String sot ){

        this.id=id;
        this.standart=standart;
        this.product=product;
        this.code=code;
        this.ob=ob;
        this.ob_gost=ob_gost;
        this.sot=sot;
    }
    public String getID() { return this.id; }
    public String getStandart() { return this.standart; }
    public String getProduct() { return this.product; }
    public String getCode() { return this.code; }
    public String getOb() { return this.ob; }
    public String getOb_gost() { return this.ob_gost; }
    public String getSot() { return this.sot; }
}
