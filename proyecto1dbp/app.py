from flask import Flask , render_template, request, redirect, url_for, jsonify

from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ilussia123@localhost:5432/e1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
##migrate = Migrate(app,db)
doctor_dni = 0
 
class PACIENTE(db.Model):
  __tablename__= 'pacientes'
  dni = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(), nullable=False)
  edad = db.Column(db.Integer(), nullable=False)
  sexo = db.Column(db.String(), nullable=False)
  caso = db.Column(db.String(), nullable=False)
  doctor = db.Column(db.Integer, db.ForeignKey('doctores.dni'), nullable=False)
  def __repr__(self):
     return f'<PACIENTE: {self.dni}, {self.nombre}, {self.edad},{self.sexo} , {self.caso}>'

class CONSULTA(db.Model):
  __tablename__= 'consultas'
  dni = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(), nullable=False)
  dia = db.Column(db.Integer, nullable=False)
  mes = db.Column(db.Integer, nullable=False)
  numero = db.Column(db.Integer, nullable=False)
  completed = db.Column(db.Boolean, nullable=False, default=False)
  doctor = db.Column(db.Integer, db.ForeignKey('doctores.dni'), nullable=False)
  def __repr__(self):
     return f'<CONSULTA: {self.dni}, {self.nombre}, {self.dia}, {self.mes}, {self.numero}>'

class DOCTOR(db.Model):
  __tablename__= 'doctores'
  dni = db.Column(db.Integer, primary_key=True)
  password = db.Column(db.String(), nullable=False)
  nombre = db.Column(db.String(), nullable=False)
  edad = db.Column(db.Integer(), nullable=False)
  sexo = db.Column(db.String(), nullable=False)
  especialidad = db.Column(db.String(), nullable=False)
  pacientes = db.relationship('PACIENTE', backref='Doctor', lazy=True)
  consultas = db.relationship('CONSULTA', backref='Doctor', lazy=True)
  def __repr__(self):
     return f'<DOCTOR: {self.dni}, {self.password}, {self.nombre}, {self.edad}, {self.sexo}, {self.especialidad}>'
 
 
db.create_all()
 
#d1 = DOCTOR(dni=12345697, password="qwerty")
#db.session.add(d1)
 
@app.route('/paciente/crear', methods=['POST'])
def crear_paciente():
  print("crear_paciente")
  try:
     dni = request.get_json()['DNI']
     nombre = request.get_json()['nombre']
     edad = request.get_json()['edad']
     sexo = request.get_json()['sexo']
     caso = request.get_json()['caso']
     doctor = request.get_json()['doctor_dni']
     paciente = PACIENTE(dni=dni, nombre=nombre, edad=edad, sexo=sexo, caso=caso, doctor=doctor)
     db.session.add(paciente)
     db.session.commit()
     return jsonify({
        "DNI": paciente.dni
     })
  except Exception as e:
      print(e)
      db.session.rollback()
  finally:
     db.session.close()

@app.route('/consulta/crear', methods=['POST'])
def crear_consulta():
  print("consulta")
  try:
     dni = request.get_json()['DNI']
     nombre = request.get_json()['nombre']
     dia = request.get_json()['dia']
     mes = request.get_json()['mes']
     numero = request.get_json()['numero']
     doctor = request.get_json()['doctor_dni']
     consulta = CONSULTA(dni=dni, nombre=nombre, dia=dia, mes=mes, numero=numero, doctor=doctor)
     db.session.add(consulta)
     db.session.commit()
     return jsonify({
        "DNI": consulta.dni,
        "nombre": consulta.nombre,
        "dia": consulta.dia,
        "mes": consulta.mes,
        "numero": consulta.numero,
        "completed": consulta.completed
     })
  except Exception as e:
      print(e)
      db.session.rollback()
  finally:
      db.session.close()
 
