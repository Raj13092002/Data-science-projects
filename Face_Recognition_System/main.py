from tkinter import *
import tkinter.messagebox
from tkinter import ttk #stylist tools
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student import Student

import os

from train import Train
from face_recognition import Face_Recognition

from attendance import Attendence

from developer import Developer

from help import Help


class Face_Recognition_System:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition Sysytem")
        #first
                img=Image.open(r"college_images\upper_1.jpg")
                img=img.resize((500,130),Image.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=500,height=130)
        #2nd img
                img_1=Image.open(r"college_images\upper_2.jpeg")
                img_1=img_1.resize((500,130),Image.LANCZOS)
                self.photoimg_1=ImageTk.PhotoImage(img_1)

                f_lbl=Label(self.root,image=self.photoimg_1)
                f_lbl.place(x=500,y=0,width=500,height=130)

        #3rd img
                img_2=Image.open(r"college_images\upper_3.jpeg")
                img_2=img_2.resize((500,130),Image.LANCZOS)
                self.photoimg_2=ImageTk.PhotoImage(img_2)

                f_lbl=Label(self.root,image=self.photoimg_2)
                f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg_img
                img3=Image.open(r"college_images\bg_img.jpg")
                img3=img3.resize((1530,710),Image.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=130,width=1530,height=710)


                #label
                title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("Rosewood Std Regular",35),bg="light blue",fg="red")
                title_lbl.place(x=0,y=0,width=1530,height=45)
                # =====time====
                def time():
                        string=strftime('%H:%M:%S %p')
                        lbl.config(text=string)
                        lbl.after(1000,time)

                lbl=Label(title_lbl,font=("Rosewood Std Regular",15),background='white',foreground='blue')
                lbl.place(x=0,y=0,width=110,height=50)
                time()
        #student
                img4=Image.open(r"college_images\student.png")
                img4=img4.resize((220,220),Image.LANCZOS)
                self.photoimg4=ImageTk.PhotoImage(img4)


                b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
                b1.place(x=200,y=100,width=220,height=220)

                b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("Rosewood Std Regular",15),bg="light blue",fg="red")
                b1_1.place(x=200,y=300,width=220,height=40)
        #detect face
                img5=Image.open(r"college_images\face detcore.webp")
                img5=img5.resize((220,220),Image.LANCZOS)
                self.photoimg5=ImageTk.PhotoImage(img5)


                b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.Face_data)
                b1.place(x=500,y=100,width=220,height=220)

                b1_1=Button(bg_img,text="Face detector",command=self.Face_data,cursor="hand2",font=("Rosewood Std Regular",15),bg="light blue",fg="red")
                b1_1.place(x=500,y=300,width=220,height=40)

        #attendence 
                img6=Image.open(r"college_images\attendence.png")
                img6=img6.resize((220,220),Image.LANCZOS)
                self.photoimg6=ImageTk.PhotoImage(img6)


                b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
                b1.place(x=800,y=100,width=220,height=220)

                b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_data,font=("Rosewood Std Regular",15),bg="light blue",fg="red")
                b1_1.place(x=800,y=300,width=220,height=40)

        #help 
                img7=Image.open(r"college_images\chat.jpg")
                img7=img7.resize((220,220),Image.LANCZOS)
                self.photoimg7=ImageTk.PhotoImage(img7)


                b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
                b1.place(x=1100,y=100,width=220,height=220)

                b1_1=Button(bg_img,text="Help",command=self.help_data,cursor="hand2",font=("Rosewood Std Regular",15),bg="light blue",fg="red")
                b1_1.place(x=1100,y=300,width=220,height=40)


        #train
                img8=Image.open(r"college_images\train.png")
                img8=img8.resize((220,220),Image.LANCZOS)
                self.photoimg8=ImageTk.PhotoImage(img8)


                b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.Train_data)
                b1.place(x=200,y=400,width=220,height=220)

                b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.Train_data,font=("Rosewood Std Regular",15),bg="light blue",fg="red")
                b1_1.place(x=200,y=600,width=220,height=40)
        #photos
                img9=Image.open(r"college_images\photos.jpeg")
                img9=img9.resize((220,220),Image.LANCZOS)
                self.photoimg9=ImageTk.PhotoImage(img9)


                b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
                b1.place(x=500,y=400,width=220,height=220)

                b1_1=Button(bg_img,text="photos",cursor="hand2",command=self.open_img,font=("Rosewood Std Regular",15),bg="light blue",fg="red")
                b1_1.place(x=500,y=600,width=220,height=40)

        #developer 
                img10=Image.open(r"college_images\developer.png")
                img10=img10.resize((220,220),Image.LANCZOS)
                self.photoimg10=ImageTk.PhotoImage(img10)


                b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
                b1.place(x=800,y=400,width=220,height=220)

                b1_1=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("Rosewood Std Regular",15),bg="light blue",fg="red")
                b1_1.place(x=800,y=600,width=220,height=40)

        #exit 
                img11=Image.open(r"college_images\exit.jpg")
                img11=img11.resize((220,220),Image.LANCZOS)
                self.photoimg11=ImageTk.PhotoImage(img11)


                b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
                b1.place(x=1100,y=400,width=220,height=220)

                b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("Rosewood Std Regular",15),bg="light blue",fg="red")
                b1_1.place(x=1100,y=600,width=220,height=40)
        def open_img(self):
                os.startfile("data")       

        def iExit(self):
                self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit from this project",parent=self.root)
                if self.iExit >0:
                        self.root.destroy()
                else:
                        return


# ===functions buttons===
        def student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Student(self.new_window)
                
        def Train_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Train(self.new_window)
        def Face_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)

        
        def attendence_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Attendence(self.new_window)
        
        def developer_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Developer(self.new_window)
        def help_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Help(self.new_window)

        




        



        











if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()