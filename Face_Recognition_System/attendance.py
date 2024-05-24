from tkinter import *
from tkinter import ttk #stylist tools
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]


class Attendence:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition Sysytem")

                # =====variables===
                self.var_atten_id=StringVar()
                self.var_atten_roll=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_attendance=StringVar()

                #first
                img=Image.open(r"college_images\attendence_first.jpeg")
                img=img.resize((800,300),Image.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=800,height=300)
        #2nd img
                img_1=Image.open(r"college_images\attendence_second.webp")
                img_1=img_1.resize((800,300),Image.LANCZOS)
                self.photoimg_1=ImageTk.PhotoImage(img_1)

                f_lbl=Label(self.root,image=self.photoimg_1)
                f_lbl.place(x=800,y=0,width=800,height=300)

                #bg_img
                img3=Image.open(r"college_images\bg_img.jpg")
                img3=img3.resize((1540,710),Image.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=300,width=1540,height=710)

                #label
                title_lbl=Label(bg_img,text="Attendence Management System",font=("Rosewood Std Regular",35),bg="light blue",fg="Dark blue")
                title_lbl.place(x=0,y=0,width=1530,height=45)

                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=0,y=46,width=1530,height=650)

                #left site
                left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence  Details",font=("times new roman",16))
                left_frame.place(x=10,y=10,width=740,height=580)

                img_left=Image.open(r"college_images\right_frame.jpeg")
                img_left=img_left.resize((720,130),Image.LANCZOS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=720,height=100)

                left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
                left_inside_frame.place(x=1,y=100,width=720,height=370)

                # labeland_entry

                #attendence id
                AttendenceId_label=Label(left_inside_frame,text="AttendenceId:",font=("times new roman",13))
                AttendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

                AttendenceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13))
                AttendenceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

                #roll
                rollLabel=Label(left_inside_frame,text="Roll:",font=("times new roman",13))
                rollLabel.grid(row=0,column=2,padx=4,pady=8)

                atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13))
                atten_roll.grid(row=0,column=3,pady=8)

                #name
                nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",13))
                nameLabel.grid(row=1,column=0)

                atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13))
                atten_name.grid(row=1,column=1,pady=8)

                #department
                deplabel=Label(left_inside_frame,text="Department:",font=("times new roman",13))
                deplabel.grid(row=1,column=2)

                atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13))
                atten_dep.grid(row=1,column=3,pady=8)

                #time
                timelabel=Label(left_inside_frame,text="Time:",font=("times new roman",13))
                timelabel.grid(row=2,column=0)

                atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13))
                atten_time.grid(row=2,column=1,pady=8)

                #date
                datelabel=Label(left_inside_frame,text="Date:",font=("times new roman",13))
                datelabel.grid(row=2,column=2)

                atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13))
                atten_date.grid(row=2,column=3,pady=8)

                #attendence status
                attendancelabel=Label(left_inside_frame,text="Attendence status:",font=("times new roman",13))
                attendancelabel.grid(row=3,column=0)

                self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",13),state="readonly")
                self.atten_status["values"]=("Status","Present","Absent")
                self.atten_status.grid(row=3,column=1,pady=8)
                self.atten_status.current(0)

                #buttons frame
                btn_frame=Frame(left_inside_frame,bd=2,relief=RAISED,bg="white")
                btn_frame.place(x=0,y=250,width=715,height=35)

                Update_btn=Button(btn_frame,text="Update",width=21,font=("times new roman",11),bg="Blue",fg="white")
                Update_btn.grid(row=0,column=1)

                delete_btn=Button(btn_frame,text="Import CSV",width=21,command=self.importCSV,font=("times new roman",11),bg="Blue",fg="white")
                delete_btn.grid(row=0,column=2)

                save_btn=Button(btn_frame,text="Export CSV",width=21,command=self.exportCSV,font=("times new roman",11),bg="Blue",fg="white")
                save_btn.grid(row=0,column=0)

                reset_btn=Button(btn_frame,text="reset",width=21,command=self.reset_data,font=("times new roman",11),bg="Blue",fg="white")
                reset_btn.grid(row=0,column=3)






                #right site
                right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",16))
                right_frame.place(x=760,y=10,width=720,height=580)

                table_frame=Frame(right_frame,bd=2,relief=RAISED,bg="white")
                table_frame.place(x=5,y=5,width=700,height=380)


                # ======scorll bar====

                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.AttendenceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.AttendenceReportTable.xview)
                scroll_y.config(command=self.AttendenceReportTable.yview)

                self.AttendenceReportTable.heading("id",text="Attendence Id")
                self.AttendenceReportTable.heading("roll",text="Roll")
                self.AttendenceReportTable.heading("name",text="Name")
                self.AttendenceReportTable.heading("department",text="Department")
                self.AttendenceReportTable.heading("time",text="time")
                self.AttendenceReportTable.heading("date",text="date")
                self.AttendenceReportTable.heading("attendence",text="attendence")

                self.AttendenceReportTable["show"]="headings"
                self.AttendenceReportTable.column("id",width=100)
                self.AttendenceReportTable.column("roll",width=100)
                self.AttendenceReportTable.column("name",width=100)
                self.AttendenceReportTable.column("department",width=100)
                self.AttendenceReportTable.column("time",width=100)
                self.AttendenceReportTable.column("date",width=100)
                self.AttendenceReportTable.column("attendence",width=100)


                self.AttendenceReportTable.pack(fill=BOTH,expand=1)
                self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)


                # ====function   fetch data=====
        def fetchData(self,rows):
                self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
                for i in rows:
                        self.AttendenceReportTable.insert("",END,values=i)
                # ====import csv===
        def importCSV(self):
                global mydata
                mydata.clear()
                fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL FILES","*.*")),parent=self.root)
                with open(fln) as myfile:
                        csvread=csv.reader(myfile,delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fetchData(mydata)

# ==== export csv====

        def exportCSV(self):
                try:
                        if len(mydata)<1:
                                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                                return False
                        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL FILES","*.*")),parent=self.root)
                        with open(fln,mode="w",newline="") as myfile:
                                exp_write=csv.writer(myfile,delimiter=",")
                                for i in mydata:
                                        exp_write.writerow(i)
                                messagebox.showinfo("Data Export","Your Data exported to  "+os.path.basename(fln)+"  sucessfully")
                except Exception as es:
                                messagebox.showerror("Error",f"Due to : {str(es)} ",parent=self.root)
        

        # ==== get cursor===

        def get_cursor(self,event=""):
                cursor_row=self.AttendenceReportTable.focus()
                content=self.AttendenceReportTable.item(cursor_row)
                rows=content["values"]
                if len(rows) >= 7:
                        self.var_atten_id.set(rows[0])
                        self.var_atten_roll.set(rows[1])
                        self.var_atten_name.set(rows[2])
                        self.var_atten_dep.set(rows[3])
                        self.var_atten_time.set(rows[4])
                        self.var_atten_date.set(rows[5])
                        self.var_atten_attendance.set(rows[6])
                else:
                        print("Error: Not enough data in the selected row")

        def reset_data(self):
                self.var_atten_id.set("")
                self.var_atten_roll.set("")
                self.var_atten_name.set("")
                self.var_atten_dep.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_attendance.set("")


                



                






if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()