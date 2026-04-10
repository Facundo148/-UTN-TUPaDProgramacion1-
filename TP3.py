#Ejercicio 1— “Caja del Kiosco”
print("#Ejercicio 1")

while True:
    name_client=input("Ingresar el nombre del cliente: ")
    solo_letra=name_client.isalpha()
    if solo_letra==True:
        break
    else:
        print("Por favor no incluya numeros...")

while True:
    productos=(input("Ingresar la cantidad de productos a comprar: "))
    solo_numero=productos.isdigit() 
    if solo_numero:
        productos=int(productos)
        if productos>0:
            break
        else:
            print("La cantidad debe ser mayor a 0")
    else:
        print("Por favor no incluya letras...")

total=0
total_1=0
total_2=0

lista_1=[]

for i in range(productos):
    while True:  
        precio=(input(f"Ingresar precio del producto N°{i+1}: ")) 
        solo_numero_1=precio.isdigit()
        if solo_numero_1:
            precio=int(precio)
            nproducto=i+1
            total+=precio
            break
        else:
            print("Error. Solo escribir números")
    while True:
        print("¿El producto tiene descuento?")
        descuento=input("Indicar con S/N: ").upper()
        if descuento in ("S", "N"):
            break
        else:
            print("Error. Intento otra vez")
    if descuento=="S": 
        precio_1=0.90*precio
        total_1+=precio_1
    else:
        total_2+=precio
    lista_1.append([nproducto,precio,descuento])

total_3=total_2+total_1
promedio = total_3 / productos
ahorro=total-total_3
print()
print(f"Cliente: {name_client}")
for i in range(productos):
    print(f"Producto N°: {lista_1[i][0]} -- Precio del producto: {lista_1[i][1]} -- Descuento: '{lista_1[i][2]}'")

print(f"Total sin descuento: {total}\n"
      f"Total con descuento: {total_3:.2f}\n"
      f"Ahorro: {ahorro:.2f}\n"
      f"Promedio por producto: {promedio:.2f}")   
 

#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
print("#Ejercicio 2")

usuario_correcto="alumno"
clave_correcta="python123"
intentos=0
sesion=0

while intentos<3:
    usuario=input("Ingresar usuario: ")
    clave=input("Ingresar clave: ")
    print()
    if usuario==usuario_correcto and clave==clave_correcta:
        sesion=1
        print("Sesión iniciada con éxito!") 
        break
    else:
        intentos+=1
        if intentos==3:
            print("Cuenta bloqueada...")
        else:
            print(f"Numero de intentos: {intentos}/3")
            print("Contraseña o clave incorrectos.\n"
            f"intentar otra vez...\n")
print()
while sesion==1:
    print("1)Ver estado de inscripción   2)Cambiar clave   3)Mostrar mensaje motivacional   4)Salir")
    opcion=input("Selecionar una opción: ")
    print()
    if opcion in ("1", "2", "3", "4"):
        if opcion=="1":
            print("Estado: Usted esta inscripto!\n")
        elif opcion=="2":
            while True:
                print("2. Cambiar clave.")
                print("La nueva clave debe tener minimo 6 caracteres.")
                clave_nueva=input("Ingresar una nueva clave: ")
                if len(clave_nueva)>=6:
                    clave_confirmar=input("Confirmar nueva clave: ")
                    while clave_confirmar!=clave_nueva:
                        print("La contraseña no coincide.")
                        clave_confirmar=input("confirmar nueva clave: ")                       
                    clave_correcta=clave_nueva
                    print("Se cambió la contraseña!\n")
                    break
                else:
                    print("Error. Tienen que ser minimo 6 caracteres\n")
                    continue    
                    
        elif opcion=="3":
            print("Cada fracaso te acerca más al éxito\n")
        elif opcion=="4":
            print("Saliendo del menu principal...")
            break
    else:
        print("Opción incorrecta. Ingresar una de las 4 opciones.\n")
        

#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
lunes1 = lunes2 = lunes3 = lunes4 = "" 
martes1=martes2=martes3=""

nombre_operador=input("Ingresar nombre del operador: ")
verificar_nombre=nombre_operador.isalpha()
while verificar_nombre==False:
    print("Solo ingresar letras por favor, sin espacios")
    nombre_operador=input("Ingresar nuevamente un nombre: ")    
    verificar_nombre=nombre_operador.isalpha()
