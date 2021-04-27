
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mavado18*051996",
  database="examen_final"
)
mycursor = mydb.cursor()


mycursor.execute("create table Materia(Id varchar (100) primary key, nombre_Materia Varchar (100))")





query = "INSERT INTO Materia VALUES (%s, %s)"
Values = [('1A', 'Tecnicas de programacion'),
('2A', 'Diseño 1'),
 ('3A', 'Bioestadistica'),
('4A', 'Ingles introductorio'),
('5A', 'Matematica Basica'),
('6A', 'Orientacion Medica'),
 ('7A', 'Quimica General 1'),
 ('8A', 'Fisica Basica 1'),
 ('9A', 'Quimica General 2'),
 ('10A', 'Informatica Basica')
 ]
mycursor.executemany(query, Values)
mydb.commit

consulta = "INSERT INTO Carrera (Id, nombre_carrera) Values (%d, %s)"
valores= [
(1, 'Medicina') 
 (2, 'Agrimensura'),
 (3, 'Ingenieria civil'),
 (4, 'Arquitectura'),
 (5, 'Musica'),
(6, 'Ingenieria industrial'),
 (7, 'Ingenieria en sistemas computacionales'),
 (8, 'Diseño de interiores'),
 (9, 'Psicologia Clinica'),
 (10, 'Psicologia industrial')
 ]
mycursor.executemany(consulta, valores)
mydb.commit

segunda_consulta = "INSERT INTO Materias_de_Carrera (id_Materia, Nombre_Materia_Carrera) Values (%s, %s)"
segundos_valores = [
('inf-555-01', 'Circuitos logicos'),
('inf-258-01', 'Tecnicas de programacion'),
('Mat-160', 'Algebra superior'),
('inf-158', 'Introduccion a la informatica'),
 ('mat-180', 'Geometria Analitica'),
('Hum-150', 'Historia de la cultura universal'),
('Mat-365', 'Algebra de matrices'),
('ing-224', 'Dibujo 1'),
 ('fis-211', 'Fisica General 1'),
('Hum-160', 'Historia Dominicana')
 ]
mycursor.executemany(segunda_consulta, segundos_valores)
mydb.commit


tercera_consulta = "INSERT INTO Estudiantes (Matricula, Nombre_Estudiante) values (%s, %s)"  
terceros_valores = [('15-0679', 'Luis Landeta'),
('18-0950', 'Luz Canario'),
('19-0320', 'Gabriel Villalona'),
('20-1050', 'Sandro Landeta'),
('19-0450', 'Marlem Olivo'),
('18-4500', 'Daniel Rodriguez'),
('17-1340', 'Aura rodriguez'),
('16-1560', 'Robert Furcal'),
('14-2300', 'Chantal Abreu'),
('13-1000', 'David Salomon')]
mycursor.executemany(tercera_consulta, terceros_valores)
mydb.commit



cuarta_consulta = "INSERT INTO Profesores (Id, Nombre_Profesor) values (%d, %s)"
cuartos_valores =[(1, 'Sidney Renzo Delgado'),
(2, 'David Torres'),
(3, 'Jose Ramon Romero'),
 (4, 'Pantaleon Mueses'),
(5, 'Alex Rodriguez'),
(6, 'Stephen Hawking'),
(7, 'Albert Einstein'),
 (8, 'Frederick Gauss'),
 (9, 'Rafael Peña'),
(10, 'Dominicana Asuncion')
 ]
mycursor.executemany(cuarta_consulta, cuartos_valores)
mydb.commit
quinta_consulta = "INSERT INTO materias_estudiantes (ID, nombre_materia_sesion)  values (%d, %s)"
quintos_valores = [
    (1, 'Algebra de Matrices'),
    (2, 'Calculo diferencial e integral 2'),
    (3, 'Dibujo 1'),
    (4, 'Fisica General 1'),
    (5, 'Historia Dominicana'),
    (6, 'Quimica General 1'),
    (7, 'Ingles Elemental'),
    (8, 'Instalacion y mantenimiento de microcomputadoras'),
    (9, 'Introduccion a la ingenieria de sistemas'),
    (10, 'Matematica Discreta 1')
    ]
