import tkinter as tk
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from RSA import *
from utility import *

class GUIDecriptor(tk.Tk):
    def __init__(roo):
        super().__init__()
        def GUITQRVerif():
            
            def selecttextfile():
                filename = filedialog.askopenfile(mode='r', filetypes=[('Text files', 'txt')])
                if filename is not None:
                    content = filename.read()
                    entry_cipher.delete(0, len(entry_cipher.get()))
                    entry_cipher.insert(0, content)
                    cipher.set(content)

            def selectpubkey():
                content = openPublicKeyFile()
                if content is not None:
                    entry_pubkey.delete(0, len(entry_pubkey.get()))
                    entry_pubkey.insert(0, content)
                    pubkey.set(content) 
                                    
            def dekripsi():
                if len(pubkey.get()) == 0:
                    messagebox.showerror("Error", "Public Key is empty")
                elif len(cipher.get()) == 0:
                    messagebox.showerror("Error", "Cipher text is empty")
                else:
                    print("cipher: ",cipher.get())
                    print("pubkey: ",pubkey.get())
               
                    stringkey = str(pubkey.get())
                    real_key = stringtokey(stringkey)
                    
                    pla = decrypt(real_key, int(cipher.get()))
                    print("pla: ",pla)
                    plaintext = num2str(pla)
                    entry_plain2.delete(0, len(entry_plain2.get()))
                    entry_plain2.insert(0, plaintext)
                    plain2.set(plaintext)
                    
                    print("plain2: ",plain2.get())
                    print("plain2 type: ", type(cipher.get()))
                    print("plaintext type: ", type(plaintext))
            
            roo.geometry("600x400")
            roo.title("Decrypt QR Code")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            text = Label(roo, text="Pendeksripsian Ciphertext QR Code\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)

            # variabel
            pubkey = StringVar()
            plain = StringVar()
            plain2 = StringVar()
            cipher = StringVar()

            
            #kolom ciphertext
            label_cipher = Label(roo, text="Ciphertext", font=("Arial", 12), bg = "#FBE6BF")
            label_cipher.place(x=40, y=50)
            entry_cipher = Entry(roo, textvariable=cipher, width=40)
            entry_cipher.place(x=200, y=50)
            
            button_file = Button(roo, text="Buka Ciphertext", command=selecttextfile)
            button_file.place(x=500, y=50)
            
            #kolom public key
            label_pubkey = Label(roo, text="PublicKey", font=("Arial", 12), bg = "#FBE6BF")
            label_pubkey.place(x=40, y=90)
            entry_pubkey = Entry(roo, textvariable=pubkey, width=40)
            entry_pubkey.place(x=200, y=90)
            button_pubkey = Button(roo, text="Browse", command=selectpubkey)
            button_pubkey.place(x=500, y=90)              
            
            #dekripsi text
            button_dek = Button(roo, text="Dekripsi", command=dekripsi)
            button_dek.place(x=200, y=130)
                   
            #kolom hasil dekripsi plaintext
            label_plain2 = Label(roo, text="Hasil Dekripsi", font=("Arial", 12), bg = "#FBE6BF")
            label_plain2.place(x=40, y=170)
            entry_plain2 = Entry(roo, textvariable=plain2, width=40)
            entry_plain2.place(x=200, y=170)

            #exit
            button = Button(roo, text="Keluar", font=("Arial", 10, "bold"), command = lambda: roo.destroy())
            button.place(x=500, y=250)

        GUITQRVerif()