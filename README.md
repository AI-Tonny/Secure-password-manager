# Secure Password Manager

This project is a secure password manager implemented in Python. It encrypts passwords using the `cryptography` library and securely stores them in a JSON file. Users can add, view, update, and delete accounts with encrypted passwords. The program has an inactivity timer that automatically logs out users after a set period to enhance security.

## Features
- **Add a new account and password**
- **View existing accounts**
- **Update the password for an account**
- **Delete an account**
- **Automatic logout after 1 minute of inactivity**

## Requirements
- Python 3.7 or later
- `cryptography` library

### Install the library
```bash
pip install cryptography
```
## Main Files
- **manager.json** - stores encrypted password data in JSON format.
- **key.key** - stores the encryption key, generated only once.

## Key Functions
**Generate an Encryption Key**

The ```Write_key``` function generates an encryption key if it doesn't already exist and saves it to the ```key.key`` file.
```
def Write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
```
**Load the Encryption Key**

The ```Load_key``` function reads the saved key from ```key.key```.
```
def Load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key
```
**Automatic Logout Timer**

The ```start_logout_timer``` function starts a timer that automatically logs out the program after 60 seconds of inactivity.
```
def start_logout_timer():
    global logout_timer
    if logout_timer is not None:
        logout_timer.cancel()
    logout_timer = threading.Timer(TIMEOUT, automatic_logout)
    logout_timer.start()
```
**Load and Save Data**

The ```Load_data``` and ```Write_data``` functions read and save data to ```manager.json```.
```
def Load_data():
    with open("manager.json", "r") as json_file:
        try:
            data = json.load(json_file)
            return data
        except json.decoder.JSONDecodeError:
            return {}

def Write_data(filename, database):
    with open(filename, "w") as json_file:
        json.dump(database, json_file)
```
**Account Operations**

- **View Database (View_database): displays all accounts and passwords in decrypted form.**
- **Add Account (Add_account): reads an account name and password, encrypts the password, and saves it to the database.**
- **Delete Account (Delete_account): removes an account if it exists in the database.**
- **Update Password (Update_password): updates the encrypted password for an existing account.**

**Usage Example**

After starting, the program prompts the user to choose an operation:

- **view** - view the database
- **add** - add a new account
- **delete** - delete an account
- **update** - update a password
- **q** - exit the program

**Running the Project**
1. Copy the files to your working directory.
2. Run the program from the command line:
```python Secure_password_manager.py```
3. Follow the on-screen instructions to manage the password database.
