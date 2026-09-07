from fastapi import FastAPI, Depends
from conexion import get_connection, initDb
import sqlite3
from models.Producto import Producto
from managers.managerProductos import ManagerProductos

managerProductos = ManagerProductos()
app = FastAPI()

@app.on_event("startup")
def startup():
    print("Inicializando DB")
    initDb()

#py -m venv env
#env/Scripts/activate
#py -m pip install "fastapi[standard]"
#Correr api -> fastapi dev main.py

#CRUD -> Hicimos Create, Read y Delete

@app.post("/agregar_producto")
def postProduct(producto: Producto, conexion: sqlite3.Connection = Depends(get_connection)):
    return managerProductos.postProduto(producto, conexion)

@app.get("/leer_productos")
def getProducts():
    conexion = get_connection()
    res = conexion.execute("SELECT * FROM productos").fetchall()
    conexion.close()
    return [dict(item) for item in res]

#UPDATE
#@app.put("")
    
@app.delete("/eliminar_producto/{id}")
def deleteProduct(id: int):
    conexion = get_connection()
    conexion.execute("DELETE FROM productos WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    return f"Se elimino el producto con id {id}"

@app.get("/")
def read_root():
    return "Hello World"