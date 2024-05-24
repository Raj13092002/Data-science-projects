from tkinter import *
from tkinter import ttk #stylist tools
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("face Recognition Sysytem")


            title_lbl=Label(self.root,text="Help Desk",font=("Rosewood Std Regular",35),bg="White",fg="Dark blue")
            title_lbl.place(x=0,y=0,width=1530,height=65)


            img_top=Image.open(r"college_images\help_desk.jpg")
            img_top=img_top.resize((1530,720),Image.LANCZOS)
            self.photoimg_top=ImageTk.PhotoImage(img_top)

            f_lbl=Label(self.root,image=self.photoimg_top)
            f_lbl.place(x=0,y=60,width=1530,height=720)

            dev_label=Label(f_lbl,text="Email: Rajaryan13092002@gmail.com",font=("times new roman",19),bg="white",fg="blue")
            dev_label.place(x=1130,y=5)
            



if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()