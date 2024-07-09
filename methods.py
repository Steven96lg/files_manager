
import os
import shutil
import utils as uls

####
def delete_method():
    print("metodo para eliminar")

####### Metodo para organizar los archivos en carptas
def organize_method():
    files_to_list = os.getcwd()
    files_to_organize = os.listdir(files_to_list)

    for file_name in files_to_organize:
        file_path = os.path.join(files_to_list, file_name)
        name, extension = os.path.splitext(file_path)

        # Recorre el diccionario para ver los tipos y crear las carpetas
        for file_dict in uls.files_dictionary:
            target_folder = file_dict["file"]
            if file_dict["type"] == extension.lstrip("."):
                # Verifica si la carpeta de destino existe, si no, créala
                if not os.path.exists(target_folder):
                    os.mkdir(target_folder)
                
                # Mueve el archivo al directorio de destino
                shutil.move(file_path, os.path.join(files_to_list, target_folder, file_name))

def show_all_files():
    print(uls.files_list_print)
    files_to_list = os.getcwd()
    files_to_show = os.listdir(files_to_list)

    for file in files_to_show:
        print(f"== {file}")


#funciones a exportar
export_methods = {
    "showfiles":{
        "do": show_all_files
    },
    "delete":{
        "do": delete_method
    },
    "organize": {
        "do": organize_method
    }
}