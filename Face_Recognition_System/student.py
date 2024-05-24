from tkinter import *
from tkinter import ttk #stylist tools
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition Sysytem")

                # =====variables===
                self.var_dep=StringVar()
                self.var_cource=StringVar()
                self.var_year=StringVar()
                self.var_semester=StringVar()
                self.var_std_id=StringVar()
                self.var_std_name=StringVar()
                self.var_div=StringVar()
                self.var_roll=StringVar()
                self.var_gender=StringVar()
                self.var_dob=StringVar()
                self.var_email=StringVar()
                self.var_phone=StringVar()
                self.var_address=StringVar()
                self.var_teacher=StringVar()
                


        #first
                img=Image.open(r"D:\final year projects\college_images\student_upper_1.jpg")
                img=img.resize((500,130),Image.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=500,height=130)
        #2nd img
                img_1=Image.open(r"D:\final year projects\college_images\student_upper_2.jpg")
                img_1=img_1.resize((500,130),Image.LANCZOS)
                self.photoimg_1=ImageTk.PhotoImage(img_1)

                f_lbl=Label(self.root,image=self.photoimg_1)
                f_lbl.place(x=500,y=0,width=500,height=130)

        #3rd img
                img_2=Image.open(r"D:\final year projects\college_images\student_upper_3.jpg")
                img_2=img_2.resize((500,130),Image.LANCZOS)
                self.photoimg_2=ImageTk.PhotoImage(img_2)

                f_lbl=Label(self.root,image=self.photoimg_2)
                f_lbl.place(x=1000,y=0,width=550,height=130)
        #bg_img
                img3=Image.open(r"D:\final year projects\college_images\bg_img.jpg")
                img3=img3.resize((1530,710),Image.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=130,width=1530,height=710)


                #label
                title_lbl=Label(bg_img,text="Student Management System",font=("Rosewood Std Regular",35),bg="light blue",fg="Dark blue")
                title_lbl.place(x=0,y=0,width=1530,height=45)


                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=0,y=46,width=1530,height=650)


                #left site
                left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",16))
                left_frame.place(x=10,y=10,width=740,height=580)

                img_left=Image.open(r"D:\final year projects\college_images\left_label..webp")
                img_left=img_left.resize((720,130),Image.LANCZOS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=720,height=100)
                #current cource
                current_cource_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Cource Information",font=("times new roman",11))
                current_cource_frame.place(x=5,y=132,width=720,height=125)
        #Department
                dep_label=Label(current_cource_frame,text="Department",font=("times new roman",11))
                dep_label.grid(row=0,column=0,padx=10,sticky=W)

                dep_combo=ttk.Combobox(current_cource_frame,textvariable=self.var_dep,font=("times new roman",11),state="readonly",width=17)
                dep_combo["values"]=("Select Department","BCA","BCA-IT","BBA","B.com")
                dep_combo.current(0)
                dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Cource
                cource_label=Label(current_cource_frame,text="Cource",font=("times new roman",11))
                cource_label.grid(row=0,column=2,padx=10,sticky=W)

                cource_combo=ttk.Combobox(current_cource_frame,textvariable=self.var_cource,font=("times new roman",11),state="readonly",width=17)
                cource_combo["values"]=("Select Cource","Cloud Computing","Data Science","Tally","financial management","CNN","Ethicial hacking")
                cource_combo.current(0)
                cource_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        #Year
                Year_label=Label(current_cource_frame,text="Year",font=("times new roman",11))
                Year_label.grid(row=1,column=0,padx=10,sticky=W)

                Year_combo=ttk.Combobox(current_cource_frame,textvariable=self.var_year,font=("times new roman",11),state="readonly",width=17)
                Year_combo["values"]=("Select Year","2021-2024","2022-2025","2023-2026","2024-2027")
                Year_combo.current(0)
                Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #Semester
                Semester_label=Label(current_cource_frame,text="Semester",font=("times new roman",11))
                Semester_label.grid(row=1,column=2,padx=10,sticky=W)

                Semester_combo=ttk.Combobox(current_cource_frame,textvariable=self.var_semester,font=("times new roman",11),state="readonly",width=17)
                Semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6")
                Semester_combo.current(0)
                Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        #class student information 
                class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",11))
                class_student_frame.place(x=5,y=260,width=720,height=290)
        #student id
                Student_id_label=Label(class_student_frame,text="Student ID:",font=("times new roman",11))
                Student_id_label.grid(row=0,column=0,padx=10,sticky=W)

                Student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",11))
                Student_id_entry.grid(row=0,column=1,padx=10,sticky=W)
        #student name
                Student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",11))
                Student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

                Student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",11))
                Student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #class division
                class_div_label=Label(class_student_frame,text="Class division:",font=("times new roman",11))
                class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

                # Studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",11))
                # Studentid_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
                div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",11),state="readonly",width=15)
                div_combo["values"]=("Select Gender","A","B","C","D")
                div_combo.current(0)
                div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
                rollno_label=Label(class_student_frame,text="Roll NO:",font=("times new roman",11))
                rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

                rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",11))
                rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #Gender
                Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",11))
                Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

                # Gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",11))
                # Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
                gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",11),state="readonly",width=15)
                gender_combo["values"]=("Select Gender","Male","other","Female",)
                gender_combo.current(0)
                gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
                Dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",11))
                Dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

                Dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",11))
                Dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #Email
                Email_label=Label(class_student_frame,text="Email:",font=("times new roman",11))
                Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

                Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",11))
                Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #Phone no
                Phoneno_label=Label(class_student_frame,text="Phone no:",font=("times new roman",11))
                Phoneno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

                Phoneno_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",11))
                Phoneno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #Address
                Address_label=Label(class_student_frame,text="Address:",font=("times new roman",11))
                Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

                Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",11))
                Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        #Teacher_name
                Teacher_name_label=Label(class_student_frame,text="Teacher_name:",font=("times new roman",11))
                Teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

                Teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",11))
                Teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        #radio buttons
                self.var_radio1=StringVar()
                radiobt1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
                radiobt1.grid(row=6,column=0)
                self.var_radio2=StringVar()
                radiobt2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
                radiobt2.grid(row=6,column=1)

        #buttons frame
                btn_frame=Frame(class_student_frame,bd=2,relief=RAISED,bg="white")
                btn_frame.place(x=0,y=190,width=715,height=35)

                Update_btn=Button(btn_frame,text="Update",command=self.update_data,width=21,font=("times new roman",11),bg="Blue",fg="white")
                Update_btn.grid(row=0,column=1)

                delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=21,font=("times new roman",11),bg="Blue",fg="white")
                delete_btn.grid(row=0,column=2)

                save_btn=Button(btn_frame,text="Save",command=self.add_data,width=21,font=("times new roman",11),bg="Blue",fg="white")
                save_btn.grid(row=0,column=0)

                reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=21,font=("times new roman",11),bg="Blue",fg="white")
                reset_btn.grid(row=0,column=3)
        #button2 frame
                btn1_frame=Frame(class_student_frame,bd=2,relief=RAISED,bg="white")
                btn1_frame.place(x=0,y=225,width=715,height=35)

                Take_photo_sample_btn=Button(btn1_frame,command=self.generate_dataset,text="Take_photo_sample",width=43,font=("times new roman",11),bg="Blue",fg="white")
                Take_photo_sample_btn.grid(row=0,column=0)

                update_photo_sample_btn=Button(btn1_frame,text="update_photo_sample",width=43,font=("times new roman",11),bg="Blue",fg="white")
                update_photo_sample_btn.grid(row=0,column=1)





                #right site
                right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",11))
                right_frame.place(x=760,y=10,width=660,height=580)

                img_right=Image.open(r"D:\final year projects\college_images\right_frame.jpeg")
                img_right=img_right.resize((720,130),Image.LANCZOS)
                self.photoimg_right=ImageTk.PhotoImage(img_right)

                f_lbl=Label(right_frame,image=self.photoimg_right)
                f_lbl.place(x=5,y=0,width=720,height=100)
        # =====search system=====

                Serach_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",11))
                Serach_frame.place(x=5,y=135,width=650,height=70)

                Search_label=Label(Serach_frame,text="Search:",font=("times new roman",11),bg="red",fg="white")
                Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

                Search_combo=ttk.Combobox(Serach_frame,font=("times new roman",11),state="readonly",width=15)
                Search_combo["values"]=("Select","dep","cource","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo")
                Search_combo.current(0)
                Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

                Search_entry=ttk.Entry(Serach_frame,width=20,font=("times new roman",11))
                Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

                Search_btn=Button(Serach_frame,text="Search",width=14,font=("times new roman",11),bg="Blue",fg="white")
                Search_btn.grid(row=0,column=3,padx=4)

                Show_all_btn=Button(Serach_frame,text="Show_all",width=14,font=("times new roman",11),bg="Blue",fg="white")
                Show_all_btn.grid(row=0,column=4,padx=4)

                # ===table frame===
                Table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
                Table_frame.place(x=5,y=210,width=650,height=350)

                scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

                self.student_table=ttk.Treeview(Table_frame,columns=("dep","cource","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("dep",text="Department")
                self.student_table.heading("cource",text="Cource")
                self.student_table.heading("year",text="Year")
                self.student_table.heading("sem",text="Semester")
                self.student_table.heading("id",text="StudentID")
                self.student_table.heading("name",text="Name")
                self.student_table.heading("div",text="Division")
                self.student_table.heading("roll",text="Roll")
                self.student_table.heading("gender",text="Gender")
                self.student_table.heading("dob",text="DOB")
                self.student_table.heading("email",text="Email")
                self.student_table.heading("phone",text="Phone")
                self.student_table.heading("address",text="Address")
                self.student_table.heading("teacher",text="Teacher")
                self.student_table.heading("photo",text="photoSampleStatus")
                
                
                self.student_table["show"]="headings"

                self.student_table.column("dep",width=100)
                self.student_table.column("cource",width=100)
                self.student_table.column("year",width=100)
                self.student_table.column("sem",width=100)
                self.student_table.column("id",width=100)
                self.student_table.column("name",width=100)
                self.student_table.column("div",width=100)
                self.student_table.column("roll",width=100)
                self.student_table.column("gender",width=100)
                self.student_table.column("dob",width=100)
                self.student_table.column("email",width=100)
                self.student_table.column("phone",width=100)
                self.student_table.column("address",width=100)
                self.student_table.column("teacher",width=100)
                self.student_table.column("photo",width=100)
                
                

                

                self.student_table.pack(fill=BOTH,expand=1)
                self.student_table.bind("<ButtonRelease>",self.get_cursor)
                self.fetch_data()

        
        # ========function decleraation=====
        def add_data(self):
                if (self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()==""):
                        messagebox.showerror("Error","All field are required",parent=self.root)
                else:

                        try:
                                conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
                                my_cursor=conn.cursor()
                                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_cource.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_id.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get()
                                                                ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Sucess","Student details has been added sucessfully",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to : {str(es)} ",parent=self.root)
# =========fetch data base======
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                data=my_cursor.fetchall()


                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("",END,values=i)
                        conn.commit()
                conn.close()
# ===== get cursor=====
        def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus()
                content=self.student_table.item(cursor_focus)
                data=content["values"]

                self.var_dep.set(data[0]),
                self.var_cource.set(data[1]),
                self.var_year.set(data[2]),
                self.var_semester.set(data[3]),
                self.var_std_id.set(data[4]),
                self.var_std_name.set(data[5]),
                self.var_div.set(data[6]),
                self.var_roll.set(data[7]),
                self.var_gender.set(data[8]),
                self.var_dob.set(data[9]),
                self.var_email.set(data[10]),
                self.var_phone.set(data[11]),
                self.var_address.set(data[12]),
                self.var_teacher.set(data[13]),                                                                         
                self.var_radio1.set(data[14])
                

# ===update function===
        def update_data(self):
                if (self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()==""):
                        messagebox.showerror("Error","All field are required",parent=self.root)
                else:
                        try:
                                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                                if Update>0:
                                        conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
                                        my_cursor=conn.cursor()
                                        my_cursor.execute("Update student set dep=%s,cource=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_cource.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get()
 
                                        ))
                                else:
                                        if not Update:
                                                return
                                messagebox.showinfo("Sucess","student details sucessfully updated completely",parent=self.root)
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                        except Exception as es:
                                messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)
