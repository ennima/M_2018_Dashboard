# import pandas as pd
import os
import pathlib
from datetime import datetime
import math

import time
from time import time as time_i

cwd = os.getcwd()
print(cwd)



#### Funciones
 ## Funciones generales creadas a partir de éste problema
def proceso_fragmentado(tarea_ejecutar,parametros,total,steps):
	
	regreso_global = []

	case_type_string = type("hola")
	case_type_tuple = type(("hola","que tal"))
	case_type_list = type(["hola","que tal"])

	this_type = ""
	# print("LEN PARAM: ",len(parametros))
	# print("Type Param:",type(parametros))

	if(case_type_tuple == type(parametros)):
		# print("---  Es una tupla papa")
		this_type = "tuple"
	elif(case_type_string == type(parametros)):
		# print("--- String")
		this_type = "str"

	# total = 101
	# steps = 2

	step_size = math.floor(total / steps)

	print("## Header ################## "+"steps:",steps,"step_size:",step_size,"total:",total)

	first_step = True
	ini = 0
	out = 0
	out_last = 0

	for i in range(0,steps):
		if(first_step):
			print("First Step")
			ini = 0
			out = ini + step_size
			print("	"+str(ini)+","+str(out))
			#made action
			if(this_type == "str"):
				if(parametros == "in_out"):
					tarea_ejecutar(ini,out)
				else:
					tarea_ejecutar(*parametros)
			elif(this_type == "tuple"):
				# print("OKI")
				# print(parametros[0])
				# print(parametros[1])
				if(parametros[0] == "in_out"):
					if(type(parametros[1]) == case_type_tuple):
						parametrosN = parametros[1] + (str(ini),str(out))
						# print(parametrosN)

						resultado = tarea_ejecutar(*parametrosN)
						if(case_type_list == type(resultado)):
							print("---------- regreso_global ----------------")
							# print(regreso_global)
							regreso_global += resultado
					elif(type(parametros[1]) == case_type_string):
						print("## WARNING! ## Pendiente de resolver: Case String")

			# out_last = out
			first_step = False
		elif((i+1) == steps):
			print("last step")
			ini = out + 1
			out = total
			print("	"+str(ini)+","+str(out))
			#made action
			if(this_type == "str"):
				if(parametros == "in_out"):
					tarea_ejecutar(ini,out)
				else:
					tarea_ejecutar(*parametros)
			elif(this_type == "tuple"):
				# print("OKI")
				# print(parametros[0])
				# print(parametros[1])
				if(parametros[0] == "in_out"):
					if(type(parametros[1]) == case_type_tuple):
						parametrosN = parametros[1] + (str(ini),str(out))
						# print(parametrosN)

						resultado = tarea_ejecutar(*parametrosN)
						if(case_type_list == type(resultado)):
							# print("---------- regreso_global ----------------")
							# print(regreso_global)
							regreso_global += resultado
					elif(type(parametros[1]) == case_type_string):
						print("## WARNING! ## Pendiente de resolver: Case String")
			
		else:
			# print("Step Intermedio")
			ini = out + 1
			out = ini + step_size
			# print("	"+str(ini)+","+str(out))
			#made action
			if(this_type == "str"):
				if(parametros == "in_out"):
					tarea_ejecutar(ini,out)
				else:
					tarea_ejecutar(*parametros)
			elif(this_type == "tuple"):
				# print("OKI")
				# print(parametros[0])
				# print(parametros[1])
				if(parametros[0] == "in_out"):
					if(type(parametros[1]) == case_type_tuple):
						parametrosN = parametros[1] + (str(ini),str(out))
						# print(parametrosN)

						resultado = tarea_ejecutar(*parametrosN)
						if(case_type_list == type(resultado)):
							# print("---------- regreso_global ----------------")
							# print(regreso_global)
							regreso_global += resultado
					elif(type(parametros[1]) == case_type_string):
						print("## WARNING! ## Pendiente de resolver: Case String")


	return regreso_global



def abre_reporte(path):
	with open(path,"r") as f:
		current_report = f.readlines()
	return current_report

def validar_desbordamiento(i,lista):
	if(i >= len(lista)):		
		i = len(lista) - 1
	return i

def get_lista_reportes(path_mm,type):
	#Existen dos types "in" y "out"
	score_files = []
	for item in pathlib.Path(path_mm).iterdir():
		# print(item)
		if item.is_file():
			# print(type(get_date_from_stratus_summary(item)))
			if type in str(item):
				# print(item)
				score_files.append(str(item))
	return score_files

