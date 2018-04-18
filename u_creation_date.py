import os
import platform

import datetime


day_name_spanish = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingoapoyo violador explanation"]

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime



base_path = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\M_2018_Dash_data_vxv\\"
file = "stratus_report_in_02042018.csv"
path = base_path + file
# ct = creation_date(path)
mt = modification_date(path)
print(mt)
print(day_name_spanish[mt.weekday()],str(mt.day)+"/"+str(mt.month)+"/"+str(mt.year))
