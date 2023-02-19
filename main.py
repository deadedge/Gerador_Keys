import datetime
from tkinter import messagebox

import customtkinter

import tkinter
import secrets
from plyer import notification
from google.cloud import firestore

import firebase_admin
from customtkinter import CTkEntry
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

cred = credentials.Certificate(r"C:\Users\JoaoP\Downloads\gerador-pass-firebase-adminsdk-jq5tz-e946967ec9.json")

appFirebase = firebase_admin.initialize_app(cred)

db = firestore.client()
app = customtkinter.CTk()


def VerifiUser(nomeUser, key):
    users_ref = db.collection(u"User")
    docs = users_ref.stream()

    for doc in docs:
        nomeUserFireBase = doc.to_dict()['NameUser']
        keyUserFire = doc.to_dict()['Key']
        if nomeUser == nomeUserFireBase:
            messagebox.showerror(title='error', message='Nome utilizador ja usado')
            return False
        elif keyUserFire == key:
            messagebox.showerror(title='error', message='Esta key ja foi usada')
            return False
        else:
            return True

    return True


# Criar nove key
def ADDNewKey():
    key = secrets.token_hex(64)
    now = datetime.now()
    dia = now.strftime('%d/%m/%Y')

    doc_ref = db.collection(u'Keys').document()
    doc_ref.set({
        u'Key': key,
        u'Day': dia,
        u'DayFinish': "12/02/3023",  # isto tem que ser mudado tem que ser feito uma verificacao antes
        u'Duracao': u'lifetime',
        u'Usada': False
    })


def VerifiKey(key):
    door=False
    users_ref = db.collection(u"Keys")
    docs = users_ref.stream()
    now = datetime.now()
    day = now.strftime('%d/%m/%Y')
    ####Contar documentos####
    collection_ref = db.collection(u'Keys')
    # conta o número de documentos na coleção
    docss = collection_ref.get()
    num_docs = len(docss)
    i = 0
    for doc in docs:
        i += 1
        dayFinish = doc.to_dict()['DayFinish']
        keyFireBase = doc.to_dict()['Key']
        keyUse = doc.to_dict()['Usada']
        if keyFireBase != key:
            door=True
            if i == num_docs:
                messagebox.showerror(title='error', message='Key não existe')
            return False
        elif day >= dayFinish:
            messagebox.showerror(title='error', message='Key expirada')
            return False
        elif keyUse:
            messagebox.showerror(title='error', message='Key ja utilizada')
            return False
        else:
            return True


def VerifiInput(nomeUser, passUser, email, key):
    if nomeUser == "" or passUser == "" or email == "" or key == "":
        messagebox.showerror(title='Error', message='Preencha todos os campos para prosseguir')
        return False
    else:
        return True


# Criar novo Usuario
def AddNewAccout(email, nomeUser, passUser, key):
    if VerifiInput(nomeUser, passUser, email, key):
        if VerifiKey(key):
            if VerifiUser(nomeUser, key):
                doc_ref = db.collection(u'User').document()
                doc_ref.set({
                    u'NameUser': nomeUser,
                    u'Pass': passUser,
                    u'Email': email,
                    u'Key': key
                })
                messagebox.showinfo(title='success', message='Conta criada com sucesso')


# pagina de registro
def LayoutRegister():
    app.destroy()
    app2 = customtkinter.CTk()
    app2.geometry("600x400")
    app2.title('Register')

    frame = customtkinter.CTkFrame(app2, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l1 = customtkinter.CTkLabel(master=frame, text="Register", font=('Century Gothic', 20))
    l1.place(x=138, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Email")
    entry1.place(x=50, y=105)  # tenho que muda ro valor para aparecer

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
    entry2.place(x=50, y=150)

    entry3 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password", show="*")
    entry3.place(x=50, y=195)

    entry4 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Key")
    entry4.place(x=50, y=240)

    btn1 = customtkinter.CTkButton(master=frame, width=220, text='Register', corner_radius=6,
                                   command=lambda: AddNewAccout(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    btn1.place(x=50, y=300)

    app2.mainloop()


# LoginLayout
def LayoutLogin():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app.geometry("600x400")
    app.title('Login')

    frame = customtkinter.CTkFrame(app, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l1 = customtkinter.CTkLabel(master=frame, text="Login", font=('Century Gothic', 20))
    l1.place(x=138, y=45)

    entry1: CTkEntry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password", show="*")
    entry2.place(x=50, y=165)

    button1 = customtkinter.CTkButton(master=frame, width=220, text='login', corner_radius=6,
                                      command=lambda: LayoutRegister())
    button1.place(x=50, y=240)

    app.mainloop()


LayoutLogin()
