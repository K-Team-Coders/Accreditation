package com.dis.veles;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class UserAdapter extends RecyclerView.Adapter<UserAdapter.UserViewHolder> {

    Context context;
    JSONArray userJsonArray;

    public UserAdapter(Context context, JSONArray userJsonArray) {
        this.context = context;
        this.userJsonArray = userJsonArray;
    }

    @NonNull
    @Override
    public UserViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new UserViewHolder(LayoutInflater.from(parent.getContext()).inflate(R.layout.card_table, parent, false));
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
            holder.id.setText(jsonObject.getString("id"));
            holder.standart.setText(jsonObject.getString("docs"));
            holder.product.setText(jsonObject.getString("group"));
            holder.code.setText(jsonObject.getString("tnved"));
            holder.ob.setText(jsonObject.getString("equipment_user_len"));
            holder.ob_gost.setText(jsonObject.getString("equipment_find_len"));
            holder.sot.setText(String.valueOf(100*Float.parseFloat(jsonObject.getString("similarity_score"))));
        } catch (JSONException e) {
            e.printStackTrace();
        }

    }

    @Override
    public int getItemCount() {
        return userJsonArray.length();
    }

    class UserViewHolder extends RecyclerView.ViewHolder{

         TextView id,standart, product,code,ob,ob_gost,sot;

        UserViewHolder(@NonNull View view) {
            super(view);

            id = view.findViewById(R.id.id_txt);
            standart = view.findViewById(R.id.gost_txt);
            product = view.findViewById(R.id.prod_txt);
            code = view.findViewById(R.id.code_txt);
            ob = view.findViewById(R.id.ob_txt);
            ob_gost = view.findViewById(R.id.ob_txt2);
            sot = view.findViewById(R.id.sot_txt);


        }
    }
}
