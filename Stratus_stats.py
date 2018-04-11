import pandas as pd
import os
import pathlib
from datetime import datetime
import matplotlib.pyplot as plt
cwd = os.getcwd()

def get_date_from_stratus_summary(filename):
	# print(filename)
	drive = str(filename).split(":\\")
	# print(drive) 
	if(len(drive) == 2):
		filename2 = drive[1]
		d = filename2.split("_")[3].replace(".csv","")
		date = datetime.strptime(d, '%d%m%Y')
		# print(date)
	else:
		d=str(filename).split("_")[4].replace(".csv","")
		# print(d)
		date = datetime.strptime(d, '%d%m%Y')
		# print(date)

	return date


path_mm = "q:\\"

score_files = []
for item in pathlib.Path(path_mm).iterdir():
    if item.is_file():
        #print(type(get_date_from_stratus_summary(item)))
        if "summary_in" in str(item):

            # print(item)
            score_files.append(str(item))


used_size_history = []
for item in score_files:
    # print(item)
    date_score = get_date_from_stratus_summary(item)
    # print(date_score)
    df_score = pd.read_csv(item)
    used_size_score = df_score.loc[0].total_size
    uzn = float(used_size_score.replace("Tb",""))
    t = date_score
    tt = t.strftime('%m-%d-%Y')
    score_data = {"date_label":tt,"date":date_score,"used_size_label":used_size_score,"used_size":uzn}
    used_size_history.append(score_data)
    


df_used_size_history = pd.DataFrame(used_size_history)
print(df_used_size_history)


date_norm = pd.DatetimeIndex(df_used_size_history['date']).normalize()
g = df_used_size_history.groupby(pd.DatetimeIndex(df_used_size_history['date']).normalize())
prom = df_used_size_history.groupby([date_norm])['used_size'].mean().sort_values(ascending=False)

# print(prom)

total_mas_grande = df_used_size_history['used_size'].max()
print("\n Total_mas_grande:",total_mas_grande)



# Encontrar la fecha del total más grande
#print(df_used_size_history[df_used_size_history['used_size'] == total_mas_grande]['date'])

# Encontrar el row del total más grande
print(df_used_size_history[df_used_size_history['used_size'] == total_mas_grande])

# Promedio
print(df_used_size_history['used_size'].mean())



print("Historial por fechas")
print(df_used_size_history.sort('date'))
# print(df_used_size_history.sort('date').to_json(orient='records'))
# print(df_used_size_history.sort('date'))
# with open('temp.json', 'w') as f:
#     f.write(df_used_size_history.to_json(orient='records', lines=True))

# ax = df_used_size_history['date'].hist()
# fig = ax.get_figure()
# fig.savefig('figure2.png')


