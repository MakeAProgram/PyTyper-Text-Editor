from tkinter import *
from tkinter import filedialog

filename = None

def newFile():
    global filename
    filename = "Kein Titel"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = filedialog.asksaveasfile(mode='w')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Diese Datei kann nicht gespeichert werden...")

def openFile():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("PyTexter 2020")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Neue Datei", command=newFile)
filemenu.add_command(label="Datei Öffnen", command=openFile)
filemenu.add_command(label="Datei Speichern", command=saveFile)
filemenu.add_command(label="Datei Speichern unter", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=root.quit)
menubar.add_cascade(label="Datei", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
