from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont


app = tk.Tk()
app.title("Watermarking")
app.geometry("300x150")

app_font=('times', 18, 'bold')

l1=tk.Label(app,text="Watermark photo",width=30,font=app_font)
l1.pack()

b1=tk.Button(app,text="Upload and Watermark File", width=20,command=lambda:upload_file())
b1.pack()

b3=tk.Button(app, text="Quit", width=20, command=lambda:quit())
b3.pack()

def upload_file():
    messagebox.showinfo(title="Warning",
                        message="Watermarked img will be saved in same folder as py file")
    file = filedialog.askopenfilename()
    image = Image.open(file)
    name = image.filename
    filename = name.split("/")[(len(name.split("/"))-1)].split(".")
    width, height = image.size
    
    drawing = ImageDraw.Draw(image)
    font = ImageFont.truetype("./font/Freedom-10eM.ttf", (width/6-height/6))
    fill_color = (203,201,201)
    watermark_text = "MAGNES"
    x = width/2 - 50
    y = height/2 - 50
    position = (x, y)
    drawing.text(xy = position, text = watermark_text, font = font, fill = fill_color)
    image.save(f'{filename[0]}_watermarked.jpg')    

def quit():
    app.quit()

app.mainloop()