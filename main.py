import firebase_admin
from firebase_admin import firestore
import addNewAcout
import loginCliente
import datetime
from tkinter import messagebox
import customtkinter
import tkinter
import secrets
import re
import tkinter as tk
from plyer import notification
from google.cloud import firestore
from customtkinter import CTkEntry
from datetime import datetime
from datetime import date



# get the Firestore client

app = customtkinter.CTk()

def LoginConfirm():
    loginCliente.VerifiInformation()
def center_window(root, width=300, height=200):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates for the Tk root window
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))

    # Set the dimensions and position of the window
    root.geometry(f"{width}x{height}+{x}+{y}")
# pagina de registro
def LayoutRegister():

    app.withdraw()
    app2 = customtkinter.CTk()
    center_window(app2, 600, 400)
    app2.title('Register')
    app2.resizable(False, False)
    app2.iconbitmap('C:/Users/JoaoP/Downloads/Arvore.ico')



    frame = customtkinter.CTkFrame(app2, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l1 = customtkinter.CTkLabel(master=frame, text="Register", font=('Century Gothic', 20))
    l1.place(x=125, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Email")
    entry1.place(x=50, y=105)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
    entry2.place(x=50, y=150)

    entry3 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password", show="*")
    entry3.place(x=50, y=195)

    entry4 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Key")
    entry4.place(x=50, y=240)

    btn1 = customtkinter.CTkButton(master=frame, width=220, text='Register', corner_radius=6,
                                   command=lambda: addNewAcout.AddNewAccout(entry1.get(), entry2.get(), entry3.get(),
                                                                            entry4.get(),app2,app))
    btn1.place(x=50, y=300)

    app2.mainloop()


# LoginLayout
def LayoutLogin():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    center_window(app, 600, 400)
    app.title('Login')
    app.iconbitmap('C:/Users/JoaoP/Downloads/Arvore.ico')
    app.resizable(False, False)

    frame = customtkinter.CTkFrame(app, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l1 = customtkinter.CTkLabel(master=frame, text="Login", font=('Century Gothic', 20))
    l1.place(x=138, y=65)

    entry1: CTkEntry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
    entry1.place(x=50, y=140)
    entry1.focus()

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password", show="*")
    entry2.place(x=50, y=180)

    button1 = customtkinter.CTkButton(master=frame, width=220, text='login', corner_radius=6,
                                      command=lambda: loginCliente.VerifiInformation(entry1.get(),entry2.get(),app))
    button1.place(x=50, y=220)

    button2 = customtkinter.CTkButton(master=frame, width=100, text='Registrar', corner_radius=6,
                                      command=lambda: LayoutRegister())
    button2.place(x=109, y=255)

    app.mainloop()


LayoutLogin()


