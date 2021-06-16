import tkinter as tk
from tkinter import Canvas, filedialog as fd
from tkinter.constants import NONE
from PIL import Image,ImageTk
import cv2 as cv
import numpy as np
#调用库函数

win=tk.Tk()
win.title('实验二')
win.geometry('1024x1024')
#建立窗口
class PictureProcessor():    
    def selectPicture(self):
        pic_name = fd.askopenfilename(title='选择图片', filetypes=[('jpg','png'), ('All Files', '*')])
        return pic_name
    def add_together(self,r_a,r_b):
        image_add=np.add(r_a,r_b)       
        cv.imwrite('add.png',image_add)
        path_add='add.png'
        return path_add
    def subtract_together(self,r_a,r_b):
        image_subtract=np.subtract(r_a,r_b)
        cv.imwrite('subtract.png',image_subtract) 
        path_subtract='subtract.png'
        return path_subtract 
    def multiply_together(self,r_a,r_b):
        image_multiply=np.multiply(r_a,r_b)
        cv.imwrite('multiply.png',image_multiply)
        path_multiply='multiply.png'
        return path_multiply
    def divide_together(self,r_a,r_b):
        image_divide=np.divide(r_a,r_b)
        cv.imwrite('divide.png',image_divide)
        path_divide='divide.png'
        return path_divide      
    #图片处理过程
class PictureProcessorPro(PictureProcessor):
    def update_resized_image(self,image,canvas_width,canvas_height):
        scale = min([1.0 * canvas_width / image.width, 1.0 * canvas_height / image.height])
        image_width = int(image.width * scale)
        image_height = int(image.height * scale)
        scaled = image.resize((image_width, image_height), Image.ANTIALIAS)
        return scaled
        #适应画布大小等比缩放
    def pic_select_a(self): 
        global path_a   
        #若需在方法中调用图片，则需提前声明全局变量
        path_a=self.selectPicture()
        image_a=Image.open(path_a)
        image = ImageTk.PhotoImage(image=self.update_resized_image(image_a,200,200))
        l_a.image = image
        l_a.create_image(100, 100, image=image, anchor=tk.CENTER)
        #选择图片a并显示
    def pic_select_b(self): 
        global path_b
        path_b=self.selectPicture()    
        image_b=Image.open(path_b)
        image = ImageTk.PhotoImage(image=self.update_resized_image(image_b,200,200))
        l_b.image = image
        l_b.create_image(100, 100, image=image, anchor=tk.CENTER)
        #选择图片b并显示
    def pic_add(self):
        r_a=cv.imread(path_a)
        r_b=cv.imread(path_b)
        image_add=Image.open(self.add_together(r_a,r_b))
        image = ImageTk.PhotoImage(image=self.update_resized_image(image_add,200,200))
        l_add.image = image
        l_add.create_image(100, 100, image=image, anchor=tk.CENTER)
        #图片相加并显示
    def pic_subtract(self):
        r_a=cv.imread(path_a)
        r_b=cv.imread(path_b)
        image_subtract=Image.open(self.subtract_together(r_a,r_b))
        image = ImageTk.PhotoImage(image=self.update_resized_image(image_subtract,200,200))
        l_subtract.image = image
        l_subtract.create_image(100, 100, image=image, anchor=tk.CENTER)
        #图片相减并显示
    def pic_multiply(self):
        r_a=cv.imread(path_a)
        r_b=cv.imread(path_b)
        image_multiply=Image.open(self.multiply_together(r_a,r_b))
        image = ImageTk.PhotoImage(image=self.update_resized_image(image_multiply,200,200))
        l_multiply.image = image
        l_multiply.create_image(100, 100, image=image, anchor=tk.CENTER)
        #图片相乘并显示
    def pic_divide(self):
        r_a=cv.imread(path_a)
        r_b=cv.imread(path_b)
        image_divide=Image.open(self.divide_together(r_a,r_b))
        image = ImageTk.PhotoImage(image=self.update_resized_image(image_divide,200,200))
        l_divide.image = image
        l_divide.create_image(100, 100, image=image, anchor=tk.CENTER)
        #图片相除并显示
class Frame():
    def frame(self):
        global l_a,l_b,l_add,l_subtract,l_multiply,l_divide
        canvas_width=200
        canvas_height=200

        l_a=Canvas(win,width=canvas_width,height=canvas_height,bg='white')
        l_a.grid(row=2,column=1,padx=20, pady=20)

        l_b=Canvas(win,width=canvas_width,height=canvas_height,bg='white')
        l_b.grid(row=2,column=2,padx=20, pady=20)

        l_add=Canvas(win,width=canvas_width,height=canvas_height,bg='white')
        l_add.grid(row=4,column=1,padx=20, pady=20)

        l_subtract=Canvas(win,width=canvas_width,height=canvas_height,bg='white')
        l_subtract.grid(row=4,column=2,padx=20, pady=20)

        l_multiply=Canvas(win,width=canvas_width,height=canvas_height,bg='white')
        l_multiply.grid(row=4,column=3,padx=20, pady=20)

        l_divide=Canvas(win,width=canvas_width,height=canvas_height,bg='white')
        l_divide.grid(row=4,column=4,padx=20, pady=20)
        #图片显示布局
        picture=PictureProcessorPro()
        botton1=tk.Button(win,text='选择图片a',width=10,height=2,command=picture.pic_select_a)
        botton1.grid(row=1,column=1)

        botton2=tk.Button(win,text='选择图片b',width=10,height=2,command=picture.pic_select_b)
        botton2.grid(row=1,column=2)

        botton3=tk.Button(win,text='图片相加',width=10,height=2,command=picture.pic_add)
        botton3.grid(row=3,column=1)

        botton4=tk.Button(win,text='图片相减',width=10,height=2,command=picture.pic_subtract)
        botton4.grid(row=3,column=2)

        botton5=tk.Button(win,text='图片相乘',width=10,height=2,command=picture.pic_multiply)
        botton5.grid(row=3,column=3)

        botton6=tk.Button(win,text='图片相除',width=10,height=2,command=picture.pic_divide)
        botton6.grid(row=3,column=4)
        #按钮布局

def main():
    frame1=Frame()
    frame1.frame()
    #调用frame方法完成布局    
    win.mainloop()
if __name__ == '__main__':
    main()