@app.route('/doctor/crear', methods=['POST'])
def crear_doctor():
  print("doctor")
  try:
     dni = request.get_json()['DNI']
     password = request.get_json()['contrasenha']
     nombre= request.get_json()['nombre']
     edad = request.get_json()['edad']
     sexo = request.get_json()['sexo']
     especialidad = request.get_json()['especialidad']
     doctor = DOCTOR(dni=dni, password=password, nombre=nombre, edad=edad, sexo=sexo, especialidad=especialidad)
     db.session.add(doctor)
     db.session.commit()
     return jsonify({
        "DNI": doctor.dni
     })
  except Exception as e:
      print(e)
      db.session.rollback()
  finally:
     db.session.close()
 
 
@app.route('/doctor/login', methods=['POST'])
def logear_doctor():
  print("logeado")
  dni = request.form.get("DNI", "")
  password = request.form.get("contrasenha", "")
  doctor = DOCTOR.query.filter_by(dni=dni).first()
  if doctor != None:
     if doctor.password == password:
        print("logeado")
        return redirect(url_for('doctor_home', doc_dni=doctor.dni))
     else:
        return redirect(url_for('doctor_error'))
  else:
     return redirect(url_for('doctor_error'))

 
@app.route('/home/actualizar', methods=['POST'])
def actualizar():
  dni = request.form.get("DNI", "")
  nombre = request.form.get("nombre", "")
  edad = request.form.get("edad", "")
  sexo = request.form.get("sexo", "")
  caso = request.form.get("caso", "")
  paciente = PACIENTE.query.filter_by(dni=dni).first()
  if paciente != None:
      if nombre != "":
         paciente.nombre = nombre
      if edad != "":
         paciente.edad = edad
      if sexo != "":
         paciente.sexo = sexo
      if caso != "":
         paciente.caso = caso
      db.session.commit()
      return redirect(url_for('doctor_home', doc_dni=paciente.doctor))
  else:
     return redirect(url_for('doctor_home', doc_dni=paciente.doctor))
 
@app.route('/home/borrar', methods=['POST'])
def borrar():
  dni = request.form.get("DNI", "")
  paciente = PACIENTE.query.filter_by(dni=dni).first()
  if paciente != None:
     db.session.delete(paciente)
     db.session.commit()
     return redirect(url_for('doctor_home', doc_dni=paciente.doctor))
  else:
     return redirect(url_for('doctor_home', doc_dni=paciente.doctor))

@app.route('/home/<consulta_dni>/complete-consulta', methods=['POST'])
def complete_consulta(consulta_dni):
    try:
        new_completed = request.get_json()['completed']
        consulta = CONSULTA.query.get(consulta_dni)
        consulta.completed = new_completed
        print("completado")
        db.session.commit()
        print("completado")
    except Exception as e:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('doctor_home', doc_dni=doctor_dni))

@app.route('/home/<consulta_dni>/delete-consulta', methods=['DELETE'])
def delete_consulta(consulta_dni):
    try:
        consulta = CONSULTA.query.get(consulta_dni)
        db.session.delete(consulta)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({'success': True})

@app.route('/paciente')
def para_pacientes():
  doctores = DOCTOR.query.all()
  return render_template('paciente.html', data=doctores)

@app.route('/consulta')
def para_consultas():
   doctores = DOCTOR.query.all()
   return render_template('consulta.html', data=doctores)

@app.route('/doctor')
def para_doctores():
  return render_template('doctor.html')
 
@app.route('/doctor/home/<doc_dni>', methods=['GET'])
def doctor_home(doc_dni):
   doctor_dni = doc_dni
   return render_template('home.html',
      pacientes = PACIENTE.query.filter_by(doctor=doctor_dni).order_by('dni').all(),
      consultas = CONSULTA.query.filter_by(doctor=doctor_dni).order_by('dni').all(),
      doctor_dni = doc_dni
   )
 
@app.route('/doctor/error')
def doctor_error():
  doctor=DOCTOR.query.all()
  return render_template('error.html', data=doctor)
 
@app.route('/')
def index():
  return render_template('index.html')
 
if __name__ == '__main__':
  app.run(debug = True, port=5000)
