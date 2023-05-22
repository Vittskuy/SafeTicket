import tkinter as tk
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from tkinter import messagebox
from RSA import *
from utility import *
import qrcode

#membuat GUI dari frame, label, dan tombol
class GUIQRGenerator(tk.Tk):
    def __init__(roo):
        super().__init__()
        def GUIQRGen():
                       
            def selecttextfile():
                filename = filedialog.askopenfile(mode='r', filetypes=[('Text files', 'txt')])
                if filename is not None:
                    content = filename.read()
                    entry_plain.delete(0, len(entry_plain.get()))
                    entry_plain.insert(0, content)
                    plain.set(content)
                                    
            def selectprivkey():
                content = openPrivateKeyFile()
                if content is not None:
                    entry_privkey.delete(0, len(entry_privkey.get()))
                    entry_privkey.insert(0, content)
                    privkey.set(content)

            def enkripsi():
                if len(privkey.get()) == 0:
                    messagebox.showerror("Error", "Private Key is empty")
                elif len(plain.get()) == 0:
                    messagebox.showerror("Error", "Plain text is empty")
                else:
                    print("plain: ",plain.get())
 
                    print("privkey: ",privkey.get())

                    
                    stringkey = str(privkey.get())
                    real_key = stringtokey(stringkey)
                    
                    chi = encrypt(real_key, str2num(plain.get()))
                    entry_cipher.delete(0, len(entry_cipher.get()))
                    entry_cipher.insert(0, chi)
                    cipher.set(chi)
                    
                    print("cipher: ",cipher.get())
                    print("cipher type: ", type(cipher.get()))
                    print("chi type: ", type(chi))
            
            def makeqr():
                myQR = qrcode.make(cipher.get())
                print(type(myQR))
                myQR.save("image_QR.png")
            
            roo.geometry("600x400")
            roo.title("Generate Encripted QR Code")
            roo.resizable(0, 0)
            roo.configure(bg = "#FBE6BF")
            text = Label(roo, text="Pembangkitan QR Code hasil enkripsi identitas\n", font=("Arial", 12, "bold"), bg = "#FBE6BF")
            text.place(x=40, y=10)

            # variabel
            privkey = StringVar()
            plain = StringVar()
            cipher = StringVar()

            #kolom identitas
            label_plain = Label(roo, text="Identitas", font=("Arial", 12), bg = "#FBE6BF")
            label_plain.place(x=40, y=50)
            entry_plain = Entry(roo, textvariable=plain, width=40)
            entry_plain.place(x=200, y=50)

            button_file = Button(roo, text="Save Identitas", command=selecttextfile)
            button_file.place(x=500, y=50)
            
            #kolom private key
            label_privkey = Label(roo, text="Private Key", font=("Arial", 12), bg = "#FBE6BF")
            label_privkey.place(x=40, y=80)
            entry_privkey = Entry(roo, textvariable=privkey, width=40)
            entry_privkey.place(x=200, y=80)
            button_privkey = Button(roo, text="Browse", command=selectprivkey)
            button_privkey.place(x=500, y=80)
            
            #enkripsi text
            button_enk = Button(roo, text="Enkripsi", command=enkripsi)
            button_enk.place(x=200, y=120)
            
            #kolom hasil enkripsi plaintext
            label_cipher = Label(roo, text="Ciphertext", font=("Arial", 12), bg = "#FBE6BF")
            label_cipher.place(x=40, y=160)
            entry_cipher = Entry(roo, textvariable=cipher, width=40)
            entry_cipher.place(x=200, y=160)
            
            #button make QR Code
            button_qr = Button(roo, text="Buat QR Code", command=makeqr)
            button_qr.place(x=200, y=200)

            #exit
            button = Button(roo, text="Keluar", font=("Arial", 10, "bold"), command = lambda: roo.destroy())
            button.place(x=500, y=300)
        GUIQRGen()
        
