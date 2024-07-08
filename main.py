import os
import shutil
import utils as uls
import methods as mth

current_directory = os.getcwd()
files_list = os.listdir(current_directory)

print("============ Lista de Archivos ==============")
# Imprime todos los archivos dentro del directorio actual
for file in files_list:
    file_path = os.path.join(current_directory, file)
    print(file, " ", os.path.getsize(file_path))

print(uls.options_descriptions)
option_selected = input("option>> ")

while not option_selected in uls.options_menu:
    option_selected = input("Seleccione un opcion valida>> ")

if(mth.export_methods[option_selected]):
    mth.export_methods[option_selected]["do"]()



'''
print("inciando el proceso")
# Recorre los archivos dentro del directorio
for file_name in files_list:
    file_path = os.path.join(current_directory, file_name)
    name, extension = os.path.splitext(file_path)

    # Recorre el diccionario para ver los tipos y crear las carpetas
    for file_dict in uls.files_dictionary:
        target_folder = file_dict["file"]
        if file_dict["type"] == extension.lstrip("."):
            # Verifica si la carpeta de destino existe, si no, créala
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)
            
            # Mueve el archivo al directorio de destino
            shutil.move(file_path, os.path.join(current_directory, target_folder, file_name))

'''