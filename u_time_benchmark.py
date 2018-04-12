import time
from datetime import datetime
from time import time as time_i

tiempo_inicial = time_i() 




tiempo_final = time_i()
tiempo_ejecucion = tiempo_final - tiempo_inicial


print("Tardó: " , tiempo_ejecucion,"s")
m, s = divmod(tiempo_ejecucion, 60)
h, m = divmod(m, 60)
restore_time = "%02d:%02d:%02d" % (h, m, s)
print ("Tardó:",restore_time)