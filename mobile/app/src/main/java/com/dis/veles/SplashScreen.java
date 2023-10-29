package com.dis.veles;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

import java.util.Timer;
import java.util.TimerTask;

public class SplashScreen extends Activity {
    public int count=0;
    @Override
    protected void onStart() {

        super.onStart();
        if(count==0){
        setContentView(R.layout.activity_splash);
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(getBaseContext());

        new Timer().schedule(new TimerTask() {
            @Override
            public void run() {
                startActivity(new Intent(getApplicationContext(), MainActivity.class));
            }
        }, 3000); count++;
    } else {this.finishAffinity();}
}}
