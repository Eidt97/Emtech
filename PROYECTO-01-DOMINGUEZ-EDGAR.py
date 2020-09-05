#Mandar a llamar las bd 
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

#Los usuarios y contraseñas que tendran acceso a la información
Usuarios_admin = [['Edgar','rojo'],['Fabricio','azul'],['Alma','verde']]

#Ingresar el usuario y contraseña en el login
User_entrada = input("Bienvenido a Lifestore Ingresa tu nombre de usuario: ")
Password_entrada = input("Ingresa tu contraseña: ")

contador_a = 0
total_a = []
#Para calcular la lista de mayor a menor en ventas
for producto_a in lifestore_products:
	for venta_a in lifestore_sales:
		if producto_a[0] == venta_a[1]:
			contador_a += 1

	formato_a = [producto_a[0],producto_a[1],contador_a]
	total_a.append(formato_a)
	contador_a = 0

grupos_ordenados_a = []

while total_a:
	minimo_a = total_a[0][2]
	lista_a = total_a[0]
	for grupo_a in total_a:
		if grupo_a[2] > minimo_a:
			minimo_a = grupo_a[2]
			lista_a = grupo_a
	grupos_ordenados_a.append(lista_a)
	total_a.remove(lista_a)

#Para calcular las lista de menor a mayor en ventas
contador_b = 0
total_b = []

for producto_b in lifestore_products:
	for venta_b in lifestore_sales:
		if producto_b[0] == venta_b[1]:
			contador_b += 1

	formato_b = [producto_b[0],producto_b[1],contador_b]
	total_b.append(formato_b)
	contador_b = 0

grupos_ordenados_b = []

while total_b:
	maximo_b = total_b[0][2]
	lista_b = total_b[0]
	for grupo_b in total_b:
		if grupo_b[2] < maximo_b:
			maximo_b = grupo_b[2]
			lista_b = grupo_b
	grupos_ordenados_b.append(lista_b)
	total_b.remove(lista_b)

#Los productos con menos busquedas
contador_c = 0
total_c = []

for producto_c in lifestore_products:
	for bus_c in lifestore_searches:
		if producto_c[0] == bus_c[1]:
			contador_c += 1

	formato_c = [producto_c[0],producto_c[1],contador_c]
	total_c.append(formato_c)
	contador_c = 0

grupos_ordenados_c = []

while total_c:
	minimo_c = total_c[0][2]
	lista_c = total_c[0]
	for grupo_c in total_c:
		if grupo_c[2] < minimo_c:
			minimo_c = grupo_c[2]
			lista_c = grupo_c
	grupos_ordenados_c.append(lista_c)
	total_c.remove(lista_c)

#Los productos con más busquedas
contador_d = 0
total_d = []

for producto_d in lifestore_products:
	for bus_d in lifestore_searches:
		if producto_d[0] == bus_d[1]:
			contador_d += 1

	formato_d = [producto_d[0],producto_d[1],contador_d]
	total_d.append(formato_d)
	contador_d = 0

grupos_ordenados_d = []

while total_d:
	maximo_d = total_d[0][2]
	lista_d = total_d[0]
	for grupo_d in total_d:
		if grupo_d[2] > maximo_d:
			maximo_d = grupo_d[2]
			lista_d = grupo_d
	grupos_ordenados_d.append(lista_d)
	total_d.remove(lista_d)


#Los productos con mejores reseñas
contador_e = 0
total_e = []

for producto_e in lifestore_products:
	for res_e in lifestore_sales:
		if producto_e[0] == res_e[1]:
			contador_e += res_e[2]

	formato_e = [producto_e[0],producto_e[1],contador_e]
	total_e.append(formato_e)
	contador_e = 0

grupos_ordenados_e = []

while total_e:
	minimo_e = total_e[0][2]
	lista_e = total_e[0]
	for grupo_e in total_e:
		if grupo_e[2] > minimo_e:
			minimo_e = grupo_e[2]
			lista_e = grupo_e
	grupos_ordenados_e.append(lista_e)
	total_e.remove(lista_e)

#Los productos con peores reseñas
contador_f = 0
total_f = []

for producto_f in lifestore_products:
	for res_f in lifestore_sales:
		if producto_f[0] == res_f[1]:
			contador_f += res_f[2]

	formato_f = [producto_f[0],producto_f[1],contador_f]
	total_f.append(formato_f)
	contador_f = 0

