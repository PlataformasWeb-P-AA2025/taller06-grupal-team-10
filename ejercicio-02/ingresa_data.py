from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests as request
from genera_base import Pais

import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basePaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

archivo = request.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
documentos = archivo.json()

for d in documentos:
    print(d)
    print(len(d.keys()))
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

    session.add(p)

# confirmar transacciones

session.commit()
