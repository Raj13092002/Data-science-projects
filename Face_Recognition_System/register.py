from tkinter import *
from tkinter import ttk #stylist tools
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

    # =====variables==
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

#bg_img
        img3=Image.open(r"D:\final year projects\college_images\bg_img.jpg")
        #img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_bg=Label(self.root,image=self.photoimg3)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
#left side
        img=Image.open(r"D:\final year projects\college_images\left_side_register.jpg")
        #img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_left=Label(self.root,image=self.photoimg)
        lbl_left.place(x=50,y=100,width=470,height=550)

#frame
        frame=Frame(self.root,bd=2,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

#label
        title_lbl=Label(frame,text="Register New User",font=("Rosewood Std Regular",20,"bold"),bg="White",fg="Dark blue")
        title_lbl.place(x=20,y=20)
#lable entry
        fname_lbl=Label(frame,text="First name",font=("Rosewood Std Regular",15,"bold"),bg="White")
        fname_lbl.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Rosewood Std Regular",15,"bold"))
        self.fname_entry.place(x=50,y=132,width=250)

        lname_lbl=Label(frame,text="Last name",font=("Rosewood Std Regular",15,"bold"),bg="White")
        lname_lbl.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Rosewood Std Regular",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        contact_lbl=Label(frame,text="Contact no",font=("Rosewood Std Regular",15,"bold"),bg="White")
        contact_lbl.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("Rosewood Std Regular",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email_lbl=Label(frame,text="Email",font=("Rosewood Std Regular",15,"bold"),bg="White")
        email_lbl.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Rosewood Std Regular",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        security_q_lbl=Label(frame,text="Select Security Questions",font=("Rosewood Std Regular",15,"bold"),bg="White")
        security_q_lbl.place(x=50,y=240)

        self.security_q_combo=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",11),state="readonly")
        self.security_q_combo["values"]=("Select","your birth place","Your girlfriend","your petname")
        self.security_q_combo.current(0)
        self.security_q_combo.place(x=50,y=270,width=250)

        sequerity_A_lbl=Label(frame,text="Security Answer",font=("Rosewood Std Regular",15,"bold"),bg="White")
        sequerity_A_lbl.place(x=370,y=240)

        self.txt_sequerity_A=ttk.Entry(frame,textvariable=self.var_security_A,font=("Rosewood Std Regular",15,"bold"))
        self.txt_sequerity_A.place(x=370,y=270,width=250)

        pswd_lbl=Label(frame,text="Password",font=("Rosewood Std Regular",15,"bold"),bg="White")
        pswd_lbl.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Rosewood Std Regular",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        cmfpsed_lbl=Label(frame,text="Confirm Password",font=("Rosewood Std Regular",15,"bold"),bg="White")
        cmfpsed_lbl.place(x=370,y=310)

        self.txt_cmfpsed=ttk.Entry(frame,textvariable=self.var_confpass,font=("Rosewood Std Regular",15,"bold"))
        self.txt_cmfpsed.place(x=370,y=340,width=250)
# =====checkbutton===

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the term and conditions",font=("Rosewood Std Regular",15,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)
        # ===button===

        img_btn=Image.open(r"D:\final year projects\college_images\register-now-button1.jpg")
        img_btn=img_btn.resize((200,50),Image.LANCZOS)
        self.photoimg_btn=ImageTk.PhotoImage(img_btn)
        b1=Button(frame,image=self.photoimg_btn,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=20,y=420,width=200)

        login_btn=Image.open(r"D:\final year projects\college_images\loginpng.png")
        login_btn=login_btn.resize((200,50),Image.LANCZOS)
        self.photologin_btn=ImageTk.PhotoImage(login_btn)
        b2=Button(frame,image=self.photologin_btn,borderwidth=0,cursor="hand2")
        b2.place(x=400,y=420,width=200)


# ====function decleartion=====
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select":
                messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password and confirm Password must be same")

        elif self.var_check.get()==0:
                messagebox.showerror("Error","please agree our terms and condition")
        else:
                conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                        messagebox.showerror("Error","User already Exist Please try another email")
                else:
                        my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_security_Q.get(),
                                                                                                self.var_security_A.get(),
                                                                                                self.var_pass.get()
                                                                                                
                                                                                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucess","Register sucessfully",parent=self.root)
        
                                




        


        




if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
