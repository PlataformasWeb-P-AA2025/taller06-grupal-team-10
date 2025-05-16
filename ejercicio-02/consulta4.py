from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# importa la clase Pais desde el archivo genera_base 
from genera_base import Pais

#trae la coneccion de la base de datos a traves de engine
from ingresa_data import engine

Session = sessionmaker(bind=engine)
session = Session()





#Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
print("Países ordenados por la capital, siempre que el país pertenezca a Europa")

#filtramos los paises del contienente europa con EU y los ordenamos por su capital
paisesEu = session.query(Pais).filter(Pais.continente=="EU").order_by(Pais.capital).all()
print(paisesEu)


print("--------------------------------")