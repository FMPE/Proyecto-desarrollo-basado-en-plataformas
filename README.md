# CLÍNICA VIRTUAL


## Integrantes

* Adrian Poma Torres
* Franco Pacheco
* Luis Robledo
* Nincol Quiroz
* Paulo Cuaresma

## Descripción del proyecto 
El proyecto está orientado al sector de salud, y consiste en la creación de una página web que permita una mejor manipulación y 
obtención de data de pacientes/usuarios, con un hospital, por lo cual la página tiene un método de ingreso de datos, y opciones 
de interacción. Posteriormente, la data se guarda en la base de datos, para futuros usos.
## Objetivo/Misión/Visión
### Objetivo
Aportar al sector de salud con la una mejor manipulación en sus datos, 
para acelerar los procesos, la atención a pacientes y obtengan data más
 confiable.
### Misión
Crear una página de interacción amigable y eficiente, contar con una base 
de datos integra.
### Visión
Usar diversas tecnologías y recursos disponibles para un mejor funcionamiento 
de la página web, y la manipulación de data dentro de la base datos.

## Tecnologías 

### Front-end
* CSS
* HTML5
* JavaScript
* Fetch
### Backend
* Flask
* Flask-Migrate
* SQLAlchemy
### Base de datos 
* PostgresSQL
## Script de inicialización de la base de datos
\c proyecto
insert into doctores(dni, password, nombre, edad, sexo, especialidad) values(7234587, 1234, 'Franco', 34, 'm', 'oncologo')
insert into pacientes(dni, nombre, edad, sexo, caso, doctor) values(7390572, 'Luis', 20, 'm', 'cancer', 7234587)
insert into consultas(dni, nombre, dia, mes, numero, completed) values(8904653, 'Nincol', 4, 1, 987654321, false)
## Referencias de API
Flask-SQLAlchemy
## Hosts
Localhost:5000
## Forma de Autenticación
Nuestra aplicacion no lo soporta
## Manejo de errores
Hacemos manejo de errores utilizando fetch en nuestros endpoints y también con url_redirect desde el app.py.
## Requests y response (ENDPOINTS)
Las funciones que hacen request a los formularios en los html son:
*crear_paciente()
*crear_consulta()
*crear_doctor()
*logear_doctor()
*actualizar()
*borrar()
*complete_consulta(consulta_dni)
*delete_consulta(consulta_dni)