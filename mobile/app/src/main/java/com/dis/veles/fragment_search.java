package com.dis.veles;

import android.app.Activity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

public class fragment_search extends Fragment implements View.OnClickListener {
    public Button searchBtn;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View v = inflater.inflate(R.layout.fragment_activity_search, container, false);

        searchBtn = (Button) v.findViewById(R.id.searchBTN);
        searchBtn.setOnClickListener(this);
        return v;
    }
    @Override
    public void onClick(View v) {
       // Toast.makeText(getContext(), "Пора покормить кота!", Toast.LENGTH_SHORT).show();
        Fragment  child = new fragment_result_search();
        getChildFragmentManager().beginTransaction()
                .add(R.id.container2,child)
                .commit();
    }
}
