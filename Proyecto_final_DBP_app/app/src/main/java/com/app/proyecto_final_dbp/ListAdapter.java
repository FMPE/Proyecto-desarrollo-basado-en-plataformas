package com.app.proyecto_final_dbp;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.util.List;

public class ListAdapter extends ArrayAdapter<PacienteDatos> {

    private final List<PacienteDatos> mList;
    private final Context mContext;
    private final int resourceLayout;
    public ListAdapter(@NonNull Context context, int resource, List<PacienteDatos> objects) {
        super(context, resource, objects);
        this.mList = objects;
        this.mContext = context;
        this.resourceLayout = resource;
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        View view = convertView;

        if(view == null)
            view = LayoutInflater.from(mContext).inflate(resourceLayout, null);

        PacienteDatos pacientedatos = mList.get(position);

        TextView Nombre = view.findViewById(R.id.tpv1);
        Nombre.setText(pacientedatos.getNombre());

        TextView DNI = view.findViewById(R.id.tpv2);
        DNI.setText(pacientedatos.getDNI());

        TextView Edad = view.findViewById(R.id.tpv3);
        Edad.setText(pacientedatos.getEdad());

        TextView Enfermedad = view.findViewById(R.id.tpv4);
        Enfermedad.setText(pacientedatos.getEnfermedad());

        TextView Discapacidad = view.findViewById(R.id.tpv5);
        Discapacidad.setText(pacientedatos.getDiscapacidad());

        return view;
    }
}