grupos_ordenados_f = []

while total_f:
	maximo_f = total_f[0][2]
	lista_f = total_f[0]
	for grupo_f in total_f:
		if grupo_f[2] < maximo_f:
			maximo_f = grupo_f[2]
			lista_f = grupo_f
	grupos_ordenados_f.append(lista_f)
	total_f.remove(lista_f)


contador_g = 0
total_g = []

for producto_g in lifestore_products:
	for venta_g in lifestore_sales:
		if producto_g[0] == venta_g[1]:
			contador_g += 1

	formato_g = [producto_g[0],producto_g[1],contador_g,contador_g*producto_g[2]]
	total_g.append(formato_g)
	contador_g = 0

grupos_ordenados_g = []

while total_g:
	minimo_g = total_g[0][2]
	lista_g = total_g[0]
	for grupo_g in total_g:
		if grupo_g[2] > minimo_g:
			minimo_g = grupo_g[2]
			lista_g = grupo_g
	grupos_ordenados_g.append(lista_g)
	total_g.remove(lista_g)


ventas_totales = []
contador_z = 0

for Ventas in grupos_ordenados_g:
	if Ventas[0] != 0:
		contador_z += Ventas[3]
formato_z = [contador_z]
ventas_totales.append(formato_z)
contador_z = 0





es_admin = 0
correcta = 0
correcta2 = 0



