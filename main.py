from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


app = tk.Tk()
app.title("Watermarking")
app.geometry("700x700")

app_font=('times', 18, 'bold')

l1=tk.Label(app,text="Watermark photo",width=30,font=app_font)
l1.pack()

canvas=tk.Canvas(app, width=500,height=500)
canvas.pack()

b1=tk.Button(app,text="Upload File", width=20,command=lambda:upload_file())
b1.pack()

b2=tk.Button(app, text="Quit", width=20, command=lambda:quit())
b2.pack()

def upload_file():
    messagebox.showinfo(title="Warning",
                        message="Images biger than 500x500 will be resized")

    file = filedialog.askopenfilename()
    image = Image.open(file)
    image = image.resize((500,500), Image.ADAPTIVE)
    img = ImageTk.PhotoImage(image)
    canvas.img = img
    canvas.create_image(0,0, image=img, anchor=NW)
    

def quit():
    app.quit()

app.mainloop()