mycursor.executemany(quinta_consulta, quintos_valores)
mydb.commit

sexta_consulta = "INSERT INTO Materias_Profesores (ID_sesion_profesor, nombre_materia_sesion_profesor) Values (%d, %s)"
sextos_valores = [
    (1, 'Circuitos logicos'),
    (2, 'Analisis y diseño de sistemas 1'),
    (3, 'Instalacion y mantenimiento de microcomputadoras'),
    (4, 'Introduccion a la ingenieria de sistemas'),
    (5, 'Matematica discreta 1'),
    (6, 'Metodos numericos'),
    (7, 'Matematica discreta 2'),
    (8, 'Tecnicas de programacion'),
    (9, 'Electronica 1'),
    (10, 'Laboratorio de electronica 1')

   ]
mycursor.executemany(sexta_consulta, sextos_valores)
mydb.commit


# Validacion de nombre de usuario y contraseña
nombre_usuario = 'll15-0679'
Contraseña = 'Mavado18*051996'
y = 0



for i in range (0,3):



        nombre_usuario_puesto_por_usuario = input("Por favor escriba su nombre de usuario: ")
        Contraseña_Puesta_Por_Usuario = input("Por favor, escriba su contraseña: ")
        if nombre_usuario_puesto_por_usuario != nombre_usuario or Contraseña_Puesta_Por_Usuario != Contraseña:

            y = y + 1
        if y<3:
            print("El nombre de usuario u contraseña es incorrecto, por favor, intente de nuevo")
        elif y==3:
            print("Ya ha agotado los 3 intentos permitidos. Por favor, valide sus datos con la universidad")
            import sys
            sys.exit()

        elif nombre_usuario_puesto_por_usuario == nombre_usuario and Contraseña_Puesta_Por_Usuario == Contraseña:
        


            print("Nombre de usuario y contraseña correctos")
            print("¿Que desea Verificar?\n1.Materias\n2.Estudiantes\n3.Carreras\n4.Profesores")
            break
            opcion = int(input(""))
if opcion == 1:
                print("1. Registrar Materias")
                print("2. Consultar Materias")
                print("3. Listar Materias")
                print("4. Eliminar Materias")
                print("5. Actualizar Materias")
                segunda_opcion = int(input("Escriba el numero de la opcion que desea utilizar: \n"))
                if segunda_opcion == 1:
                    cantidad = int(input("Cuantas materias quisiera agregar"))
                    for i in range (0,cantidad):


                        id = int(input("¿Que ID desea asignarle a la materia que agregara?"))
                        materia = input("¿Cual es el nombre de la materia que desea agregar? \n")
                        primer_valor_materia = "INSERT INTO Materia (Id,nombre_Materia) values (%s, %s)"
                        values = (" "+ str(id)," " + materia)
                        mycursor.execute(primer_valor_materia, values)
                        mydb.commit()
                        print('La materia ha sido exitosamente agregada')
                        
                elif segunda_opcion == 2:

                    datos_filtrados = input('¿Que materia desea que se filtren los datos?\n')
                    mycursor.execute("SELECT * FROM Materia where nombre_Materia=''" ,datos_filtrados)              
                    resultado = mycursor.fetchall()
                    for x in resultado:
                        print(x)
                
                        

                elif segunda_opcion == 3:

                    mycursor.execute("SELECT * FROM Materia")
                    myresult = mycursor.fetchall()
                    for y in myresult:
                        print(y)
                elif segunda_opcion == 4:
                    fila_a_eliminar= input("¿Que fila desea eliminar?\n")
                    primera_sintaxis = ("delete from Materia where nombre_Materia= '%s'" % (fila_a_eliminar))
                    

                    mycursor.execute(primera_sintaxis )
                    mydb.commit()



                elif segunda_opcion == 5:

                    materia_reemplazada = input("¿Cual es el nombre de la materia que deseas reemplazar? \m ")
                    nuevo_nombre_materia = input("¿Cual es la nueva materia que desea agregar?")
                    sql = "UPDATE Materia SET nombre_Materia = ' ' " + nuevo_nombre_materia + "where nombre_Materia = ''" + materia_reemplazada
                    mycursor.execute(sql)
                    mydb.commit()