#Login que permite el acceso a la información y proporcion proyectos
while es_admin != 1:
  for usuario in Usuarios_admin:
    if usuario[0] == User_entrada and usuario[1] == Password_entrada:
      es_admin = 1
      print("Bienvenido,elige una opcion: \n 1. Opción a: (Mostrar los 50 productos más vendidos)  \n 2. Opción b: (Mostrar los 50 productos menos vendidos) \n 3. Opción c: (Mostrar los  productos menos buscados) \n 4. Opción d: (Mostrar los  productos más buscados) \n 5. Opción e: (Mostrar los 20 productos con mejores reseñas) \n 6. Opción f: (Mostrar los 20 productos con peores reseñas) \n 7. Opción g: (Mostrar los ingresos totales)")
      opcion = input("Ingresa una opcion: ")
      while correcta != 1:
        if opcion == "a":
          print("Los productos mas vendidos son: ")
          for May_a_Men in grupos_ordenados_a[0:51]:
          	print("El producto " + May_a_Men[1] + " se ha vendido " + str(May_a_Men[2]) + " veces")
          correcta = 1
          opcion2 = input("Deseas realizar otra consulta: ")
          if opcion2 == "si" or "Si":
          	print("Bienvenido,elige una opcion: \n 1. Opción a: (Mostrar los 50 productos más vendidos)  \n 2. Opción b: (Mostrar los 50 productos menos vendidos) \n 3. Opción c: (Mostrar los  productos menos buscados) \n 4. Opción d: (Mostrar los  productos más buscados) \n 5. Opción e: (Mostrar los 20 productos con mejores reseñas) \n 6. Opción f: (Mostrar los 20 productos con peores reseñas) \n 7. Opción g: (Mostrar los ingresos totales)")
          	opcion3 = input("Ingresa una opcion ")
          	while correcta2 != 1 :
          		if opcion3 == "a":
          			print("Los productos mas vendidos son")
          			for May_a_Men in grupos_ordenados_a[0:51]:
          				print("El producto " + May_a_Men[1] + " se ha vendido " + str(May_a_Men[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "b":
          			print("Los productos menos vendidos son")
          			for Men_a_May in grupos_ordenados_b[0:51]:
          				print("El producto " + Men_a_May[1] + " se ha vendido " + str(Men_a_May[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "c":
          			print("Los productos menos buscados son:")
          			for Men_a_May_bus in grupos_ordenados_c: 
          				print("El producto " + Men_a_May_bus[1] + " se ha buscado  " + str(Men_a_May_bus[2]) + " veces")          				
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "d":
          			print("Los productos más buscados son")
          			for May_a_Men_bus in grupos_ordenados_d:
          				print("El producto " + May_a_Men_bus[1] + " se ha buscado  " + str(May_a_Men_bus[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "e":
          			print("Los productos con mejores reseñas son:")
          			for May_Men_Res in grupos_ordenados_e[0:21]:
          				print("El producto " + May_Men_Res[1] + " tiene una suma de sus reseñas de   " + str(May_Men_Res[2]))	
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "f":
          			print("Los productos con peores reseñas son:")
          			for Men_May_Res in grupos_ordenados_f[0:21]:
          					print("El producto " + Men_May_Res[1] + " tiene una suma de sus reseñas de   " + str(Men_May_Res[2]))
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "g":
          			print("\nLas ventas totales del año son " + str(ventas_totales) +" pesos")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)          		
          		else:
          			print("opcion incorrecta")
          			opcion3 = input("Vuelve a intentarlo: ")
          else:
          	print("\nHasta luego buen dia " + User_entrada)
        elif opcion == "b":
          print("Los productos menos vendidos son")
          for Men_a_May in grupos_ordenados_b[0:51]:
          	print("El producto " + Men_a_May[1] + " se ha vendido " + str(Men_a_May[2]) + " veces")
          correcta = 1
          opcion2 = input("Deseas realizar otra consulta: ")
          if opcion2 == "si" or "Si":
          	print("Bienvenido,elige una opcion: \n 1. Opción a: (Mostrar los 50 productos más vendidos)  \n 2. Opción b: (Mostrar los 50 productos menos vendidos) \n 3. Opción c: (Mostrar los  productos menos buscados) \n 4. Opción d: (Mostrar los  productos más buscados) \n 5. Opción e: (Mostrar los 20 productos con mejores reseñas) \n 6. Opción f: (Mostrar los 20 productos con peores reseñas) \n 7. Opción g: (Mostrar los ingresos totales)")
          	opcion3 = input("Ingresa una opcion ")
          	while correcta2 != 1 :
          		if opcion3 == "a":
          			print("Los productos mas vendidos son")
          			for May_a_Men in grupos_ordenados_a[0:51]:
          				print("El producto " + May_a_Men[1] + " se ha vendido " + str(May_a_Men[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "b":
          			print("Los productos menos vendidos son")
          			for Men_a_May in grupos_ordenados_b[0:51]:
          				print("El producto " + Men_a_May[1] + " se ha vendido " + str(Men_a_May[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "c":
          			print("Los productos menos buscados son:")
          			for Men_a_May_bus in grupos_ordenados_c: 
          				print("El producto " + Men_a_May_bus[1] + " se ha buscado  " + str(Men_a_May_bus[2]) + " veces")          				
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "d":
          			print("Los productos más buscados son")
          			for May_a_Men_bus in grupos_ordenados_d:
          				print("El producto " + May_a_Men_bus[1] + " se ha buscado  " + str(May_a_Men_bus[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "e":
          			print("Los productos con mejores reseñas son:")
          			for May_Men_Res in grupos_ordenados_e[0:21]:
          				print("El producto " + May_Men_Res[1] + " tiene una suma de sus reseñas de   " + str(May_Men_Res[2]))	
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "f":
          			print("Los productos con peores reseñas son:")
          			for Men_May_Res in grupos_ordenados_f[0:21]:
          					print("El producto " + Men_May_Res[1] + " tiene una suma de sus reseñas de   " + str(Men_May_Res[2]))
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "g":
          			print("\nLas ventas totales del año son " + str(ventas_totales) +" pesos")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)          		
          		else:
          			print("opcion incorrecta")
          			opcion3 = input("Vuelve a intentarlo: ")
          else:
          	print("\nHasta luego buen dia " + User_entrada)
        elif opcion == "c":
          print("Los productos menos buscados son")
          for Men_a_May_bus in grupos_ordenados_c:
          	print("El producto " + Men_a_May_bus[1] + " se ha buscado  " + str(Men_a_May_bus[2]) + " veces")
          correcta = 1
          opcion2 = input("Deseas realizar otra consulta: ")
          if opcion2 == "si" or "Si":
          	print("Bienvenido,elige una opcion: \n 1. Opción a: (Mostrar los 50 productos más vendidos)  \n 2. Opción b: (Mostrar los 50 productos menos vendidos) \n 3. Opción c: (Mostrar los  productos menos buscados) \n 4. Opción d: (Mostrar los  productos más buscados) \n 5. Opción e: (Mostrar los 20 productos con mejores reseñas) \n 6. Opción f: (Mostrar los 20 productos con peores reseñas) \n 7. Opción g: (Mostrar los ingresos totales)")
          	opcion3 = input("Ingresa una opcion ")
          	while correcta2 != 1 :
          		if opcion3 == "a":
          			print("Los productos mas vendidos son")
          			for May_a_Men in grupos_ordenados_a[0:51]:
          				print("El producto " + May_a_Men[1] + " se ha vendido " + str(May_a_Men[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "b":
          			print("Los productos menos vendidos son")
          			for Men_a_May in grupos_ordenados_b[0:51]:
          				print("El producto " + Men_a_May[1] + " se ha vendido " + str(Men_a_May[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "c":
          			print("Los productos menos buscados son:")
          			for Men_a_May_bus in grupos_ordenados_c: 
          				print("El producto " + Men_a_May_bus[1] + " se ha buscado  " + str(Men_a_May_bus[2]) + " veces")          				
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "d":
          			print("Los productos más buscados son")
          			for May_a_Men_bus in grupos_ordenados_d:
          				print("El producto " + May_a_Men_bus[1] + " se ha buscado  " + str(May_a_Men_bus[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "e":
          			print("Los productos con mejores reseñas son:")
          			for May_Men_Res in grupos_ordenados_e[0:21]:
          				print("El producto " + May_Men_Res[1] + " tiene una suma de sus reseñas de   " + str(May_Men_Res[2]))	
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "f":
          			print("Los productos con peores reseñas son:")
          			for Men_May_Res in grupos_ordenados_f[0:21]:
          					print("El producto " + Men_May_Res[1] + " tiene una suma de sus reseñas de   " + str(Men_May_Res[2]))
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "g":
          			print("\nLas ventas totales del año son " + str(ventas_totales) +" pesos")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)          		
          		else:
          			print("opcion incorrecta")
          			opcion3 = input("Vuelve a intentarlo: ")
          else:
          	print("\nHasta luego buen dia " + User_entrada)
        elif opcion == "d":
          print("Los productos más buscados son")
          for May_a_Men_bus in grupos_ordenados_d:
          	print("El producto " + May_a_Men_bus[1] + " se ha buscado  " + str(May_a_Men_bus[2]) + " veces")
          correcta = 1 
          opcion2 = input("Deseas realizar otra consulta: ")
          if opcion2 == "si" or "Si":
          	print("Bienvenido,elige una opcion: \n 1. Opción a: (Mostrar los 50 productos más vendidos)  \n 2. Opción b: (Mostrar los 50 productos menos vendidos) \n 3. Opción c: (Mostrar los  productos menos buscados) \n 4. Opción d: (Mostrar los  productos más buscados) \n 5. Opción e: (Mostrar los 20 productos con mejores reseñas) \n 6. Opción f: (Mostrar los 20 productos con peores reseñas) \n 7. Opción g: (Mostrar los ingresos totales)")
          	opcion3 = input("Ingresa una opcion ")
          	while correcta2 != 1 :
          		if opcion3 == "a":
          			print("Los productos mas vendidos son")
          			for May_a_Men in grupos_ordenados_a[0:51]:
          				print("El producto " + May_a_Men[1] + " se ha vendido " + str(May_a_Men[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "b":
          			print("Los productos menos vendidos son")
          			for Men_a_May in grupos_ordenados_b[0:51]:
          				print("El producto " + Men_a_May[1] + " se ha vendido " + str(Men_a_May[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "c":
          			print("Los productos menos buscados son:")
          			for Men_a_May_bus in grupos_ordenados_c: 
          				print("El producto " + Men_a_May_bus[1] + " se ha buscado  " + str(Men_a_May_bus[2]) + " veces")          				
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "d":
          			print("Los productos más buscados son")
          			for May_a_Men_bus in grupos_ordenados_d:
          				print("El producto " + May_a_Men_bus[1] + " se ha buscado  " + str(May_a_Men_bus[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "e":
          			print("Los productos con mejores reseñas son:")
          			for May_Men_Res in grupos_ordenados_e[0:21]:
          				print("El producto " + May_Men_Res[1] + " tiene una suma de sus reseñas de   " + str(May_Men_Res[2]))	
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "f":
          			print("Los productos con peores reseñas son:")
          			for Men_May_Res in grupos_ordenados_f[0:21]:
          					print("El producto " + Men_May_Res[1] + " tiene una suma de sus reseñas de   " + str(Men_May_Res[2]))
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "g":
          			print("\nLas ventas totales del año son " + str(ventas_totales) +" pesos")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)          		
          		else:
          			print("opcion incorrecta")
          			opcion3 = input("Vuelve a intentarlo: ")
          else:
          	print("\nHasta luego buen dia " + User_entrada)
        elif opcion == "e":
          print("Los productos con mejores reseñas son:")
          for May_Men_Res in grupos_ordenados_e[0:21]:
          	print("El producto " + May_Men_Res[1] + " tiene una suma de sus reseñas de   " + str(May_Men_Res[2]))			
          correcta = 1 
          opcion2 = input("Deseas realizar otra consulta: ")
          if opcion2 == "si":
          	print("elige una opcion: \n 1. Opción a: (Mostrar los 50 productos más vendidos)  \n 2. Opción b: (Mostrar los 50 productos menos vendidos) \n 3. Opción c: (Mostrar los  productos menos buscados) \n 4. Opción d: (Mostrar los  productos más buscados) \n 5. Opción e: (Mostrar los 20 productos con mejores reseñas) \n 6. Opción f: (Mostrar los 20 productos con peores reseñas)")
          	opcion3 = input("Ingresa una opcion ")
          	while correcta2 != 1 :
          		if opcion3 == "a":
          			print("Los productos mas vendidos son")
          			for May_a_Men in grupos_ordenados_a[0:51]:
          				print("El producto " + May_a_Men[1] + " se ha vendido " + str(May_a_Men[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "b":
          			print("Los productos menos vendidos son")
          			for Men_a_May in grupos_ordenados_b[0:51]:
          				print("El producto " + Men_a_May[1] + " se ha vendido " + str(Men_a_May[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "c":
          			print("Los productos menos buscados son:")
          			for Men_a_May_bus in grupos_ordenados_c: 
          				print("El producto " + Men_a_May_bus[1] + " se ha buscado  " + str(Men_a_May_bus[2]) + " veces")          				
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "d":
          			print("Los productos más buscados son")
          			for May_a_Men_bus in grupos_ordenados_d:
          				print("El producto " + May_a_Men_bus[1] + " se ha buscado  " + str(May_a_Men_bus[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "e":
          			print("Los productos con mejores reseñas son:")
          			for May_Men_Res in grupos_ordenados_e[0:21]:
          				print("El producto " + May_Men_Res[1] + " tiene una suma de sus reseñas de   " + str(May_Men_Res[2]))	
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "f":
          			print("Los productos con peores reseñas son:")
          			for Men_May_Res in grupos_ordenados_f[0:21]:
          					print("El producto " + Men_May_Res[1] + " tiene una suma de sus reseñas de   " + str(Men_May_Res[2]))
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		else:
          			print("opcion incorrecta")
          			opcion3 = input("Vuelve a intentarlo: ")
          else:
          	print("\nHasta luego buen dia " + User_entrada)
        elif opcion == "f":
          print("Los productos con peores reseñas son:")
          for Men_May_Res in grupos_ordenados_f[0:21]:
          	print("El producto " + Men_May_Res[1] + " tiene una suma de sus reseñas de   " + str(Men_May_Res[2]))

          correcta = 1 
          opcion2 = input("Deseas realizar otra consulta: ")
          if opcion2 == "si" or "Si":
          	print("Bienvenido,elige una opcion: \n 1. Opción a: (Mostrar los 50 productos más vendidos)  \n 2. Opción b: (Mostrar los 50 productos menos vendidos) \n 3. Opción c: (Mostrar los  productos menos buscados) \n 4. Opción d: (Mostrar los  productos más buscados) \n 5. Opción e: (Mostrar los 20 productos con mejores reseñas) \n 6. Opción f: (Mostrar los 20 productos con peores reseñas) \n 7. Opción g: (Mostrar los ingresos totales)")
          	opcion3 = input("Ingresa una opcion ")
          	while correcta2 != 1 :
          		if opcion3 == "a":
          			print("Los productos mas vendidos son")
          			for May_a_Men in grupos_ordenados_a[0:51]:
          				print("El producto " + May_a_Men[1] + " se ha vendido " + str(May_a_Men[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "b":
          			print("Los productos menos vendidos son")
          			for Men_a_May in grupos_ordenados_b[0:51]:
          				print("El producto " + Men_a_May[1] + " se ha vendido " + str(Men_a_May[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "c":
          			print("Los productos menos buscados son:")
          			for Men_a_May_bus in grupos_ordenados_c: 
          				print("El producto " + Men_a_May_bus[1] + " se ha buscado  " + str(Men_a_May_bus[2]) + " veces")          				
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "d":
          			print("Los productos más buscados son")
          			for May_a_Men_bus in grupos_ordenados_d:
          				print("El producto " + May_a_Men_bus[1] + " se ha buscado  " + str(May_a_Men_bus[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "e":
          			print("Los productos con mejores reseñas son:")
          			for May_Men_Res in grupos_ordenados_e[0:21]:
          				print("El producto " + May_Men_Res[1] + " tiene una suma de sus reseñas de   " + str(May_Men_Res[2]))	
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "f":
          			print("Los productos con peores reseñas son:")
          			for Men_May_Res in grupos_ordenados_f[0:21]:
          					print("El producto " + Men_May_Res[1] + " tiene una suma de sus reseñas de   " + str(Men_May_Res[2]))
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "g":
          			print("\nLas ventas totales del año son " + str(ventas_totales) +" pesos")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)          		
          		else:
          			print("opcion incorrecta")
          			opcion3 = input("Vuelve a intentarlo: ")
          else:
          	print("\nHasta luego buen dia " + User_entrada)
        elif opcion == "g":
          print("\nLas ventas totales del año son " + str(ventas_totales) +" pesos")
          correcta = 1 
          opcion2 = input("Deseas realizar otra consulta: ")
          if opcion2 == "si" or "Si":
          	print("Bienvenido,elige una opcion: \n 1. Opción a: (Mostrar los 50 productos más vendidos)  \n 2. Opción b: (Mostrar los 50 productos menos vendidos) \n 3. Opción c: (Mostrar los  productos menos buscados) \n 4. Opción d: (Mostrar los  productos más buscados) \n 5. Opción e: (Mostrar los 20 productos con mejores reseñas) \n 6. Opción f: (Mostrar los 20 productos con peores reseñas) \n 7. Opción g: (Mostrar los ingresos totales)")
          	opcion3 = input("Ingresa una opcion ")
          	while correcta2 != 1 :
          		if opcion3 == "a":
          			print("Los productos mas vendidos son")
          			for May_a_Men in grupos_ordenados_a[0:51]:
          				print("El producto " + May_a_Men[1] + " se ha vendido " + str(May_a_Men[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "b":
          			print("Los productos menos vendidos son")
          			for Men_a_May in grupos_ordenados_b[0:51]:
          				print("El producto " + Men_a_May[1] + " se ha vendido " + str(Men_a_May[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "c":
          			print("Los productos menos buscados son:")
          			for Men_a_May_bus in grupos_ordenados_c: 
          				print("El producto " + Men_a_May_bus[1] + " se ha buscado  " + str(Men_a_May_bus[2]) + " veces")          				
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "d":
          			print("Los productos más buscados son")
          			for May_a_Men_bus in grupos_ordenados_d:
          				print("El producto " + May_a_Men_bus[1] + " se ha buscado  " + str(May_a_Men_bus[2]) + " veces")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "e":
          			print("Los productos con mejores reseñas son:")
          			for May_Men_Res in grupos_ordenados_e[0:21]:
          				print("El producto " + May_Men_Res[1] + " tiene una suma de sus reseñas de   " + str(May_Men_Res[2]))	
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "f":
          			print("Los productos con peores reseñas son:")
          			for Men_May_Res in grupos_ordenados_f[0:21]:
          					print("El producto " + Men_May_Res[1] + " tiene una suma de sus reseñas de   " + str(Men_May_Res[2]))
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)
          		elif opcion3 == "g":
          			print("\nLas ventas totales del año son " + str(ventas_totales) +" pesos")
          			correcta2 = 1
          			print("\nHasta luego buen dia " + User_entrada)          		
          		else:
          			print("opcion incorrecta")
          			opcion3 = input("Vuelve a intentarlo: ")
          else:
          	print("\nHasta luego buen dia " + User_entrada)
 
        else:
          print("Opcion incorrecta")
          opcion = input("Vuelve a intentarlo: ")
      
  if es_admin==0:
    print("Usuario o contraseña incorrecta")
    User_entrada = input("Vuelve a ingresar tu usuario : ")
    Password_entrada = input("Vuelve a ingresar tu contraseña: ")