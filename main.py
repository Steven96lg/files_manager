import os
#import shutil
import utils as uls
import methods as mth


print(uls.options_descriptions)
option_selected = input("option>> ")

while not option_selected in uls.options_menu:
    option_selected = input("Seleccione un opcion valida>> ")

if(mth.export_methods[option_selected]):
    mth.export_methods[option_selected]["do"]()



