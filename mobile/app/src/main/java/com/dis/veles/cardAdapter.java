package com.dis.veles;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import androidx.recyclerview.widget.RecyclerView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.List;

public class cardAdapter extends RecyclerView.Adapter<cardAdapter.ViewHolder>{

    private final LayoutInflater inflater;
    private final List<Card> cards;
public JSONArray userJsonArray;
    cardAdapter(Context context, List<Card> cards) {
        this.cards = cards;
        this.inflater = LayoutInflater.from(context);
    }
    @Override
    public cardAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {

        View view = inflater.inflate(R.layout.card_table, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(cardAdapter.ViewHolder holder, int position) {

        Card card = cards.get(position);
        holder.id.setText(card.getID());
        holder.standart.setText(card.getStandart());
        holder.product.setText(card.getProduct());
        holder.code.setText(card.getCode());
        holder.ob.setText(card.getOb());
        holder.ob_gost.setText(card.getOb_gost());
        holder.sot.setText(card.getSot());

        JSONObject jsonObject = null;
        try {
            jsonObject = userJsonArray.getJSONObject(position);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        try {
            holder.id.setText(jsonObject.getString("name"));
            holder.standart.setText(jsonObject.getString("username"));
            holder.product.setText(jsonObject.getString("phone"));
            holder.code.setText(jsonObject.getString("phone"));
            holder.ob.setText(jsonObject.getString("phone"));
            holder.ob_gost.setText(jsonObject.getString("phone"));
            holder.sot.setText(jsonObject.getString("phone"));
        } catch (JSONException e) {
            e.printStackTrace();
        }


    }

    @Override
    public int getItemCount() {
        return userJsonArray.length();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {

        final TextView id,standart, product,code,ob,ob_gost,sot;
        ViewHolder(View view){
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
