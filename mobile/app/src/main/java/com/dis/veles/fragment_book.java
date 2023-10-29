package com.dis.veles;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.androidnetworking.AndroidNetworking;
import com.androidnetworking.error.ANError;
import com.androidnetworking.interfaces.JSONArrayRequestListener;
import com.androidnetworking.interfaces.JSONObjectRequestListener;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;

public class fragment_book extends Fragment {
    public fragment_book(){
        super(R.layout.fragment_activity_book);
    }
    public String USER_API = "https://api.jsonserve.com/5AlYhe";
    //public String USER_API = "https://api.jsonserve.com/q9_NFr";
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        ArrayList<Card> cards = new ArrayList<Card>();

            RecyclerView recyclerView = view.findViewById(R.id.list2);
            AndroidNetworking.initialize(getContext());

            AndroidNetworking.get(USER_API)
                    .build()
                    .getAsJSONArray(new JSONArrayRequestListener() {
                        @Override
                        public void onResponse(JSONArray response) {

                            if(response == null){
                                return;
                            }
                            UserAdapterBook userAdapter = new UserAdapterBook(getContext(), response);
                            recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
                            recyclerView.setAdapter(userAdapter);
                            TextView count = view.findViewById(R.id.count);
                            count.setText("Доступно документов: " + String.valueOf(recyclerView.getAdapter().getItemCount()));
                        }




                        @Override
                        public void onError(ANError anError) {
                            // error handling goes here
                            Toast.makeText(getContext(), "Error!",Toast.LENGTH_SHORT).show();
                        }
                    });

        }
    }

