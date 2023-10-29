package com.dis.veles;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class UserAdapterBook extends RecyclerView.Adapter<UserAdapterBook.UserViewHolder> {

    Context context;
    JSONArray userJsonArray;
    TextView count;
    public UserAdapterBook(Context context, JSONArray userJsonArray) {
        this.context = context;
        this.userJsonArray = userJsonArray;
    }

    @NonNull
    @Override
    public UserViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new UserViewHolder(LayoutInflater.from(parent.getContext()).inflate(R.layout.card_book, parent, false));
    }

    @Override
    public void onBindViewHolder(@NonNull UserViewHolder holder, int position) {

        JSONObject jsonObject = null;
        try {
            jsonObject = userJsonArray.getJSONObject(position);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        try {
            // holder.gost.setText(jsonObject.getString("num"));
            holder.gost.setText(jsonObject.getString("num"));

        } catch (JSONException e) {
            e.printStackTrace();
        }

    }

    @Override
    public int getItemCount() {
        return userJsonArray.length();
    }

    class UserViewHolder extends RecyclerView.ViewHolder{

         TextView gost;


        UserViewHolder(@NonNull View view) {
            super(view);

           gost = view.findViewById(R.id.gost_txt_book);




        }
    }
}
