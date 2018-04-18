import os
import pathlib
from datetime import datetime
import math

import time
from time import time as time_i

path_mm = "V:\\media\\"

def ls_dir_path(path_mm):
	score_files = []
	for item in pathlib.Path(path_mm).iterdir():
		if item.is_file():
		
			pass
		else:
			print(str(item).replace(path_mm,""))
	return score_files


score_files = ls_dir_path(path_mm)
print(score_files)


