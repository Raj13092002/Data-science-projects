from tkinter import *
from tkinter import ttk #stylist tools
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


from main import Face_Recognition_System

def main_login():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition Sysytem")

 #bg_img
        img3=Image.open(r"D:\final year projects\college_images\bg_img.jpg")
        #img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_bg=Label(self.root,image=self.photoimg3)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(lbl_bg,bd=2,bg="Black")
        frame.place(x=610,y=170,width=340,height=450)

        img_1=Image.open(r"D:\final year projects\college_images\LoginIconAppl.png")
        img_1=img_1.resize((100,100),Image.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lblimg1=Label(image=self.photoimg_1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        get_str=Label(frame,text="Get Started",font=("Rosewood Std Regular",18),bg="Black",fg="White")
        get_str.place(x=95,y=100)

        # labels


        username=lbl=Label(frame,text="UserName",font=("Rosewood Std Regular",14),bg="Black",fg="White")
        username.place(x=110,y=155)

        self.txtuser=ttk.Entry(frame,font=("Rosewood Std Regular",18))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("Rosewood Std Regular",14),bg="Black",fg="White")
        password.place(x=110,y=225)

        self.txtpass=ttk.Entry(frame,font=("Rosewood Std Regular",18),show="*")
        self.txtpass.place(x=40,y=250,width=270)


        # ====icon images===
        img_2=Image.open(r"D:\final year projects\college_images\LoginIconAppl.png")
        img_2=img_2.resize((25,25),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lblimg2=Label(image=self.photoimg_2,bg="black",borderwidth=0)
        lblimg2.place(x=690,y=325,width=25,height=25)

        img_3=Image.open(r"D:\final year projects\college_images\lock-512.png")
        img_3=img_3.resize((25,25),Image.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lblimg2=Label(image=self.photoimg_3,bg="black",borderwidth=0)
        lblimg2.place(x=690,y=397,width=25,height=25)
# ===buttons===
        Login_btn=Button(frame,text="Login",command=self.login,width=21,font=("times new roman",18),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        Login_btn.place(x=110,y=300,width=120,height=35)
    
    # ===register button==

        register_btn=Button(frame,text="New User",command=self.register_window,width=10,font=("times new roman",12),borderwidth=0,bg="Black",fg="white",activeforeground="white",activebackground="red")
        register_btn.place(x=5,y=350,width=110)

        forgot_password_btn=Button(frame,text="Forget",command=self.forgot_password_window,width=12,font=("times new roman",12),borderwidth=0,bg="Black",fg="white",activeforeground="white",activebackground="red")
        forgot_password_btn.place(x=5,y=390,width=110)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field Required")
        elif self.txtuser.get()=="raj" and self.txtpass.get()=="aryan":
            messagebox.showinfo("Sucess","Welcome to Raj_aryan project")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNO","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit() 
            conn.close()

    # =====reset paswword window=====
    def reset_pass(self):
        if self.security_Q_combo.get()=="Select":
            messagebox.showerror("Error","Select the secrity questions")
        elif self.txt_sequerity_A.get()=="":
            messagebox.showerror("Error","Please entre the answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please entre the new password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txtuser.get(),self.security_Q_combo.get(),self.txt_sequerity_A.get(),)
            my_cursor.execute(qury,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please entre correct answer")
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password is Sucessfully Change",parent=self.root2)
                self.root2.destroy()




            # =====Forgot password window===
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please entre the Email Address for reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My error","please entre the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)

                security_Q_lbl=Label(self.root2,text="Select Security Questions",font=("Rosewood Std Regular",15,"bold"),bg="White")
                security_Q_lbl.place(x=50,y=80)

                self.security_Q_combo=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly")
                self.security_Q_combo["values"]=("Select","your birth place","Your Age","your petname")
                self.security_Q_combo.current(0)
                self.security_Q_combo.place(x=50,y=110,width=250)

                sequerity_A_lbl=Label(self.root2,text="Security Answer",font=("Rosewood Std Regular",15,"bold"),bg="White")
                sequerity_A_lbl.place(x=50,y=150)

                self.txt_sequerity_A=ttk.Entry(self.root2,font=("Rosewood Std Regular",15,"bold"))
                self.txt_sequerity_A.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text="New Password",font=("Rosewood Std Regular",15,"bold"),bg="white",fg="black")
                new_pass.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("Rosewood Std Regular",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("Rosewood Std Regular",15,"bold"),fg="white",bg="green")
                btn.place(x=130,y=300)






            

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

        security_Q_lbl=Label(frame,text="Select Security Questions",font=("Rosewood Std Regular",15,"bold"),bg="White")
        security_Q_lbl.place(x=50,y=240)

        self.security_Q_combo=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",11),state="readonly")
        self.security_Q_combo["values"]=("Select","your birth place","Your age","your petname")
        self.security_Q_combo.current(0)
        self.security_Q_combo.place(x=50,y=270,width=250)

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
    main_login()