while True:
    print("Seleccionar una opción del menú:\n1)Reservar turno  2)Cancelar turno  3)Ver agenda del día  4)Ver resumen general  5)Cerrar sistema")
    opcion=(input("---> "))
    verificar_opcion=opcion.isdigit()
    while verificar_opcion==False or not(opcion in ("1","2","3","4","5")):
        print("Opción inválida. Por favor solo ingresar el numero de las opciónes")
        opcion=input("---> ")
        verificar_opcion=opcion.isdigit() 
    if opcion=="1":
        print()
        print("Reservar turno")
        nombre_paciente=input("Ingresar nombre del paciente: ")
        while not nombre_paciente.isalpha():
            print("Solo ingresar letras...")
            nombre_paciente = input("Ingresar nombre del paciente: ")
        print("Elegir día: 1=Lunes  2=Martes")
        dia_turno=input("---> ")
        while not(dia_turno.isdigit() and dia_turno in ("1","2")):
            print("Día invalido. Por favor ingresar una de las dos opciones: 1=Lunes  2=Martes")
            dia_turno=input("---> ")
        if dia_turno=="1":
            if nombre_paciente in (lunes1, lunes2, lunes3, lunes4):
                print("Este paciente ya tiene turno el lunes...\n")
            elif lunes1=="":
                print(f"Turno guardado para {nombre_paciente}!\n")
                lunes1=nombre_paciente
            elif lunes2=="":
                print(f"Turno guardado para {nombre_paciente}!\n")
                lunes2=nombre_paciente
            elif lunes3=="":
                print(f"Turno guardado para {nombre_paciente}!\n")
                lunes3=nombre_paciente
            elif lunes4=="":
                print(f"Turno guardado para {nombre_paciente}!\n")
                lunes4=nombre_paciente
            else:
                print("No queda ningun turno para el dia lunes...\n")
        elif dia_turno=="2":
            if nombre_paciente in (martes1, martes2, martes3):
                print("Este paciente ya tiene turno el martes...\n")
            elif martes1=="":
                print(f"Turno guardado para {nombre_paciente}!\n")
                martes1=nombre_paciente
            elif martes2=="":
                print(f"Turno guardado para {nombre_paciente}!\n")
                martes2=nombre_paciente
            elif martes3=="":
                print(f"Turno guardado para {nombre_paciente}!\n")
                martes3=nombre_paciente
            else:
                print("No queda ningun turno para el dia martes...\n")
    elif opcion=="2":
        print()
        print("Cancelación de turnos:  ")
        print("Elegir el día del turno: 1=Lunes  2=Martes")
        dia_turno=input("---> ")
        while not(dia_turno.isdigit() and dia_turno in ("1","2")):
            print("Día invalido. Por favor ingresar una de las dos opciones: 1=Lunes  2=Martes")
            dia_turno=input("---> ")
        nombre_paciente=input("Ingresar nombre del paciente: ")
        while not nombre_paciente.isalpha():
            print("Solo ingresar letras...\n")
            nombre_paciente = input("Ingresar nombre del paciente: ")
        if dia_turno=="1":   
            if lunes1==nombre_paciente:
                print(f"Turno cancelado para {nombre_paciente}!\n")
                lunes1=""
            elif lunes2==nombre_paciente:
                print(f"Turno cancelado para {nombre_paciente}!\n")
                lunes2=""
            elif lunes3==nombre_paciente:
                print(f"Turno cancelado para {nombre_paciente}!\n")
                lunes3=""
            elif lunes4==nombre_paciente:
                print(f"Turno cancelado para {nombre_paciente}!\n")
                lunes4=""
            else:
                print("No existe ningun turno el lunes para este paciente...\n")
        elif dia_turno=="2":   
            if martes1==nombre_paciente:
                print(f"Turno cancelado para {nombre_paciente}!\n")
                martes1=""
            elif martes2==nombre_paciente:
                print(f"Turno cancelado para {nombre_paciente}!\n")
                martes2=""
            elif martes3==nombre_paciente:
                print(f"Turno cancelado para {nombre_paciente}!\n")
                martes3=""
            else:
                print("No existe ningun turno el martes para este paciente...\n")
    elif opcion=="3":
        print()
        print("Agenda del dia")
        print("Indicar el dia de la agenda: 1=Lunes  2=Martes")       
        dia_turno=input("---> ")
        while not(dia_turno.isdigit() and dia_turno in ("1","2")):
            print("Día invalido. Por favor ingresar una de las dos opciones: 1=Lunes  2=Martes")
            dia_turno=input("---> ")
        if dia_turno=="1":
            print("Turno 1", f"ocupado por {lunes1}" if lunes1 != "" else "libre")
            print("Turno 2", f"ocupado por {lunes2}" if lunes2 != "" else "libre")
            print("Turno 3", f"ocupado por {lunes3}" if lunes3 != "" else "libre")
            print("Turno 4", f"ocupado por {lunes4}" if lunes4 != "" else "libre")
        elif dia_turno=="2":
            print("Turno 1", f"ocupado por {martes1}" if martes1!="" else "libre")
            print("Turno 2", f"ocupado por {martes2}" if martes2!="" else "libre")
            print("Turno 3", f"ocupado por {martes3}" if martes3!="" else "libre")
    elif opcion=="4":
        ocupados_lunes=0
        ocupados_martes=0
        libres_lunes=0
        libres_martes=0
        if lunes1 != "":
            ocupados_lunes += 1
        else:
            libres_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        else:
            libres_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        else:
            libres_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1
        else:
            libres_lunes += 1
        if martes1 != "":
            ocupados_martes += 1
        else:
            libres_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        else:
            libres_martes += 1
        if martes3 != "":
            ocupados_martes += 1
        else:
            libres_martes += 1
        print("Resumen general")
        print("Agenda del Lunes:")
        print(f"Turnos ocupados: {ocupados_lunes}")
        print(f"Turnos libres: {libres_lunes}\n")
        print("Agenda del Martes:")
        print(f"Turnos ocupados: {ocupados_martes}")
        print(f"Turnos libres: {libres_martes}\n")
    elif opcion=="5":
        print("Cerrando el sistema...")
        break


