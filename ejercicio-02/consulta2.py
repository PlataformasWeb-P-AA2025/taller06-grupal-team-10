from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Pais

from ingresa_data import engine

Session = sessionmaker(bind=engine)
session = Session()



print("Presentación de los países de Asía, ordenados por el atributo Dial.")



#Presentar los países de Asía, ordenados por el atributo Dial.

#Obtenemos de la tabla Pais los objetos con continente Asia y los ordenamos por Dial
paisesAsia = session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()
print(paisesAsia)


print("--------------------------------")