elif opcion == 2:
                print("1. Registrar Estudiantes")
                print("2. Consultar Estudiantes")
                print("3. Listar Estudiantes")
                print("4. Eliminar Estudiantes")
                print("5. Actualizar Estudiantes")
                tercera_opcion = int(input("Escriba el numero de la opcion que desea utilizar: \n"))
                if tercera_opcion == 1:
                    quantity = int(input("¿Cuantos Estudiantes quisiera agregar? "))
                    for x in range (0,quantity):
                    
                        Matricula = input("¿Cual es la matricula del estudiante que desea agregar? \n")
                        nombre_estudiante = input('¿Cual es el nombre del estudiante? \m ')
                        primer_valor = "INSERT INTO Estudiantes (Matricula, Nombre_Estudiante) values(%s,%s)"
                        segundo_valor = ("" + Matricula,"  " + nombre_estudiante)
                        mycursor.execute(primer_valor, segundo_valor)
                        mydb.commit()
                        print('El/La estudiante ha sido exitosamente agregado/da')

                elif tercera_opcion == 2:
                    datos_a_filtrar=input('Escriba por favor el nombre del estudiante que desea ver la informacion \n')
                    mycursor.execute("SELECT Matricula, Nombre_Estudiante FROM Estudiante where Nombre_Estudiante=''"+ datos_a_filtrar)
                    myresult = mycursor.fetchall()

                    for r in myresult:
                        print(r)

                elif tercera_opcion == 3:

                    mycursor.execute("SELECT * FROM Estudiantes")
                    my_result = mycursor.fetchall()
                    for e in myresult:
                        print(e)

                elif tercera_opcion == 4:
                    estudiante_a_eliminar= int(input("¿Cual es el nombre del o la estudiante que desea eliminar?\n"))
                    mycursor.execute("DELETE Nombre_Estudiante, Matricula WHERE Nombre_Estudiante = ''",estudiante_a_eliminar)
                    mydb.commit()

                elif tercera_opcion == 5:

                    estudiante_reemplazado = input("¿Cual es el nombre del o la estudiante que deseas reemplazar? \m ")
                    nuevo_nombre_estudiante = input("¿Cual es el nuevo estudiante que desea agregar?")
                    actualizacion_tabla_estudiantes = "UPDATE Materia SET Nombre_Estudiante = ' ' " + nuevo_nombre_estudiante + "where Nombre_Estudiante = ''" + estudiante_reemplazado
                    mycursor.execute(actualizacion_tabla_estudiantes)
                    mydb.commit()



