package com.app.proyecto_final_dbp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ListView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class DoctorMainActivity extends AppCompatActivity {

    DatabaseReference mRootReference;
    private ListView mListView;
    private final List<PacienteDatos> mLista = new ArrayList<>();
    ListAdapter mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_doctor_main);

        mListView = findViewById(R.id.listView);

        mRootReference = FirebaseDatabase.getInstance().getReference();

        mRootReference.child("Paciente").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                for(DataSnapshot snapshot : dataSnapshot.getChildren()){
                    PacienteDatos paciente = snapshot.getValue(PacienteDatos.class);
                    mLista.add(new PacienteDatos(paciente.getDiscapacidad(),paciente.getNombre(),paciente.getEnfermedad(),paciente.getDNI(),paciente.getEdad()));
                }
                mAdapter = new ListAdapter(DoctorMainActivity.this,R.layout.pacient_row,mLista);
                mListView.setAdapter(mAdapter);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
            }

        });
    }
}