#Ejercicio 4 — “Escape Room: La Bóveda”
racha=0
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
print("“Escape Room: La Bóveda”\n"
"Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.\n"
"Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.\n")
agente=input("Ingresar nombre del agente: ")
print(f"Bienvenido {agente}!")
while True:
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}\n")
    print("1)Forzar cerradura  2)Hackear panel  3)Descansar")
    menu=input("Elegir una de las opciones: ")
    while not(menu.isdigit()) or menu not in ("1","2","3"):
        print("Opción invalida. Solo ingresar una de las 3 opciones")
        menu=input("Elegir una de las opciones: ")
    if menu=="1":
        energia-=20
        tiempo-=2
        racha+=1
        print("Forzar cerradura (costo: -20 energía, -2 tiempo)")
        if racha>=3:
            alarma=True
            print("Cerradura trabada! La alarma se activo!")
        else:
            forzar=input("Ingrear un numero de 1 al 3: ")
            while not(forzar.isdigit()) or forzar not in ("1","2","3"):
                print("Opción invalida. Solo ingresar un numero del 1 al 3...")
                forzar=input("Ingresar un numero de 1 al 3: ")                
            if forzar=="3":
                alarma=True
                print("Se activo la alarma!")
            elif forzar in ("1","2"):
                cerraduras_abiertas+=1
                print("Abriste una cerradura!")      
    elif menu=="2":
        racha=0
        energia-=10
        tiempo-=3
        print("Hackear panel (costo: -10 energía, -3 tiempo)")
        for i in range(4):
            codigo_parcial+="a"
            print("Hackeando...")
        if len(codigo_parcial)>=8:
            print("Hackeo completado.\nAbriste una cerradura!")
            codigo_parcial=""
            cerraduras_abiertas+=1
        else:
            print("Progreso acumulado... ")
    elif menu=="3":
        racha=0
        if alarma==False:
            energia+=15
            print("Descansar (costo: +15 energía)")
        elif alarma==True:
            energia+=5
            print("Descansar (Costo: +5 energia)")
        if energia>=100:
                energia=100
                print("Tienes el maximo de energía!")
    if cerraduras_abiertas==3:
        print(f"Felicidades {agente}! Abriste las 3 cerraduras y ganaste el juego!")
        break
    if alarma==True and tiempo<=3:
        print("Bloqueo por alarma. Pierdes...")
        break    
    if energia <= 0 or tiempo <= 0:
        print("Perdiste")
        break
    

#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
vida_gladiador=100
vida_enemigo=100
pociones_vida=3
daño_base=15
daño_base_enemigo=12# <--- Lo dejo aca pero no fue neceseria esta variable para el codigo del juego
turno_gladiador=True
gladiador=input("Ingresar tu nombre de gladiador: ")
while gladiador.isalpha()==False:
    print("Solo ingresar letras...")
    gladiador=input("Ingresar tu nombre de gladiador: ")
while True:
    print("---------------------")
    print(f"Tu vida: {vida_gladiador} Tus pociones: {pociones_vida} / Vida del enemigo: {vida_enemigo}")
    print("Elije una acción: 1)Ataque pesado  2)Rafaga veloz  3)Curar")
    accion=input("---> ")
    while accion not in ("1","2","3"):
        print("Error. Ingresar solo uno de los numeros de las opciones...")
        accion=(input("---> "))
    if accion=="1":
        if vida_enemigo<20:
            golpe_critico=int(daño_base*1.5)
            vida_enemigo-=golpe_critico
            print(f"Atacaste al enemigo por {golpe_critico} puntos de daño critico!")
        else: 
            vida_enemigo-=daño_base
            print(f"Atacaste al enemigo por {daño_base} puntos de daño!")
    elif accion=="2":
        for i in range(3):
            print("golpe conectado por 5 puntos de daño!")
        vida_enemigo-=15
        print(f"Atacaste al enemigo por un total de 15 puntos de daño!")
    elif accion=="3":
        if pociones_vida>0:
            if vida_gladiador==100:
                print("Ya tienes la vida al maximo")
            else:
                vida_gladiador+=30
                pociones_vida-=1
                if vida_gladiador>=100:
                    print("Tu vida subió al maximo!")
                    vida_gladiador=100
        else:
            print("No te quedan más pociones...")
    if vida_enemigo<=0:
        print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
        break
    print(f"El enemigo te ataco por 12 puntos de daño!")
    vida_gladiador-=12
    if vida_gladiador<=0:
        print("DERROTA...")
        break
