import time # Importamos time para la funcion exit

# Creamos la clase User para el manejo de los usuarios
class User: 
    def __init__(self, username, password, status):
        self.username = username  # Atributo de nombre de usuario
        self.password = password  # Atributo de contraseña
        self.status = status      # Atributo de estado (on/off)

    # Representación de los objetos User en formato de texto
    def __repr__(self):
        return f"User(username ='{self.username}', password ='{self.password}', Status = '{self.status}')"

# Añadimos algunos usuarios base para probar el sistema
DefaultUsers = [
    User('juanito123', '124', 'off'),  # Usuario 1
    User('juanito1234', '124', 'off'), # Usuario 2
    User('juanito1235', '124', 'off'), # Usuario 3
    User('diego123', '123', 'off'),    # Usuario 4
]
users = DefaultUsers[:]  # Creamos una copia de la lista de usuarios base

# Método de ordenamiento quicksort para ordenar los usuarios alfabéticamente
def quicksort(users):
    if len(users) <= 1:
        return users
    else:
        pivot = users[len(users) // 2]  # Elegimos el pivote como el usuario del medio
        left = [x for x in users if x.username < pivot.username]  # Los usuarios menores que el pivote
        middle = [x for x in users if x.username == pivot.username]  # Los usuarios iguales al pivote
        right = [x for x in users if x.username > pivot.username]  # Los usuarios mayores que el pivote
        return quicksort(left) + middle + quicksort(right)  # Llamamos recursivamente para ordenar los usuarios

# Método de búsqueda binaria para encontrar un usuario por nombre de usuario
def binary_search(users, username):
    low = 0
    high = len(users) - 1

    while low <= high:
        mid = (low + high) // 2
        if users[mid].username == username:  # Si encontramos el usuario
            return mid

        elif users[mid].username < username:  # Si el nombre es mayor, buscamos en la mitad superior
            low = mid + 1

        else:  # Si el nombre es menor, buscamos en la mitad inferior
            high = mid - 1

    return None  # Si no encontramos el usuario, devolvemos None

# Función de login para permitir a los usuarios iniciar sesión
def login():
    print("Login")
    username = input("Username: ")
    idx = binary_search(users, username)  # Buscamos al usuario por nombre de usuario

    if idx is not None:  # Si el usuario existe

        if users[idx].status == "off":  # Si el estado del usuario está 'off', no puede iniciar sesión
            print(f"Cannot login for {username} while status is 'off'.")
        else:
            print("Username found")
            password = input("Password: ")

            print("Checking password...")
            time.sleep(1)  # Simula la verificación de la contraseña
            if users[idx].password == password:  # Si la contraseña es correcta
                print("Password correct")
                print(f"Login successful, {username}")
                return users[idx]  # Devuelve el objeto de usuario

            else:  # Si la contraseña es incorrecta
                print("Incorrect password")

    else:  # Si el usuario no existe
        print("Username doesn't exist")
    return None  # Si no se pudo iniciar sesión, devolvemos None

# Función para registrar un nuevo usuario
def register():
    print("Register")

    username = input("Username: ")
    idx = binary_search(users, username)  # Verificamos si el usuario ya existe

    if idx is not None:  # Si el usuario ya existe, no permitimos el registro
        print("Username already exists")
    else:  # Si el usuario no existe, lo registramos
        password = input("Password: ")
        status = "off"  # El estado inicial del usuario es 'off'

        new_user = User(username, password, status)  # Creamos el nuevo objeto de usuario
        users.append(new_user)  # Añadimos el nuevo usuario a la lista
        users[:] = quicksort(users)  # Ordenamos la lista de usuarios

        print(f"Register successful, user {username}")
    return

# Función para editar un usuario
def eUser():
    print("Edit user")
    
    username = input("Username: ")
    idx = binary_search(users, username)  # Buscamos al usuario a editar

    if idx is not None:
        if users[idx].status == "off":  # Si el estado del usuario está 'off', no se puede editar
            print(f"Cannot edit user {username} while status is 'off'.")
        else:
            new_username = input("New username: ")  # Pedimos el nuevo nombre de usuario

            if binary_search(users, new_username) is not None:  # Si el nuevo nombre ya existe
                print("Username already exists")
            else:
                new_password = input("New password: ")  # Pedimos la nueva contraseña
                users[idx].username = new_username  # Actualizamos el nombre de usuario
                users[idx].password = new_password  # Actualizamos la contraseña
                users[:] = quicksort(users)  # Ordenamos nuevamente la lista

                print("User edited successfully")
    else:
        print("Username doesn't exist")  # Si el usuario no existe
    return

# Función para eliminar un usuario
def dAccount():
    print("Delete account")

    username = input("Username: ")
    idx = binary_search(users, username)  # Buscamos al usuario a eliminar

    if users[idx].status == "on":  # Si el usuario está 'on', no se puede eliminar
        print(f"Cannot delete account {username} while status is 'on'.")
    elif idx is not None:  # Si el usuario existe, lo eliminamos
        users.pop(idx)  # Eliminamos el usuario de la lista
        print(f"Account {username} deleted successfully")
    else:
        print("Username doesn't exist")  # Si el usuario no existe
    return

# Función para hacer logout de un usuario
def logout(user):
    print("Logout")

    if user:
        idx = binary_search(users, user.username)  # Buscamos al usuario para hacer logout

        if users[idx].status == "on":  # Si el estado del usuario es 'on', no se puede hacer logout
            print(f"Cannot logout while status is 'on' for {user.username}.")
        else:
            print(f"{user.username}, has logged out.")
    else:
        print("Nobody has been logged in.")  # Si nadie ha iniciado sesión

# Función para cambiar el estado de un usuario (on/off)
def toggle_status():
    print("Toggle status")

    username = input("Username: ")
    idx = binary_search(users, username)  # Buscamos al usuario

    if idx is not None:
        new_status = input("New status (on/off): ")  # Pedimos el nuevo estado

        if new_status == "on" or new_status == "off":  # Si el estado es válido
            users[idx].status = new_status  # Actualizamos el estado
            print(f"Status for {username} changed to '{new_status}'.")
        else:
            print("Invalid status. Please type exactly 'on' or 'off'.")
    else:
        print("Username doesn't exist")  # Si el usuario no existe
    return

# Función para salir del programa
def exit(user):
    print("Leaving")

    if user:  # Si hay un usuario conectado
        if user.status == "on":  # Si el estado del usuario es 'on', no podemos salir
            print(f"Cannot exit the program while the status of {user.username} is 'on'.")
            return  # Salimos de la función, no del programa

        print(f"{user.username}, has logged out.")  # Si el estado no es 'on', hacemos logout
    else:
        print("Nobody has been logged in.")  # Si no hay usuario logueado

    seconds = 3
    for i in range(seconds, 0, -1):  # Contamos regresivamente los segundos para salir
        print(f"{i} seconds remaining...")
        time.sleep(1)

    print("Bye")
    quit()  # Finaliza el programa si el estado no es "on"

# Main del programa, donde se presenta el menú y se ejecutan las opciones
user = None
while True:
    print("\nMenu:")  # Muestra el menú de opciones
    print("1. Login")
    print("2. Register")
    print("3. Edit user")
    print("4. Delete account")
    print("5. Logout")
    print("6. Toggle user status")
    print("7. Exit")

    command = int(input("What do you want to do?: "))  # Entrada de opción del menú

    if command == 1:  # Si la opción es 1, se hace login
        user = login()

    elif command == 2:  # Si la opción es 2, se registra un nuevo usuario
        register()

    elif command == 3:  # Si la opción es 3, se edita un usuario
        eUser()

    elif command == 4:  # Si la opción es 4, se elimina un usuario
        dAccount()

    elif command == 6:  # Si la opción es 6, se cambia el estado de un usuario
        toggle_status()

    elif command == 7:  # Si la opción es 7, se sale del programa
        exit(user)
        break