def get_date_from_stratus_summary(filename):
	print(filename)
	d=str(filename).split("_")[3].replace(".csv","")
	print(d)
	date = datetime.strptime(d, '%d%m%Y')
	print(date)

	return date

def find_item(item,array):
	result = True
	res = [each for each in array if each==item]
	# print(res)
	if(len(res)==0):
		result = False
	return result

def get_size_bytes(item):
	item_split = item.split(",")
	return int(item_split[2])

#pinta una lista con número de linea como editor de código
def print_list(lista):
	line_counter = 0
	for item in lista:
		line_counter+=1
		print(str(line_counter)+" "+item)

def get_clean_list(current_report,line_breaker_conditio,stream_limit):
	discard_list = []
	clean_list_1 = []
	clean_list = []
	# stream_limit = 2800
	fisrt_pass = False
	pass_counter = 0


	for breaker in line_breaker_conditio:
		pass_counter += 1
		# print("\n\n\n------############### Begin Pass",breaker,"- pass:",pass_counter)
		if(fisrt_pass == False):
			# First pass toma una muestra de los datos y genera una primer lista limpia
			# descarta el primer breaker
			for i in range(0,stream_limit):
				# print(str(i)+"  "+current_report[i])
				i = validar_desbordamiento(i,current_report)
				item = current_report[i]
				breaker = line_breaker_conditio[0]
				if(breaker in item):
					# print("---Descartar")
					pass
				else:
					if(find_item(item,clean_list) == False):
						if(find_item(item,discard_list)==False):
							# print("AGREGA: ",item)
							clean_list.append(item)
					else:
						# print("NO AGREGA: ", item)
						discard_list.append(item)
			fisrt_pass = True
			clean_list_1 = clean_list
			clean_list = []
		else:
			# print("next pass")
			
			for item in clean_list_1:
				# breaker = line_breaker_conditio[1]
				if(breaker in item):
					# print("---Descartar")
					pass
				else:
					if(find_item(item,clean_list) == False):
						if(find_item(item,discard_list)==False):
							# print("AGREGA: ",item)
							clean_list.append(item)
					else:
						# print("NO AGREGA: ", item)
						discard_list.append(item)

			clean_list_1 = clean_list
			clean_list = []

			


		# print("\n------############### END Pass",breaker,"- pass:",pass_counter,"\n\n\n")
	return clean_list_1

def get_clean_list_large(current_report,line_breaker_conditio,stream_limit_inf,stream_limit_sup):
	# print("## Ejecutando ##",)
	discard_list = []
	clean_list_1 = []
	clean_list = []
	# stream_limit = 2800
	fisrt_pass = False
	pass_counter = 0


	for breaker in line_breaker_conditio:
		pass_counter += 1
		# print("\n\n\n------############### Begin Pass",breaker,"- pass:",pass_counter)
		if(fisrt_pass == False):
			# First pass toma una muestra de los datos y genera una primer lista limpia
			# descarta el primer breaker
			for i in range(int(stream_limit_inf),int(stream_limit_sup)):						
				i = validar_desbordamiento(i,current_report)
				item = current_report[i]
				breaker = line_breaker_conditio[0]
				if(breaker in item):
					# print("---Descartar")
					pass
				else:
					if(find_item(item,clean_list) == False):
						if(find_item(item,discard_list)==False):
							# print("AGREGA: ",item)
							clean_list.append(item)
					else:
						# print("NO AGREGA: ", item)
						discard_list.append(item)
			fisrt_pass = True
			clean_list_1 = clean_list
			clean_list = []
		else:
			# print("next pass")
			
			for item in clean_list_1:
				# breaker = line_breaker_conditio[1]
				if(breaker in item):
					# print("---Descartar")
					pass
				else:
					if(find_item(item,clean_list) == False):
						if(find_item(item,discard_list)==False):
							# print("AGREGA: ",item)
							clean_list.append(item)
					else:
						# print("NO AGREGA: ", item)
						discard_list.append(item)

			clean_list_1 = clean_list
			clean_list = []

			


		# print("\n------############### END Pass",breaker,"- pass:",pass_counter,"\n\n\n")
	return clean_list_1