elif opcion == 3:

                print('1. Registrar Carreras')
                print('2. Consultar Carreras')
                print('3. Listar Carreras')
                print('4. Eliminar Carreras')
                print('5. Actualizar Carreras')
                cuarta_opcion = int(input('¿Que opcion desea elegir?'))

                if cuarta_opcion == 1: 
                    cantidad_carreras = int(input("¿Cuantas Carreras quisiera agregar?"))
                    for c in range (0,cantidad_carreras-1):
                        Carrera = input("¿Cual es el nombre de la carrera que desea agregar? \n")
                        First_value = "INSERT INTO Carrera (Id, nombre_carrera) values (%s, %s)"
                        Second_value = ("1" , "  " + Carrera)
                        mycursor.execute(First_value, Second_value)
                        mydb.commit()
                        print('')
                    



                elif cuarta_opcion == 2:
                    datos_filtracion=input('Escriba por favor el nombre de la carrera que desea ver la informacion \n')
                    mycursor.execute("SELECT Id, nombre_carrera FROM Carrera where nombre_carrera=''"+ datos_filtracion)
                    mi_resultado = mycursor.fetchall()

                    for w in mi_resultado:
                        print(w)
                elif cuarta_opcion == 3:
    
                    mycursor.execute("SELECT * FROM Carrera")
                    my_Result = mycursor.fetchall()
                    for b in myresult:
                        print(b)
                elif cuarta_opcion == 4:
                    carrera_a_eliminar= input("¿Cual es el nombre de la carrera que desea eliminar?\n")
                    mycursor.execute("DELETE nombre_carrera WHERE nombre_carrera = ''"+ carrera_a_eliminar)
                    mydb.commit()


                elif cuarta_opcion == 5:
                    carrera_reemplazada = input("¿Cual es el nombre de la carrera que deseas reemplazar? \m ")
                    nueva_carrera = input("¿Cual es la nueva carrera que desea agregar?")
                    actualizacion_tabla_estudiantes = "UPDATE Carrera  SET nombre_carrera = ' ' " + nueva_carrera + "where nombre_carrera = ''" + carrera_reemplazada
                    mycursor.execute(actualizacion_tabla_estudiantes)
                    mydb.commit()


elif opcion == 4:

                print('1. Registrar Profesores')
                print('2. Consultar Profesores')
                print('3. Listar Profesores')
                print('4. Eliminar Profesores')
                print('5. Actualizar Profesores')
                quinta_opcion = int(input('¿Que opcion desea elegir?'))

                if quinta_opcion == 1:
                    cantidad_profesores = int(input("¿Cuantos profesores desea agregar? \n"))
                    for x in range (0,cantidad_profesores):
                        id_profesor = int(input("¿Cual es el id que desea asignarle al profesor? "))
                        nombre_profesor = input('¿Cual es el nombre del profesor?')
                        primer_valor_profesores = "Insert into Profesores (Id, Nombre_Profesor) values (%s, %s)"
                        strings = ("", + id_profesor + " " + nombre_profesor)
                        mycursor.execute(primer_valor_profesores, strings)
                        mydb.commit

                        print(mycursor.rowcount, "filas insertadas")
                

                elif quinta_opcion == 2:

                    informacion_a_filtrar=input('Escriba por favor el nombre del profesor que desea ver la informacion \n')
                    mycursor.execute("SELECT * FROM Profesores where Nombre_Profesor=''"+ informacion_a_filtrar)
                    final_resultado = mycursor.fetchall()

                    for v in mi_resultado:
                        print(v)

                elif quinta_opcion == 3:
                    mycursor.execute("SELECT * FROM Profesores")
                    theresult = mycursor.fetchall()
                    for u in myresult:
                        print(u)

               
                elif quinta_opcion == 4:
                    profesor_a_eliminar= input("¿Cual es el nombre del profesor o profesora que desea eliminar?\n")
                    mycursor.execute("DELETE Nombre_Profesor WHERE Nombre_Profesor = ''"+ profesor_a_eliminar)
                    mydb.commit()

                elif quinta_opcion == 5:
                    profesor_a_reemplazar = input("¿Cual es el nombre del profesor que deseas reemplazar? \m ")
                    nuevo_profesor = input("¿Cual es la nuevo profesor que desea agregar?")
                    actualizacion_tabla_profesores = "UPDATE Profesores SET Nombre_Profesor = ' ' " + nuevo_profesor + "where Nombre_Profesor = ''" + profesor_a_reemplazar
                    mycursor.execute(actualizacion_tabla_profesores)
                    mydb.commit()












                                                                                            

    




      






    
    
          
          
          
          
          
          

        
          
                                   

                   
