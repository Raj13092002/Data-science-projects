from tkinter import *
from tkinter import ttk #stylist tools
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("face Recognition Sysytem")


            title_lbl=Label(self.root,text="DEVELOPER",font=("Rosewood Std Regular",35),bg="White",fg="Dark blue")
            title_lbl.place(x=0,y=0,width=1530,height=65)


            img_top=Image.open(r"college_images\dev.jpg")
            img_top=img_top.resize((1530,720),Image.LANCZOS)
            self.photoimg_top=ImageTk.PhotoImage(img_top)

            f_lbl=Label(self.root,image=self.photoimg_top)
            f_lbl.place(x=0,y=60,width=1530,height=720)
# Frame
            main_frame=Frame(f_lbl,bd=2,bg="light Blue")
            main_frame.place(x=1000,y=0,width=500,height=600)

            img_top1=Image.open(r"college_images\raj.jpg")
            img_top1=img_top1.resize((200,200),Image.LANCZOS)
            self.photoimg_top1=ImageTk.PhotoImage(img_top1)

            f_lbl=Label(main_frame,image=self.photoimg_top1)
            f_lbl.place(x=300,y=0,width=200,height=200)
#Developer info
            dev_label=Label(main_frame,text="Hello My name is Raj Aryan",font=("times new roman",19),bg="white",fg="blue")
            dev_label.place(x=0,y=5)
            dev_label=Label(main_frame,text="I am from BCA-Aku",font=("times new roman",19),bg="white",fg="blue")
            dev_label.place(x=0,y=45)
            dev_label=Label(main_frame,text="ID-13057",font=("times new roman",19),bg="white",fg="blue")
            dev_label.place(x=0,y=85)

            dev_label=Label(main_frame,text="I am junior ML Engineer",font=("times new roman",19),bg="white",fg="blue")
            dev_label.place(x=0,y=125)


            img_2=Image.open(r"D:\final year projects\college_images\ML.jpeg")
            img_2=img_2.resize((500,400),Image.LANCZOS)
            self.photoimg_2=ImageTk.PhotoImage(img_2)

            f_lbl=Label(main_frame,image=self.photoimg_2)
            f_lbl.place(x=0,y=200,width=500,height=400)





if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()