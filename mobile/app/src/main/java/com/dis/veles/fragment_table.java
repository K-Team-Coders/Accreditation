package com.dis.veles;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.androidnetworking.AndroidNetworking;
import com.androidnetworking.error.ANError;
import com.androidnetworking.interfaces.JSONArrayRequestListener;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class fragment_table extends Fragment {
    public fragment_table(){
        super(R.layout.fragment_activity_table);
    }

    public String USER_API = "https://api.jsonserve.com/MpiapF";

    // contacts JSONArray

    ArrayList<Card> cards = new ArrayList<Card>();
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        RecyclerView recyclerView = view.findViewById(R.id.list);
        AndroidNetworking.initialize(getContext());

        AndroidNetworking.get(USER_API)
                .build()
                .getAsJSONArray(new JSONArrayRequestListener() {
                    @Override
                    public void onResponse(JSONArray response) {

                        if(response == null){
                            return;
                        }
                        UserAdapter userAdapter = new UserAdapter(getContext(), response);
                        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
                        recyclerView.setAdapter(userAdapter);
                    }


                    @Override
                    public void onError(ANError anError) {
                        // error handling goes here
                        Toast.makeText(getContext(), "Error!",Toast.LENGTH_SHORT).show();
                    }
                });

    }



        }



