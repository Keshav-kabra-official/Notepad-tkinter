'''
 @author : Keshav Kabra
'''

import tkinter.messagebox as tmsg

def about_us():
    tmsg.showinfo(
        "About",
        "This Software is made with by KESHAV KABRA.\n\n"
        "Contact Info :\n"
        "      Phone No. : +91-7014722936\n"
        "      Email Info  : keshavkabra118@gmail.com\n"
        "                       keshavkabra.official@gmail.com\n"
        "      INDIA \n\n"
        " If you have any Issues, please tell your Feedback."
    )

def actions():
    tmsg.showinfo(
        "About Software",
        "- This is a Text-Editor and Saver Software.\n"
        "- One can write the text and save it from here.\n"
        "- Some other handy functions are provided on the menu bar.\n"
    )

def exit(root):
    val = tmsg.askyesno("NoteBook", "Do you want to Exit ?")
    if val>0:
        tmsg.showinfo("NoteBook", " Thank You! Hope you liked the Service !!")
        root.destroy()