from flask import Flask , render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://adrian@localhost:5432/proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class PACIENTE(db.Model):
   __tablename__= 'paciente'
   dni = db.Column(db.Integer, primary_key=True)
   nombre = db.Column(db.String(), nullable=False)
   edad = db.Column(db.Integer(), nullable=False)
   caso = db.Column(db.String(), nullable=False)
   doctor = db.Column(db.String())
   def __repr__(self):
      return f'<PACIENTE: {self.dni}, {self.nombre}, {self.edad}, {self.caso}, {self.doctor}>'


class DOCTOR(db.Model):
   __tablename__= 'doctor'
   dni = db.Column(db.Integer, primary_key=True)
   password = db.Column(db.String(), nullable=False)
   numero = db.Column(db.Integer(), nullable=False)
   def __repr__(self):
      return f'<DOCTOR: {self.dni}, {self.password}>'


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
      caso = request.get_json()['especialidad']
      paciente = PACIENTE(dni=dni, nombre=nombre, edad=edad, caso=caso)
      db.session.add(paciente)
      db.session.commit()
      return jsonify({
         "DNI": paciente.dni
      })
   except:
      db.session.rollback()
   finally:
      db.session.close()


@app.route('/doctor/crear', methods=['POST'])
def crear_doctor():
   print("doctor")
   try:
      dni = request.get_json()['DNI']
      password = request.get_json()['contrasenha']
      numero= request.get_json()['numero']
      doctor = DOCTOR(dni=dni, password=password, numero=numero)
      db.session.add(doctor)
      db.session.commit()
      return jsonify({
         "DNI": doctor.dni
      })
   except:
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
         return redirect(url_for('doctor_home'))
      else:
         return redirect(url_for('doctor_error'))
   else:
      return redirect(url_for('doctor_error'))





@app.route('/home/actualizar', methods=['POST'])
def actualizar():
   dni = request.form.get("DNI", "")
   nombre = request.form.get("nombre", "")
   edad = request.form.get("edad", "")
   caso = request.form.get("especialidad", "")
   paciente = PACIENTE.query.filter_by(dni=dni).first()
   if paciente != None:
      if nombre != "":
         paciente.nombre = nombre
      if edad != "":
         paciente.edad = edad
      if caso != "":
         paciente.caso = caso
      db.session.commit()
      return redirect(url_for('doctor_home'))
   else:
      return redirect(url_for('doctor_home'))

@app.route('/home/borrar', methods=['POST'])
def borrar():
   dni = request.form.get("DNI", "")
   paciente = PACIENTE.query.filter_by(dni=dni).first()
   if paciente != None:
      db.session.delete(paciente)
      db.session.commit()
      return redirect(url_for('doctor_home'))
   else:
      return redirect(url_for('doctor_home'))

@app.route('/paciente')
def para_pacientes():
   pacientes = PACIENTE.query.all()
   return render_template('paciente.html', data=pacientes)

@app.route('/doctor')
def para_doctores():
   return render_template('doctor.html')

@app.route('/doctor/home')
def doctor_home():
   pacientes = PACIENTE.query.all()
   return render_template('home.html', data=pacientes)

@app.route('/doctor/error')
def doctor_error():
   doctor=DOCTOR.query.all()
   return render_template('error.html', data=doctor)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True, port=5010)