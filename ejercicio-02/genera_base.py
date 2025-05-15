from sqlalchemy import create_engine

# se crea la conexion con la base de datos sqlite
engine = create_engine('sqlite:///basePaises.db')

from sqlalchemy.ext.declarative import declarative_base

# se crea la clase base para definir las tablas con sqlalchemy
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean

# clase que representa la tabla 'paises' en la base de datos
# contiene columnas para almacenar informacion basica de cada pais
class Pais(Base):
    __tablename__ = 'paises'

    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    independencia = Column(String)

# crea las tablas en la base de datos si no existen
Base.metadata.create_all(engine)
