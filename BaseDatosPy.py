# importing required libraries
from datetime import date
from sre_constants import BRANCH
import mysql.connector
  

# Coneccion a la base de datos MySQL
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Ramirito-51",
  database = "BaseDatosPy"
)

def crearTableTeacher():
  # Creo la tabla en la base de datos
  teacherRecord = """CREATE TABLE TEACHER (
                   NAME  VARCHAR(20) NOT NULL,
                   LASTNAME VARCHAR(50),
                   CEDULA INT NOT NULL,
                   USERNAME VARCHAR(15),
                   EDAD INT
                   )"""
  # manda a executar en la base de datos el comando de my SQL que le envio
  cursorObject.execute(teacherRecord)

def insertData(name,lastName,cedula,userName,edad):
  sql = "INSERT INTO TEACHER (NAME, LASTNAME, CEDULA, USERNAME, EDAD)\
    VALUES (%s, %s, %s, %s, %s)"
  val = [(name,lastName,cedula,userName,edad)]
  cursorObject.executemany(sql, val)
  dataBase.commit()
# disconnecting from server  

def selectData():
  query = """SELECT NAME,USERNAME FROM TEACHER"""
  cursorObject.execute(query)
  myresult = cursorObject.fetchall()
  for x in myresult:
    print(x)

def updateData():
  dataUpdate = input("Ingrese el nombre de usuario del profesor que desea actualizar\n")
  dateToUpdate = int(input("Eliga el datos que desea modificar:\n" +
                "1.Nombre\n2.Apellido\n3.Cedula\n4.UserName\n5.Edad\n"))
  data = ""
  if dateToUpdate == 1:
    data = "NAME"
  elif dateToUpdate == 2:
    data = "LASTNAME"
  elif dateToUpdate == 3:
    data = "CEDULA"
  elif dateToUpdate == 4:
    data = "CEDULA"
  elif dateToUpdate == 5:
    data = "EDAD"
  else:
    print("Eleccion fuera del rango")
  dataOfAtribute= input("Ingrese el dato por el cual va a reemplazar: ")
  query = "UPDATE TEACHER SET "+  data +" = '"+str(dataOfAtribute) + "' WHERE USERNAME = '" + str(dataUpdate) +"'"
  print(query)
  cursorObject.execute(query)
  dataBase.commit()

# Preparando un cursoObject
cursorObject = dataBase.cursor()
opcion = int(input("Ingrese la opcion que desee realizar:\n" +
      "1.Agregar un profesor a la base de datos.\n" +
      "2.Actualizar registros de la base de datos\n" + 
      "3.Consultar informacion de la base de datos\n"
      "4.Crear tabla de profesores\n"))
if opcion == 1:
    name= input("Nombre del profesor: ")
    lastName= input("Apellido del profesor: ")
    cedula= input("Cedula del profesor: ")
    userName= input("Nombre de usuario del profesor: ")
    edad= input("Edad del profesor: ")
    insertData(name,lastName,cedula,userName,edad)
elif opcion == 2:
    updateData()
elif opcion == 3:
    selectData()
elif opcion == 4:
    crearTableTeacher()
else:
    print("Eligio una opcion fuera del rango")

# Me desconecto de la base de datos
dataBase.close()