def suma_sizes_clean_list(lista_limpia,path_to_inspect):
	##   path_to_inspect es la carpeta sobre la que se quiere actuar
	tiempo_inicial1 = time_i()
	line_counter = 0
	sumatoria = 0
	for item in lista_limpia:
		line_counter+=1
		# print(str(line_counter)+"  "+item)

		###### Extraer el peso ########
		
		if(item == lista_limpia[0]):
			# print("cabezal")
			pass
		elif(path_to_inspect in item):
			# print("SUMAR")
			size = get_size_bytes(item)
			sumatoria+=size		
		else:
			# print("---ITEM---",item)
			path_to_inspect_size = get_size_bytes(item)
	print("###############  TIEMPOS SUMATORIA   ######################")
	display_times_end(tiempo_inicial1)
	return sumatoria


def display_times_end(tiempo_inicial):
	tiempo_final = time_i()
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	print("Tardó: " , tiempo_ejecucion,"s")
	m, s = divmod(tiempo_ejecucion, 60)
	h, m = divmod(m, 60)
	restore_time = "%02d:%02d:%02d" % (h, m, s)
	print ("Tardó:",restore_time)
#### Fin de Funciones



tiempo_inicial = time_i() 



### Get lista de reportes ###
path_mm = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\M_2018_Dash_data_vxv\\"
score_files = get_lista_reportes(path_mm,"in")



## Simplificar los reportes
print("\n\n################# SCORES: ###########################")
print(score_files)
print("\n\n\n\n\n")
## Select Scores
score_curr = len(score_files) -1
current_report = abre_reporte(score_files[score_curr])
print("Total of lines: ",len(current_report))

# ### Fin Get lista de reportes ###



### Generar la lista limpia de dirs ###
line_breaker_conditio = [".cmf\\","Edius Projects\\",".db\\",".mp4\\",".txt\\",".jpg\\",".bmp\\",".mpeg\\",".eap\\",".ewc2\\"]
path_to_inspect="V:\\media\\VOTOXVOTO 2018 LIVEU\\"
path_to_inspect_size = 0

## LArge step ok = 968
steps = 48 

###  Seleccionar el mejor número de Steps de acuerdo al reporte 
total_lines = len(current_report)

############   ### Velocidades de ejecución
long_speed = [12,24,48,96,192,384]
just_speed = [24,48,96,192,384,768]
fast_speed = [48,96,192,384,768,968]
ultra_fast_speed = [96,192,384,768,968,1968]
just_entrepeneur_fast_speed = [196,768,1768,2768,4968,9968]

speed_matrix = just_entrepeneur_fast_speed

if(total_lines < 400000):
	steps = speed_matrix[0]
elif(total_lines < 600000):
	steps = speed_matrix[1]
elif(total_lines < 800000):
	steps = speed_matrix[2]
elif(total_lines < 900000):
	steps = speed_matrix[3]
elif(total_lines < 1000000):
	steps = speed_matrix[4]
elif(total_lines > 1009717):
	steps = speed_matrix[5]
############   ### END Velocidades de ejecución



step_size = math.floor(total_lines / steps)
print("total_lines:",total_lines,"step_size:",step_size," Steps:",steps)
lista_limpia = proceso_fragmentado(get_clean_list_large,("in_out",(current_report,line_breaker_conditio)),len(current_report),steps)

# lista_limpia = get_clean_list_large(current_report,line_breaker_conditio,stream_limit_1+1,len(current_report))

# print_list(lista_limpia)




############### Sumatoria de los elementos de la lista limpia 
print("\n\n \n\n \n\n########## Clean List ###########")


###  Sumar varios directorios o paths
path_root = "V:\\media\\"
path_to_inspect_list=["VOTOXVOTO 2018 LIVEU","VOTOXVOTO 2018 CAMARAS","Especiales Noticias","Estudio","LiveU"]

sumatoria_lista = []


for directorio in path_to_inspect_list:
	path_to_find = path_root + directorio + "\\"
	sumatoria = suma_sizes_clean_list(lista_limpia,path_to_find)
	print("path_to_inspect = ",path_to_find)
	print("sumatoria = ",sumatoria)
	item_suma = {"size":sumatoria,"path":directorio}
	sumatoria_lista.append(item_suma)



for item in sumatoria_lista:
	print("->",item)
# sumatoria = suma_sizes_clean_list(lista_limpia,path_to_find)
# print("path_to_inspect = ",path_to_inspect)
# # print("path_to_inspect_size = ",path_to_inspect_size)
# print("sumatoria = ",sumatoria)



# ######### Despliega datos del tiempo de ejecución

print("\n\n\n\n ################## TIEMPOS GLOBALES ###################")
display_times_end(tiempo_inicial)