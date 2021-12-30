package com.app.proyecto_final_dbp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import java.util.ArrayList;
import java.util.List;

import ahmed.easyslider.EasySlider;
import ahmed.easyslider.SliderItem;


public class MainActivity extends AppCompatActivity {
    EasySlider Slider;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Slider=findViewById(R.id.slide);

        List<SliderItem> Sliders=new ArrayList<>();

        Sliders.add(new SliderItem("¡Bienvenido!",R.drawable.slid1));
        Sliders.add(new SliderItem("¡Welcome!",R.drawable.slid2));
        Sliders.add(new SliderItem("¡Bienvenido!",R.drawable.slid3));
        Sliders.add(new SliderItem("¡Welcome!",R.drawable.slid4));

        Slider.setPages(Sliders);
    }

    public void openPacienteHome(View view) {
        Intent i = new Intent(this, PacienteHomeActivity.class);
        startActivity(i);
    }

    public void openDoctorHome(View view){
        Intent i = new Intent(this, DoctorHomeActivity.class);
        startActivity(i);
    }
}