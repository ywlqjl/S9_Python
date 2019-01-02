import hashlib
from tkinter import *
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import json


salt = 'python_tp'


def pack_login_pwd(login, password):
    with open('userinfo.json', "r", encoding='utf-8') as f:
        try:
            all_data = json.load(f)
        except:
            all_data = []

    data = {}
    data['login'] = login


    # utilise assert
    try:
        assert isinstance(salt, str)
    except AssertionError as ae:
        print(ae)

    password = salt + password + login
    mdp = hashlib.sha256(password.encode()).hexdigest()

    data['password'] = mdp
    all_data.append(data)

    return all_data


def store_data(login, password):
    packed_data = pack_login_pwd(str(login.get()), str(password.get()))

    with open('userinfo.json', "w") as f:
        json.dump(packed_data, f)
    # password.delete(0,END)
    messagebox.showinfo("Success", "User information stored")

def verify(login, password):
    with open('userinfo.json', "r", encoding='utf-8') as f:
        try:
            all_data = json.load(f)
        except:
            messagebox.showerror("Error", "Empty database")
            return None
    login_text = str(login.get())
    password_text = str(password.get())
    password = salt + password_text + login_text
    pwd_text = hashlib.sha256(password.encode()).hexdigest()

    for info in all_data:
        if info['login'] == login_text and info['password'] == pwd_text:
            messagebox.showinfo("Success","Verification passed")
            return 1
    messagebox.showinfo("Error", "User information error")

def crypto_file(filename, password):

    try:
        key = password
        cipher = AES.new(key, AES.MODE_EAX)
        with open(str(filename.get()), 'r') as f:
            data = f.read()
        ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf8"))
        file_out = open("encrypted.bin", "wb")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    except FileNotFoundError as fe:
        messagebox.showinfo("Error", fe)

def crypto(login, password):
    new_window = Tk()
    new_window.title("Crypto")
    filename = Entry(new_window, width=15)
    label = Label(new_window, text="Filename").grid(row=1, column=1)
    filename.grid(row=1, column=2)

    login_text = str(login.get())
    password_text = str(password.get())
    password = salt + password_text + login_text
    pwd_text = hashlib.sha256(password.encode()).digest()
    ok = Button(master=new_window, text='Ok', relief=RIDGE, width=5, command=lambda: crypto_file(filename,pwd_text)).grid(row=2,
                                                                                                               column=1)


bg = Tk()
bg.title('User Info')

login_label = Label(bg, text="Login").grid(row=1, column=1)
login = Entry(bg, width=15)
login.grid(row=1, column=2)

pwd_label = Label(bg, text="Password").grid(row=2, column=1)
password = Entry(bg, show="*", width=15)
password.grid(row=2, column=2)

ok = Button(master=bg, text='Store info', relief=RIDGE, width=10, command=lambda: store_data(login, password)).grid(row=3, column=1)

verify_btn = Button(master=bg, text='Verify', relief=RIDGE, width=5, command=lambda: verify(login, password)).grid(row=3, column=2)

crypto_btn = Button(master=bg, text='Crypto', relief=RIDGE, width=5, command=lambda: crypto(login,password)).grid(row=3, column=3)


mainloop()
