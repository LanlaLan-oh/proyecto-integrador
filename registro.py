def validar_registro(nombre):
    if not nombre.strip():
        return "Error: El campo nombre es obligatorio."
    return "Registro válido."