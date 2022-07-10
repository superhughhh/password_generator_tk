
from random import randint
from secrets import choice
import string
from tkinter import *
import tkinter


def generate_password():
    password_min = 8
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(choice(all_chars) for x in range(randint(password_min,password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
        
        
        


#creer la fenetre
window = Tk()
window.title("Password generator")
window.geometry("720x480")
window.iconphoto(False, tkinter.PhotoImage(file="logo.png"))
window.config(background="#000000")

#creation de la frame principale
frame = Frame(window, bg="#000000")

#creation de l'image(canva)
width = 250
height = 250
img = PhotoImage(file="img.png").zoom(15).subsample(30)
canvas = Canvas(frame, width=width, height=height, bg="#000000", highlightthickness=0, bd=0)#les 2 derniers parametre permettent d'enlever la bordure autour de l'image
canvas.create_image(width/2, height/2, image=img)
canvas.grid(row=0, column=0, sticky=W, padx=40)

#creation d'une sous-boite
right_frame = Frame(frame, bg="#000000" )

#creation du titre
label_title = Label(right_frame, text="PASSWORD", font=("Helvetica", 20), bg="#000000", fg="white")
label_title.pack()

#creation du input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg="#000000", fg="white")
password_entry.pack()

#creation du BOUTON
generate_password_button = Button(right_frame, text="GENERATE", font=("Helvetica", 20), highlightbackground='white', fg="#000000", command=generate_password)
generate_password_button.pack(fill=X)

#on place la sous-boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

#affichage de la frame
frame.pack(expand=YES)

#affichage de l'app
window.mainloop()