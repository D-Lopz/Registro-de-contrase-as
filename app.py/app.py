import time

class User:
    def __init__(self, username, password, status):
        self.username = username
        self.password = password
        self.status = status

    def __repr__(self):
        return f"User(username ='{self.username}', password ='{self.password}', Status = '{self.status}')"

DefaultUsers = [
    User('juanito123', '124', 'off'),
    User('juanito1234', '124', 'off'),
    User('juanito1235', '124', 'off'),
    User('diego123', '123', 'off'),
]
users = DefaultUsers[:]

def quicksort(users):
    if len(users) <= 1:
        return users
    else:
        pivot = users[len(users) // 2]
        left = [x for x in users if x.username < pivot.username]
        middle = [x for x in users if x.username == pivot.username]
        right = [x for x in users if x.username > pivot.username]
        return quicksort(left) + middle + quicksort(right)


def binary_search(users, username):

    low = 0
    high = len(users) - 1

    while low <= high:

        mid = (low + high) // 2
        if users[mid].username == username:
            return mid

        elif users[mid].username < username:
            low = mid + 1

        else:
            high = mid - 1

    return

def login():

    print("Login")
    username = input("Username: ")
    idx = binary_search(users, username)

    if idx is not None:

        if users[idx].status == "off":
            print(f"Cannot login for {username} while status is 'off'.")

        else:
            print("Username found")
            
            password = input("Password: ")

            print("Checking password...")
            time.sleep(1)
            print("Password checked")            

            if users[idx].password == password:

                print("Password correct")
                print(f"Login successful, {username}")
                return users[idx]

            else:
                print("Incorrect password")

    else:
      print("Username doesn't exist")
    return None

def register():
    print("Register")

    username = input("Username: ")
    idx = binary_search(users, username)

    if idx is not None:
        print("Username already exists")
         
    else:            
        password = input("Password: ")
        status = "off"

        new_user = User(username, password, status)
        users.append((new_user))
        users[:] = quicksort(users)

        print(f"Register successful, user {username}")
    return

def eUser():
    print("Edit user")
    
    username = input("Username: ")
    idx = binary_search(users, username)

    if idx is not None:
        if users[idx].status == "off":
            print(f"Cannot edit user {username} while status is 'off'.")
    
        else:
            new_username = input("New username: ")

            if binary_search(users, new_username) is not None:
                print("Username already exists")

            else:
                new_password = input("New password: ")
                users[idx].username = new_username
                users[idx].password = new_password
                users[:] = quicksort(users)

                print("User edited successfully")
    else:
        print("Username doesn't exist")
    return

def dAccount():
    print("Delete account")

    username = input("Username: ")
    idx = binary_search(users, username)

    if users[idx].status == "on":
            print(f"Cannot delete account {username} while status is 'on'.")

    elif idx is not None:
        users.pop(idx)
        print(f"Account {username} deleted successfully")

    else:
        print("Username doesn't exist")

    return

def logout(user):
    print("Logout")

    if user:
        
        idx = binary_search(users, user)

        if users[idx].status == "on":
            print(f"Cannot logout while status is 'on' for {user}.")
            
        else:
            print(f"{user}, has logged out.")

    else:
        print("Nobody has been logged in.")

def toggle_status():
    print("Toggle status")

    username = input("Username: ")
    idx = binary_search(users, username)

    if idx is not None:
        new_status = input("New status (on/off): ")

        if new_status == "on" or new_status == "off":
            users[idx].status = new_status
            print(f"Status for {username} changed to '{new_status}'.")
        
        else:
            print("Invalid status. Please type exactly 'on' or 'off'.")
    
    else:
       print("Username doesn't exist")
    return

def exit(user):
    print("Leaving")

    if user:
        if user.status == "on":
            print(f"Cannot exit the program while the status of {user.username} is 'on'.")
            return  # Salimos de la función, no del programa

        print(f"{user.username}, has logged out.")
    else:
        print("Nobody has been logged in.")

    seconds = 3

    for i in range(seconds, 0, -1):
        print(f"{i} seconds remaining...")
        
        time.sleep(1)

    print("Bye")
    quit()  # Finaliza el programa si el estado no es "on"


user = None
while True:
    print("\nMenu:")
    print("1. Login")
    print("2. Register")
    print("3. Edit user")
    print("4. Delete account")
    print("5. Logout")
    print("6. Toggle user status")
    print("7. Exit")

    command = int(input("What do you want to do?: "))

    if command == 1:
        user = login()

    elif command == 2:
        register()

    elif command == 3:
        eUser()

    elif command == 4:
        dAccount()

    elif command == 6:
        toggle_status()

    elif command == 7:
        exit(user)
        break