import tkinter
from tkinter import messagebox
from tkinter.constants import END
import base64

def encode(key,clear):
    enc=[]
    for i in range(len(clear)):
        key_c=key[i%len(key)]
        enc_c=chr((ord(clear[i])+ord(key_c)) %256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key,enc):
    dec=[]
    enc=base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c=key[i%len(key)]
        dec_c=chr((256+ord(enc[i]) - ord(key_c))%256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrpt_notes():
    title=title_lablentry.get()
    message= secret_text.get("1.0",END)
    master_secret=master_lablentry.get()

    if len(title)==0 or len(message)==0 or len(master_secret)==0:
        messagebox.showwarning(title="Error!",message="Please enter all info.")
    else:
        message_encrpyted=encode(master_secret,message)

        try:
            with open("my_secret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrpyted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrpyted}")
        finally:
            title_lablentry.delete(0,END)
            master_lablentry.delete(0,END)
            secret_text.delete("1.0",END)

def decrypt_notes():
    message_encrypted=secret_text.get("1.0",END)
    master_secret=master_lablentry.get()

    if len(message_encrypted)==0 or len(master_secret)==0:
        messagebox.showwarning(title="Error!",message="Please enter all info.")
    else:
        try:
            decrypted_message=decode(master_secret,message_encrypted)
            secret_text.delete("1.0",END)
            secret_text.insert("1.0",decrypted_message)
        except:
            messagebox.showwarning(title="Error",message="Please enter encrypted text!")


secret_window=tkinter.Tk()
secret_window.title("Secret Notes")
secret_window.minsize(width=450,height=900)

#photo
photo= tkinter.PhotoImage(file="pngimg.com - eagle_PNG1227.png")
photo_canvas= tkinter.Canvas(height=200,width=200)
photo_canvas.create_image(250,250,image=photo)
photo_canvas.pack()

#title_lable

title_lable= tkinter.Label(text="Enter your title")
title_lable.pack()

title_lablentry= tkinter.Entry(width=20)
title_lablentry.pack()

#secret_lable

secret_lable=tkinter.Label(text="Enter your secret")
secret_lable.pack()

secret_text= tkinter.Text(width=20,height=20)
secret_text.pack()

#master_lable

master_lable=tkinter.Label(text="Enter master key")
master_lable.pack()

master_lablentry=tkinter.Entry(width=20)
master_lablentry.pack()


#button save
save_button=tkinter.Button(text="Save & Encrypt",command=save_and_encrpt_notes)
save_button.pack()


#button decrypt

decrypt_button=tkinter.Button(text="Decrypt",command=decrypt_notes)
decrypt_button.pack()


secret_window.mainloop()





