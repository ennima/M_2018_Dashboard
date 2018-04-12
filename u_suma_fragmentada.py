###############################################################
# 	Función que ayuda a realizar procesos de manera fragmentada
# 	dando más eficiencia a la ejecución de procesos que
# 	necesitan procesar grandes cantidades de datos pero 
#	con muy pocos recursos
###############################################################
import os
import math

def x(a,b):
	print("Param 1 %s param 2 %s"%(a,b))

def x2(a1,b1,a,b):
	print("%s, %s QUE loco 1 %s param 2 %s"%(a1,b1,a,b))

def y(z,t):
	z(*t)



def proceso_fragmentado(tarea_ejecutar,parametros,total,steps):
	
	case_type_string = type("hola")
	case_type_tuple = type(("hola","que tal"))
	this_type = ""
	print("LEN PARAM: ",len(parametros))
	print("Type Param:",type(parametros))

	if(case_type_tuple == type(parametros)):
		print("---  Es una tupla papa")
		this_type = "tuple"
	elif(case_type_string == type(parametros)):
		print("--- String")
		this_type = "str"

	total = 101
	steps = 2

	step_size = math.floor(total / steps)

	print(step_size)

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
				print("OKI")
				print(parametros[0])
				print(parametros[1])
				if(parametros[0] == "in_out"):
					if(type(parametros[1]) == case_type_tuple):
						parametrosN = parametros[1] + (str(ini),str(out))
						print(parametrosN)

						tarea_ejecutar(*parametrosN)
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
			
		else:
			print("Step Intermedio")
			ini = out + 1
			out = ini + step_size
			print("	"+str(ini)+","+str(out))
			#made action
			if(this_type == "str"):
				if(parametros == "in_out"):
					tarea_ejecutar(ini,out)
				else:
					tarea_ejecutar(*parametros)



## ¿Cómo usar?
# proceso_fragmentado(x,("in_out",("lol"),100,5)

proceso_fragmentado(x2,("in_out",("lol","lalala")),100,5)

print("\n\n\n")
proceso_fragmentado(x,("in_out"),100,5)

print("\n\n\n")
proceso_fragmentado(x,("in_out","lol"),100,5)


