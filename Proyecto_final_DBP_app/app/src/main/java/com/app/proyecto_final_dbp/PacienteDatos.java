package com.app.proyecto_final_dbp;

public class PacienteDatos {

    private String Discapacidad;
    private  String Nombre;
    private  String Enfermedad;
    private  int DNI;
    private  int Edad;

    public PacienteDatos() {
    }

    public PacienteDatos(String discapacidad, String nombre, String enfermedad, int DNI, int edad) {
        Discapacidad = discapacidad;
        Nombre = nombre;
        Enfermedad = enfermedad;
        this.DNI = DNI;
        Edad = edad;
    }

    public String getDiscapacidad() {
        return Discapacidad;
    }

    public void setDiscapacidad(String discapacidad) {
        Discapacidad = discapacidad;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String nombre) {
        Nombre = nombre;
    }

    public String getEnfermedad() {
        return Enfermedad;
    }

    public void setEnfermedad(String enfermedad) {
        Enfermedad = enfermedad;
    }

    public int getDNI() {
        return DNI;
    }

    public void setDNI(int DNI) {
        this.DNI = DNI;
    }

    public int getEdad() {
        return Edad;
    }

    public void setEdad(int edad) {
        Edad = edad;
    }

}
