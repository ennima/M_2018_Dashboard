import os
import pathlib
from datetime import datetime
import math

import time
from time import time as time_i

path_mm = "V:\\media\\"
score_files = []
for item in pathlib.Path(path_mm).iterdir():
	# print(item)
	if item.is_file():
		# print(type(get_date_from_stratus_summary(item)))
		pass
	else:
		print(str(item).replace(path_mm,""))