# ===== delete====
        def delete_data(self):
                if self.var_std_id.get()=="":
                        messagebox.showerror("Error","Student id must be required",parent=self.root)
                else:
                        try:
                                delete=messagebox.askyesno("Student delete page","do you want to delete this student",parent=self.root)
                                if delete>0:
                                        conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
                                        my_cursor=conn.cursor()
                                        sql="delete from student where Student_id=%s"
                                        val=(self.var_std_id.get(),)
                                        my_cursor.execute(sql,val)
                                else:
                                        if not delete:
                                                return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("delete","Sucessfully deleted",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)
# =======reset====
        def reset_data(self):
                self.var_dep.set("Select Department"),
                self.var_std_name.set(""),
                self.var_roll.set(""),
                self.var_div.set("select division"),
                self.var_semester.set("select semester"),
                self.var_year.set("selet year"),
                self.var_std_id.set(""),

                self.var_gender.set("select gender"),
                self.var_dob.set(""),
                self.var_email.set(""),
                self.var_phone.set(""),
                self.var_address.set(""),
                self.var_teacher.set(""),
                                                                                                                        
                self.var_radio1.set(""),
                self.var_cource.set("select Cource")   
# ======Generate dataset=====take a samples====
        def generate_dataset(self):
                if (self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()==""):
                        messagebox.showerror("Error","All field are required",parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
                                my_cursor=conn.cursor()
                                my_cursor.execute("select * from student")
                                myresult=my_cursor.fetchall()
                                id=0
                                for x in myresult:
                                        id+=1
                                my_cursor.execute("Update student set dep=%s,cource=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_cource.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),

                                                                                                                        self.var_gender.get(),

                                                                                                                        self.var_dob.get(),

                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get()==id+1,
 
                                        ))
                                conn.commit()
                                self.fetch_data()
                                self.reset_data()
                                conn.close()
                        

                                # =====Load predefine data of ffrontal from open cv====
                                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                                def face_cropped(img):
                                        
                                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                                        #scaling factor=1.3
                                        #minimum neighbour=5

                                        for (x,y,w,h) in faces:
                                                face_cropped=img[y:y+h,x:x+w]
                                                return face_cropped
                                cap=cv2.VideoCapture(0)
                                img_id=0
                                while True:
                                        ret,my_frame=cap.read()
                                        if face_cropped(my_frame) is not None:
                                                img_id+=1
                                                face=cv2.resize(face_cropped(my_frame),(450,450))
                                                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                                file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                                cv2.imwrite(file_name_path,face)
                                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                                cv2.imshow("Crooped Face",face)

                                        if cv2.waitKey(1)==13 or int(img_id)==100:
                                                break
                                
                                cap.release()
                                cv2.destroyAllWindows()

                                messagebox.showinfo("Result","Generating data sets completed sucessfully !!!")
                        except Exception as es:
                                messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)





                        

                           










if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()