import tkinter as tk
import string
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *

import GUIKeyGenerator as GUIKey
import GUIDecriptor as GUIDecript
import GUIQRGenerator as GUIQR

class Main(tk.Tk):
    def __init__(root):
        super().__init__()
        
        #canvas
        root.geometry("790x400")
        root.title("Safe Ticket")
        root.configure(bg = "#FBE6BF")

        canvas = Canvas(
            root,
            bg = "#FBE6BF",
            height = 600,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        canvas.create_text(
            220,
            30,
            anchor="nw",
            text="Program Safe Ticket",
            fill="#000000",
            font=("OpenSansRoman Bold", 40 * -1)
        )

        canvas.create_text(
            230,
            100,
            anchor="nw",
            text="QR Code Ticketing with RSA Encription",
            fill="#000000",
            font=("OpenSansRoman Regular", 20 * -1)
        )
        
        canvas.create_text(
            250,
            370,
            anchor="nw",
            text="Tugas Makalah Kriptografi ©2023 Michel Vito Adinugroho",
            fill="#000000",
            font=("OpenSansRoman Regular", 12 * -1)
        )
            
        #button
        button_image_1 = PhotoImage(
            file = "img/Key.png")
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [GUIKey.GUIKeyGenerator()],
            bg = "#FBE6BF",
            relief="flat"
        )
        button_1.place(
            x=25.0,
            y=250.0,
            width=125,
            height=55
        )
        button_image_2 = PhotoImage(
            file = "img/QR Generator.png")
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [GUIQR.GUIQRGenerator()],
            bg = "#FBE6BF",
            relief="flat"
        )
        button_2.place(
            x=225,
            y=250,
            width=125,
            height=55
        )
        button_image_3 = PhotoImage(
            file = "img/Decryptor.png")
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [GUIDecript.GUIDecriptor()],
            bg = "#FBE6BF",
            relief="flat"
        )
        button_3.place(
            x=425,
            y=250,
            width=125,
            height=55
        )
        button_image_4 = PhotoImage(
            file = "img/Exit.png")
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: root.destroy(),
            bg = "#FBE6BF",
            relief="flat"
        )
        button_4.place(
            x=625,
            y=250,
            width=125,
            height=55
        )
                        
        
        root.resizable(False, False)
        root.mainloop()
        
if __name__ == "__main__":
    Main()
    