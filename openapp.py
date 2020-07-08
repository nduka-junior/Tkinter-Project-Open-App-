import tkinter as tk
from tkinter import filedialog,messagebox
import subprocess
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('700x600+300+80')
root.iconbitmap('app.ico')

def Open():
   global photo
   
   filename = filedialog.askopenfilename(
      initialdir="Pictures", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"),("png files", "*.png")))
   query_search.delete(0, tk.END)
   query_search.insert(0, filename)
   try:
      photo = ImageTk.PhotoImage(Image.open(filename).resize((200, 200)))
      photoimage = tk.Label(root, image=photo)
      photoimage.grid(row=2, column=0, sticky='w', padx=40)
   except:
      messagebox.showerror('App Manager','Unable to view file')
   try:
      subprocess.call(filename, shell=True)
   except:
      messagebox.showerror('App Manager','Unable to such open file')
   return filename


header = tk.Label(root, text='App Manager', font=("Roboto", "25",))
header.grid(row=0, column=0, sticky='nesw', pady=30)

searchframe = tk.Frame(root, width=100, height=80,)
searchframe.grid(row=1, column=0, padx=20, pady=40)

query_search = tk.Entry(master=searchframe, font=("Roboto", "15",), width=50)
query_search.grid(row=0, column=0, sticky='nesw',)

query_search_button = tk.Button(
    master=searchframe, text='Open App', font=("Helvetica", "12"), command=Open)
query_search_button.grid(row=0, column=1, sticky='nesw', padx=10)

root.mainloop()
