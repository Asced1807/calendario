from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Usuarios"], responses = {404: {"Mensaje": "Ruta no encontrada"}}) # opciones para agregar en nuestra api de la ruta definida, nombre de la api o titulo, respuesta a un error especifico

class Usuario (BaseModel):  # Esquema de la clase
    Id: int
    Nombre: str
    Apellido: str
    Edad: int
    Sexo: str  # [M, F]
    Bio: str

# lista 
listaUsuarios = [ Usuario(Id = 1, Nombre = 'Juan', Apellido = 'Perez', Edad = 18, Sexo = 'M', Bio = 'Hola soy nuevo'),
                 Usuario(Id = 2, Nombre = 'Brea', Apellido = 'Los Santos', Edad = 20, Sexo = 'M', Bio = 'Hola soy nuevo, y me gusta cantar'),
                 Usuario(Id = 3, Nombre = 'Luis', Apellido = 'calderon', Edad = 20, Sexo = 'M', Bio = 'Hola'),
                 Usuario(Id = 4, Nombre = 'Ana', Apellido = 'González', Edad = 25, Sexo = 'F', Bio = 'Me encanta la música'),
                 Usuario(Id = 5, Nombre = 'María', Apellido = 'López', Edad = 30, Sexo = 'F', Bio = 'Amo viajar y explorar nuevos lugares'),
                 Usuario(Id = 6, Nombre = 'Laura', Apellido = 'Pérez', Edad = 28, Sexo = 'F', Bio = 'Apasionada por la cocina y la comida saludable'),
                 Usuario(Id = 7, Nombre = 'Juan', Apellido = 'Perez', Edad = 12, Sexo = 'M', Bio = 'Hola soy nuevo'),]


'''@router.get('/')
async def listaJoin():
    return [{'id': 1, 'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 18, 'Sexo': 'M', 'Bio': 'Hola soy nuevo'},
                 {'id':2, 'Nombre': 'Brea', 'Apellido': 'Los Santos', 'Edad': 20, 'Sexo': 'M', 'Bio': 'Hola soy nuevo, y me gusta cantar '},
                 {'id':3, 'Nombre': 'Luis', 'Apellido': 'calderon', 'Edad': 20, 'Sexo': 'M', 'Bio': 'Hola'},
                 {"id": 5, "Nombre": "Ana", "Apellido": "González", "Edad": 25, "Sexo": "F", "Bio": "Me encanta la música."},
                 {"id": 6, "Nombre": "María", "Apellido": "López", "Edad": 30, "Sexo": "F", "Bio": "Amo viajar y explorar nuevos lugares."},
                 {"id": 7, "Nombre": "Laura", "Apellido": "Pérez", "Edad": 28, "Sexo": "F", "Bio": "Apasionada por la cocina y la comida saludable."}]'''
# decoradores 
@router.get('/')
async def listaUsuario():
    return listaUsuarios


@router.get('/{id}')
async def buscar(Id: int):
    return buscaUsuario(Id)


@router.post('/')
async def usuarioCreado(usuario: Usuario):
    if type(buscaUsuario(usuario.Id)) == Usuario:
        return {"Error": "El usuario ya existe"}
    else:
        listaUsuarios.append(usuario)


@router.put("/{id}")
async def actualizado(id: int, nombre: str, apellido: str, edad: int, sexo: str, bio: str):
    return actualizarUsuario(id, nombre, apellido, edad, sexo, bio)


@router.delete("/{id}")
async def usuarioEliminado(Id: int):
    return eliminarUsuario(Id)





# funciones 
def buscaUsuario(Id: int):
    users = filter(lambda usuario: usuario.Id == Id, listaUsuarios)
    try:
        return list(users)[0]
    except:
        return {"error": f"No se encontró un usuario con ID {Id}"}


'''def createUsuarios(createUsu: Usuario):
    registros = {
        "Id": createUsu.Id,
        "Nombre": createUsu.Nombre.title(),
        "Apellido": createUsu.Apellido.title(),
        "Edad": createUsu.Edad,
        "Sexo": createUsu.Sexo,
        "Bio": createUsu.Bio.title()
    }
    listaUsuarios.append(registros)
    return {'Registro': 'Ya estas Registrado el Usuario:) '}'''


def actualizarUsuario(id: int, nombre: str, apellido: str, edad: int, sexo: str, bio: str):
    for usuario in listaUsuarios:
        if usuario.Id == id:  
            usuario.Nombre = nombre
            usuario.Edad = edad
            usuario.Apellido = apellido
            usuario.Sexo = sexo
            usuario.Bio = bio
            return {"mensaje": f"Usuario actualizado correctamente"}
    else:
        return {"error": f"No se encontró un usuario con ID {id}"}
    

#metodo 1
def eliminarUsuario(id: int):
    for usuario1 in listaUsuarios:
        if usuario1.Id == id:
            listaUsuarios.remove(usuario1)
            return {"mensaje": f"Usuario eliminado correctamente"}
    else:
        return {"error": f"No se encontró un usuario con ID {id}"}


# metodo 2 este seria como una lista
'''async def eliminarUsuario(id: int):
    for usuario, usuario1 in enumerate(listaUsuarios):
        if usuario1.Id == id:
            # Utiliza del para eliminar el usuario con el ID especificado
            del listaUsuarios[usuario]
            return {"mensaje": f"Usuario con ID {id} eliminado correctamente"}
    
    return {"error": f"No se encontró un usuario con ID {id}"}'''


