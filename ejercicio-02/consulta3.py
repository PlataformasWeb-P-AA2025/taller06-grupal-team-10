from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# importa la clase Pais desde el archivo genera_base 
from genera_base import Pais

#trae la coneccion de la base de datos a traves de engine
from ingresa_data import engine

Session = sessionmaker(bind=engine)
session = Session()

#Presentar los lenguajes de cada país.
print("Los lenguajes de cada país")

#obtenemos solo las columnas nombre del pais y lenguajes para mostrar que lenguaje tiene cada pais
# y el group by nos permite agruparlos por la columna lenguaje
lenguajes = session.query(Pais.nombre_pais,Pais.lenguajes).group_by(Pais.lenguajes).all()
print(lenguajes)

print("--------------------------------")
