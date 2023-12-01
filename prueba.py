from flask import Flask, jsonify , render_template , request , redirect , url_for 
from db import db
from Datos import Datos
class Programa:

    def __init__(self):

        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datos.sqlite3'

        db.init_app(self.app)
        
        self.app.add_url_rule('/', view_func=self.buscarD )
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"] )

        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)
    
    def buscarD(self):
        return render_template('mostrarTodos.html', datos=Datos.query.all())
         
    def agregar(self):

        if request.method=="POST":
            nombre=request.form['nombre']
            lat= float(request.form['lat'])           
            lng= float(request.form['lng'])
            des=request.form['des']
            miDato=Datos(nombre, lat, lng, des)  
            db.session.add(miDato)
            db.session.commit()
    
            return redirect(url_for('buscarD'))
        return render_template('Prueba.html')



        
    

miPrograma=Programa()