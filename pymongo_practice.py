from pymongo import MongoClient
import pprint

cliente = MongoClient("mongodb://localhost:27017")
db = cliente.universidad
curso = db.curso

cur = {"curso":"A1", "grp":"C", "hora": "14:00"}

result = curso.insert_one(cur)

if result.acknowledged:
    print("Curso Agregado. El id es " + str(result.inserted_id) )