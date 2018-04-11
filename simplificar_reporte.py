import pandas as pd
import os
import pathlib
from datetime import datetime
cwd = os.getcwd()


#### Funciones

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

#### Fin de Funciones





### Get lista de reportes ###
path_mm = "C:\\Users\\enrique.nieto\\Documents\\develops 2017\\Milenio\\Dashboard\\vxv\\"

score_files = []
for item in pathlib.Path(path_mm).iterdir():
	if item.is_file():
		#print(type(get_date_from_stratus_summary(item)))
		if "out" in str(item):
			# print(item)
			score_files.append(str(item))


## Simplificar los reportes

print("\n\n################# SCORES: ###########################")
print(score_files)
print("\n\n\n\n\n\n\n\n\n\n\n")

with open(score_files[6],"r") as f:
	current_report = f.readlines()

### Fin Get lista de reportes ###



### Generar la lista limpia de dirs ###


line_breaker_conditio = [".db\\",".cmf\\"]
path_to_inspect="V:\\media\\"
path_to_inspect="V:\\media\\Especiales Noticias\\CONVENCION BANCARIA\\"
path_to_inspect_size = 0


discard_list = []
clean_list_1 = []
clean_list = []
stream_limit = 2000
fisrt_pass = False

for breaker in line_breaker_conditio:
	print(breaker)
	if(fisrt_pass == False):
		# First pass toma una muestra de los datos y genera una primer lista limpia
		# descarta el primer breaker
		for i in range(0,stream_limit):
			print(str(i)+"  "+current_report[i])
			item = current_report[i]
			breaker = line_breaker_conditio[0]
			if(breaker in item):
				print("---Descartar")
			else:
				# clean_list.append(item)
				if(find_item(item,clean_list) == False):
					if(find_item(item,discard_list)==False):
						print("AGREGA: ",item)
						clean_list.append(item)
				else:
					print("NO AGREGA: ", item)
					discard_list.append(item)
		fisrt_pass = True
	else:
		print("next pass")



# for i in range(0,5000):
# 	print(str(i)+"  "+current_report[i])
# 	item = current_report[i]

# 	# for breaker in line_breaker_conditio:
	
# 	breaker = line_breaker_conditio[0]
# 	if(breaker in item):
# 		print("---Descartar")
# 	else:
# 		# clean_list.append(item)
# 		if(find_item(item,clean_list) == False):
# 			if(find_item(item,discard_list)==False):
# 				print("AGREGA: ",item)
# 				clean_list.append(item)
# 		else:
# 			print("NO AGREGA: ", item)
# 			discard_list.append(item)


# for item in clean_list:
# 	breaker = line_breaker_conditio[1]
# 	if(breaker in item):
# 		print("---Descartar")
# 	else:
# 		# clean_list.append(item)
# 		if(find_item(item,clean_list_1) == False):
# 			if(find_item(item,discard_list)==False):
# 				print("AGREGA: ",item)
# 				clean_list_1.append(item)
# 		else:
# 			print("NO AGREGA: ", item)
# 			discard_list.append(item)

# ### Fin Generar la lista limpia de dirs ###



# print("\n\n \n\n \n\n########## Clean List ###########")
# line_counter = 0
# sumatoria = 0



# for item in clean_list_1:
# 	line_counter+=1
# 	print(str(line_counter)+"  "+item)

# 	###### Extraer el peso ########
	
# 	if(item == clean_list_1[0]):
# 		print("cabezal")
# 	elif(path_to_inspect in item):
# 		print("SUMAR")
	
# 		# item_split = item.split(",")
# 		# sumatoria+=int(item_split[2])
# 		# print(item_split[2])
# 		size = get_size_bytes(item)
# 		sumatoria+=size
		
# 	else:
# 		print("---ITEM---",item)
# 		path_to_inspect_size = get_size_bytes(item)

# print("path_to_inspect_size = ",path_to_inspect_size)
# print("sumatoria = ",sumatoria)