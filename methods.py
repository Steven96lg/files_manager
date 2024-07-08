
def delete_method():
    print("metodo para eliminar")

def organize_method():
    print("metodo para organizar")



#funciones a exportar
export_methods = {
    "delete":{
        "do": delete_method
    },
    "organize": {
        "do": organize_method
    }
}