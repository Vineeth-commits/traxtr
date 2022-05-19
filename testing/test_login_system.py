import re   
import time
import pymongo

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

myclient = pymongo.MongoClient("mongodb+srv://traxtr-admin:traxtr-passkey123@traxtr-cluster.nptfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = myclient["traxtr"]
db_col = db["login_system"]

def test_check_existing_user(username):
    username_insert = {"user": username}
    users = []
    db_doc = db_col.find(username_insert)
    for x in db_doc:
        users.append(x)
    if not users:
        return False
    else:
        return True

def test_password_check(username,password):
    password_insert = {"user":username,"password":password}
    passwords = []
    db_doc = db_col.find(password_insert)
    for x in db_doc:
        passwords.append(x)
    if not passwords:
        return False
    else:
        return True

def test_database_insert(username,password,email):
    db_insert= { "user": username, "password": password, "role":"basic_user","email":email}
    db_col.insert_one(db_insert)

def test_login():
    login_attempts = 0
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        if login_attempts==4:
            print("You have exceeded your login attempts")
            return 0
        if not test_check_existing_user(username):
            print("Incorrect username")
            login_attempts += 1
            continue
        else:
            break
    login_attempts = 0
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        if login_attempts==4:
            print("You have exceeded your attempts")
            return 0
        if not test_password_check(username,password):
            print("Incorrect password")
            login_attempts +=1
            continue
        else:
            return username

def test_register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        if (test_check_existing_user(username)):
            print("Username taken")
            print("choose different username")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    while True:
        email = input("Email: ")
        if(re.search(regex,email)):
                break
        else:
            print("Enter a valid email address")
            continue
    print("Creating account...")
    test_database_insert(username,password,email)
    time.sleep(1)
    print("Account has been created")

def test_get_id_by_username(username):
    return db_col.find_one({"user":username})["_id"]
