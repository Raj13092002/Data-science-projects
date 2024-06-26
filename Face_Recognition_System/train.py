from tkinter import *
from tkinter import ttk #stylist tools
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
#https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b

class Train:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition Sysytem")




                title_lbl=Label(self.root,text="Train Dataset",font=("Rosewood Std Regular",35),bg="White",fg="Dark blue")
                title_lbl.place(x=0,y=0,width=1530,height=65)


                img_top=Image.open(r"college_images\top_img_train.png")
                img_top=img_top.resize((1530,325),Image.LANCZOS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)

                f_lbl=Label(self.root,image=self.photoimg_top)
                f_lbl.place(x=0,y=60,width=1530,height=325)
# ========buttons=========
                b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("Rosewood Std Regular",30),bg="Dark blue",fg="red")
                b1_1.place(x=0,y=380,width=1530,height=70)



                img_bottom=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
                img_bottom=img_bottom.resize((1530,325),Image.LANCZOS)
                self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

                f_lbl=Label(self.root,image=self.photoimg_bottom)
                f_lbl.place(x=0,y=440,width=1530,height=325)



        def train_classifier(self):
                data_dir=("data")
                path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

                faces=[]
                ids=[]


                for image in path:
                        img=Image.open(image).convert("L")   #gray scale images

                        imageNp=np.array(img,'uint8')
                        id=int(os.path.split(image)[1].split(".")[1])

                        faces.append(imageNp)
                        ids.append(id)

                        cv2.imshow("Training",imageNp)
                        cv2.waitKey(1)==13

                ids=np.array(ids)
                # =======Train the classifer======
                clf=cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces,ids)
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Training dataset completed !!")




                
               










if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()