package com.app.proyecto_final_dbp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;
import java.util.Map;

public class PacienteMainActivity extends AppCompatActivity {

    DatabaseReference mRootReference;
    Button mButtonSubir;
    EditText nombreP;
    EditText DNIP;
    EditText edadP;
    EditText enfermadadP;
    CheckBox yesP;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_paciente_main);

        mButtonSubir = findViewById(R.id.subirDatos);
        mRootReference = FirebaseDatabase.getInstance().getReference();

        nombreP = findViewById(R.id.nombre_paciente_main);
        DNIP = findViewById(R.id.dni_paciente_main);
        edadP = findViewById(R.id.edad_paciente_main);
        enfermadadP = findViewById(R.id.enfermedad_paciente_main);
        yesP = findViewById(R.id.yes_box);

        mButtonSubir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String mensaje;
                String nombre = nombreP.getText().toString();
                int DNI = Integer.parseInt(DNIP.getText().toString());
                int Edad = Integer.parseInt(edadP.getText().toString());
                String Enfermedad = enfermadadP.getText().toString();
                String Discapacidad;
                boolean TDiscapacidad = yesP.isChecked();
                if(TDiscapacidad){
                    Discapacidad = "Si tiene una discapacidad";
                }else{
                    Discapacidad = "No tiene una discapacidad";
                }
                subirDatos(nombre, DNI, Edad, Enfermedad, Discapacidad);

            }
        });
    }

    private void subirDatos(String nombre, int DNI, int edad, String enfermedad, String discapacidad) {
        Map<String, Object> datosPaciente = new HashMap<>();
        datosPaciente.put("Nombre", nombre);
        datosPaciente.put("DNI", DNI);
        datosPaciente.put("Edad", edad);
        datosPaciente.put("Enfermedad", enfermedad);
        datosPaciente.put("Discapcidad", discapacidad);
        mRootReference.child("Paciente").push().setValue(datosPaciente);
        Toast.makeText(getApplicationContext(),"Datos enviados correctamente!",Toast.LENGTH_SHORT).show();
    }
}