    if self.txtuser.get()=="":
                    messagebox.showerror("Error","Please entre the Email Address for reset password")
                else:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Rajaryan@10",database="face_detection")
                    my_cursor=conn.cursor()
                    query=("select / from register where email=%s")
                    value=(self.txtuser.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    print(row)