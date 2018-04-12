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

def y(z,t):
	z(*t)



def proceso_fragmentado(tarea_ejecutar,parametros,total,steps):
	

	total = 101
	steps = 10

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
			if(parametros == "in_out"):
				tarea_ejecutar(ini,out)
			else:
				tarea_ejecutar(*parametros)

			# out_last = out
			first_step = False
		elif((i+1) == steps):
			print("last step")
			ini = out + 1
			out = total
			print("	"+str(ini)+","+str(out))
			#made action
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
			if(parametros == "in_out"):
				tarea_ejecutar(ini,out)
			else:
				tarea_ejecutar(*parametros)



## ¿Cómo usar?
proceso_fragmentado(x,("in_out","lol"),100,5)

proceso_fragmentado(x,("in_out"),100,5)




