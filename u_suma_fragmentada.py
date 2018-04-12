import os
import math

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

		# out_last = out
		first_step = False
	elif((i+1) == steps):
		print("last step")
		ini = out + 1
		out = total
		print("	"+str(ini)+","+str(out))
		#made action
	else:
		print("Step Intermedio")
		ini = out + 1
		out = ini + step_size
		print("	"+str(ini)+","+str(out))
		#made action




