'''
 @author : Keshav Kabra
'''
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as tmsg
from tkinter import ttk
from tkinter import font
import Help
import os
import datetime

# ------------------------------------ Main Window -------------------------------------- #
def ask():
    new_file()
    root.destroy()

root = Tk()
root.title("Untitled - NoteBook")
root.geometry("800x650")
root.wm_iconbitmap("2.ico")

root.protocol('WM_DELETE_WINDOW', ask)
# --------------------------------------------------------------------------------------- #

# ---------------------------- Text-Area and Scrollbar ---------------------------------- #
fr = Frame(root)
text = Text(fr, font="Calibri 20", undo=True, bg="misty rose", wrap='word')
text.pack(expand=True, fill=BOTH)

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

fr.pack(expand=True, fill=BOTH)
# --------------------------------------------------------------------------------------- #

# --------------------------------- Driver Functions ------------------------------------ #
def choose_font():
    t = Toplevel()
    t.title("Font")
    t.geometry("275x110")
    t.wm_iconbitmap('4.ico')
    t.attributes("-toolwindow",1)

    font_selected = StringVar()
    size_selected = StringVar()
    # for choosing fonts
    combo_font = ttk.Combobox(t, width=15, textvariable=font_selected)
    combo_font.set("Calibri") #default
    Label(t, text='Font Name : ').grid(row=0, column=0, sticky='nw')
    combo_font['values'] = sorted(font.families())
    combo_font.grid(row=2, column=0)
    # for choosing size of font
    combo_size = ttk.Combobox(t, width=15, textvariable=size_selected)
    combo_size.set("20") #default
    Label(t, text='Size : ').grid(row=0, column=8, sticky='nw')
    combo_size['values'] = list(range(8,80,4))
    combo_size.grid(row=2, column=8)
    # apply and Cancel buttons
    apply = Button(t, text="Apply",
                   command=lambda : text.config(font=(font_selected.get(),size_selected.get())))
    apply.grid(row=5, column=5, pady=4)
    done = Button(t, text='Cancel', command=t.destroy)
    done.grid(row=9, column=5)


def new_file():
    if len(text.get('1.0', END)) > 0:
        if tmsg.askyesno("NoteBook", "Do you want to save current file ?"):
            save_file()
        else:
            text.delete('1.0', END)
            root.title("Untitled - NoteBook")

def open_file():
    try:
        new_file()
        file = filedialog.askopenfile(parent=root, title="select a file", filetypes=(("Text File","*.txt"),
                                                                                     ("All Files", "*.*")))
        root.title(os.path.basename(file.name) + " - NoteBook")
        if file != None:
            contents = file.read()
            text.insert('1.0', contents)
            file.close()
    except:
        pass

def save_file():
    try:
        file = filedialog.asksaveasfile(initialfile="Untitled.txt", mode='w',
                        defaultextension=".txt",filetypes=[("All Files","*.*"),
                                                    ("Text Documents","*.txt")])
        root.title(os.path.basename(file.name) + " - NoteBook")
        if file != None:
            contents = text.get('1.0', END)
            file.write(contents)
            file.close()
    except:
        pass

def signature():
    text.insert(END, "\n\t- Keshav Kabra")

def undo():
    text.event_generate(("<<Undo>>"))
def redo():
    text.event_generate(("<<Redo>>"))
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def delete():
    text.event_generate(("<<Clear>>"))
def select_all():
    text.event_generate(("<<SelectAll>>"))
def date_time():
    text.insert(END, datetime.datetime.now().strftime('%I:%M %p') + "  " +
                datetime.datetime.now().strftime('%d-%m-%Y'))
def day_month():
    text.insert(END, datetime.datetime.now().strftime('%A  %B'))

# --------------------------------------------------------------------------------------- #

# -------------------------------------- Menu Options ----------------------------------- #
main_menu = Menu(root)

m1 = Menu(main_menu, tearoff=0)
m1.add_command(label="New File", command=new_file)
m1.add_command(label="Open", command=open_file)
m1.add_command(label="Save", command=save_file)
m1.add_separator()
m1.add_command(label = "Signature", command=signature)
m1.add_separator()
m1.add_command(label="Exit", command=lambda : Help.exit(root))
main_menu.add_cascade(label="File", menu=m1)

m2 = Menu(main_menu, tearoff=0)
m2.add_command(label="Undo", command=undo)
m2.add_command(label="Redo", command=redo)
m2.add_separator()
m2.add_command(label="Cut", command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_command(label="Paste", command=paste)
m2.add_command(label="Delete", command=delete)
m2.add_separator()
m2.add_command(label="Select All", command=select_all)
m2.add_command(label="Time/ Date", command=date_time)
m2.add_command(label="Day/ Month", command=day_month)
main_menu.add_cascade(label="Edit", menu=m2)

m3 = Menu(main_menu, tearoff=0)
m3.add_command(label="Font...", command=choose_font)
main_menu.add_cascade(label="Format", menu=m3)

m4 = Menu(main_menu, tearoff=0)
m4.add_command(label="About Us", command=Help.about_us)
m4.add_separator()
m4.add_command(label="Actions", command=Help.actions)
main_menu.add_cascade(label="Help", menu=m4)

root.config(menu=main_menu)
# --------------------------------------------------------------------------------------- #

root.mainloop()