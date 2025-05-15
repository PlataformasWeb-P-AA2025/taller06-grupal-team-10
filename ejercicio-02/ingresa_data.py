from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests as request
from genera_base import Pais

import json

# se crea conexion con la base de datos sqlite
engine = create_engine('sqlite:///basePaises.db')

# se crea la sesion para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# se descarga el json que contiene los datos de los paises
archivo = request.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

# se convierte desde json a una lista de diccionarios
documentos = archivo.json()

# se recorre cada diccionario con datos de un pais
for d in documentos:
    print(d)
    print(len(d.keys()))

    # se crea un objeto pais con esos datos
    p = Pais(
        nombre_pais=d['CLDR display name'],
        capital=d['Capital'],
        continente=d['Continent'],
        dial=d['Dial'],
        geoname_id=str(d['Geoname ID']),
        itu=d['ITU'],
        lenguajes=d['Languages'],
        independencia=d['is_independent']
    )

    # se agrega el objeto pais a la sesion para guardarlo en la base de datos
    session.add(p)

# se confirma la transaccion
session.commit()
