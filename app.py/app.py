import time

DefaultUsers = [
    ('juanito123', '124'),
    ('juanito1234', '124'),
    ('juanito1235', '124'),
    ('diego123', '123'),
]
users = DefaultUsers[:]

def quicksort(users):

    if len(users) <= 1:
        return users
    else:

        pivot = users[len(users) // 2]
        left = [x for x in users if x[0] < pivot[0]]
        middle = [x for x in users if x[0] == pivot[0]]
        right = [x for x in users if x[0] > pivot[0]]

        return quicksort(left) + middle + quicksort(right)

def binary_search(users, username):

    low = 0
    high = len(users) - 1

    while low <= high:

        mid = (low + high) // 2
        if users[mid][0] == username:
            return mid

        elif users[mid][0] < username:
            low = mid + 1

        else:
            high = mid - 1

    return None

def login():

    print("Login")
    username = input("Username: ")
    idx = binary_search(users, username)

    if idx is not None:

        print("Username found")
        password = input("Password: ")
        print("Checking password...")
        time.sleep(1)
        print("Password checked")

        if users[idx][1] == password:

            print("Password correct")
            print(f"Login successful, {username}")
            return username

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
        users.append((username, password))
        users[:] = quicksort(users)

        print(f"Register successful, user {username}")
    return

def eUser():
    print("Edit user")

    username = input("Username: ")
    idx = binary_search(users, username)

    if idx is not None:
        new_username = input("New username: ")

        if binary_search(users, new_username) is not None:
            print("Username already exists")

        else:
            new_password = input("New password: ")
            users[idx] = (new_username, new_password)
            users[:] = quicksort(users)

            print("User edited successfully")
    else:
        print("Username doesn't exist")
    return

def dAccount():
    print("Delete account")

    username = input("Username: ")
    idx = binary_search(users, username)

    if idx is not None:
        users.pop(idx)
        print(f"Account {username} deleted successfully")

    else:
        print("Username doesn't exist")
    return

def logout(user):
    print("Logout")

    if user:
        print(f"{user}, has logged out.")

    else:
        print("Nobody has been logged in.")

def exit(user):
    print("Leaving")

    if user:
        print(f"{user}, has logged out.")

    else:
        print("Nobody has been logged in.")
    seconds = 3

    for i in range(seconds, 0, -1):
        print(f"{i} seconds remaining...")
        time.sleep(1)

    print("Bye")

user = None
while True:
    print("\nMenu:")
    print("1. Login")
    print("2. Register")
    print("3. Edit user")
    print("4. Delete account")
    print("5. Logout")
    print("6. Exit")

    command = int(input("What do you want to do?: "))

    if command == 1:
        user = login()

    elif command == 2:
        register()
        print(users)

    elif command == 3:
        eUser()

    elif command == 4:
        dAccount()

    elif command == 5:
        logout(user)

    elif command == 6:
        exit(user)
        break