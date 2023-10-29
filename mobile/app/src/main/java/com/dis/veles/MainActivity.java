package com.dis.veles;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.LinearLayout;


public class MainActivity extends AppCompatActivity {
    public LinearLayout searchBTN;
    public LinearLayout tableBTN;
    public LinearLayout bookBTN;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        searchBTN = findViewById(R.id.searchBtn);
        tableBTN = findViewById(R.id.tableBtn);
        bookBTN = findViewById(R.id.bookBtn);
        searchBTN.setBackgroundColor(getResources().getColor(R.color.main_pink));
        tableBTN.setBackgroundColor(getResources().getColor(R.color.main_gray));
        bookBTN.setBackgroundColor(getResources().getColor(R.color.main_gray));
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.container, fragment_search.class, null)
                .commit();
    }
    public void OnSearchClick (View v){
        searchBTN.setBackgroundColor(getResources().getColor(R.color.main_pink));
        tableBTN.setBackgroundColor(getResources().getColor(R.color.main_gray));
        bookBTN.setBackgroundColor(getResources().getColor(R.color.main_gray));
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.container, fragment_search.class, null)
                .commit();
    }
    public void OnTableClick (View v){
        searchBTN.setBackgroundColor(getResources().getColor(R.color.main_gray));
        tableBTN.setBackgroundColor(getResources().getColor(R.color.main_pink));
        bookBTN.setBackgroundColor(getResources().getColor(R.color.main_gray));
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.container, fragment_table.class, null)
                .commit();
    }

    public void OnBookClick (View v){
        searchBTN.setBackgroundColor(getResources().getColor(R.color.main_gray));
        tableBTN.setBackgroundColor(getResources().getColor(R.color.main_gray));
        bookBTN.setBackgroundColor(getResources().getColor(R.color.main_pink));
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.container, fragment_book.class, null)
                .commit();
    }
}