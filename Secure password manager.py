from cryptography.fernet import Fernet
import threading
import time
import json
import os


def Write_key():
    """
    Generates a new encryption key and saves it to 'key.key' file.
    This key will be used to encrypt and decrypt passwords.
    """
    key = Fernet.generate_key()

    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def Load_key():
    """
    Loads the encryption key from 'key.key' file.

    Returns:
        bytes: The encryption key.
    """
    with open("key.key", "rb") as key_file:
        key = key_file.read()

        return key


key = Load_key()
fer = Fernet(key)

TIMEOUT = 90
logout_timer = None


def start_logout_timer():
    """
    Starts or resets the logout timer. If the user is inactive for
    the defined TIMEOUT duration, the program will automatically exit.
    """
    global logout_timer

    if logout_timer is not None:
        logout_timer.cancel()

    logout_timer = threading.Timer(TIMEOUT, automatic_logout)
    logout_timer.start()


def automatic_logout():
    """
   Executes automatic logout due to inactivity. Prints a message and
   exits the program.
   """
    print("\nAutomatic exit due to inactivity.")
    os._exit(0)


def Load_data():
    """
    Loads the password manager's data from 'manager.json' file.

    Returns:
        dict: The loaded data, or an empty dictionary if the file is empty or invalid.
    """
    with open("manager.json", "r") as json_file:
        try:
            data = json.load(json_file)
            return data
        except json.decoder.JSONDecodeError:
            return {}


def Write_data(filename, database):
    """
    Writes the current state of the password database to a JSON file.

    Args:
        filename (str): The name of the JSON file to write data to.
        database (dict): The password database to save.
    """
    with open(filename, "w") as json_file:
        json.dump(database, json_file)


def View_database(database):
    """
    Prints all accounts and their decrypted passwords stored in the database.

    Args:
        database (dict): The password database to view.
    """
    print("Database:")
    for account, password in database.items():
        print("Account:", account, "| Password:", str(fer.decrypt(password.encode())))


def Add_account(database):
    """
    Adds a new account and encrypted password to the database.

    Args:
        database (dict): The password database to update.
    """
    name = input('Account name: ')
    pwd = input('Password: ')

    database[name] = fer.encrypt(pwd.encode()).decode()


def Delete_account(database, account):
    """
    Deletes an account from the database.

    Args:
        database (dict): The password database to update.
        account (str): The account name to delete.

    Returns:
        bool: True if account was deleted, False if account was not found.
    """
    if account in database:
        del database[account]
        return True

    print("Account not found, try again.😅")
    return False


def Update_password(database, account):
    """
    Updates the password for an existing account in the database.

    Args:
        database (dict): The password database to update.
        account (str): The account name to update.

    Returns:
        bool: True if password was updated, False if account was not found.
    """
    if account in database:
        new_pwd = input("Enter new password: ")
        database[account] = fer.encrypt(new_pwd.encode()).decode()
        return True

    print("Account not found, try again.😅")
    return False


def main():
    """
    Main function to run the password manager. Presents a menu to
    the user to view, add, delete, or update accounts and their passwords.
    Automatically logs out the user after a period of inactivity.
    """
    database = Load_data()
    filename = "manager.json"
    start_logout_timer()

    print('Menu.\n'
    'View - view database.\n'
    'Add - add account.\n'
    'Delete - delete account.\n'
    'Update - update password.\n'
    '1 minute of inactivity - exit.\n')
    while (choice := input('Would you like to do (press q to quit)?🤔 ').lower()) != "q":
        start_logout_timer()
        match choice:
            case "view":
                if len(database) != 0:
                    View_database(database)
                else:
                    print("Database is empty.🫠")
            case "add":
                Add_account(database)
                print("Account added.😁")
            case "delete":
                account = input("Account name: ")
                if Delete_account(database, account):
                    print("Account has been deleted.😮‍💨")
            case "update":
                account = input("Account name: ")
                if Update_password(database, account):
                    print(f"{account}'s account password has been updated.🤨")
            case _:
                print("Invalid choice, try again.😅")

        print()

    Write_data(filename, database)
    print("Exiting😴...")
    os._exit(0)


if __name__ == "__main__":
    main()
