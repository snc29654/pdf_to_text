### インポート
import tkinter
import glob
from tkinter import *
from PIL import ImageTk, Image
import os
import sys
import time
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font
import tkinter.font as tkFont
from chardet import detect 
        
import sys
from pathlib import Path
from subprocess import call

import PyPDF2
# pdf2txt.py のパス



#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.index_before = 0
        self.sizerate=10
        self.n_old=[]
        self.angle=0
        self.filenames =[]
        self.pdf_page=0
        
        
        button1 = Button(root_main, text=u'フォルダー選択', command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=50, y=5) 

        button3= Button(root_main, text=u'ファイル   選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=50, y=30) 

        button4= Button(root_main, text=u'次ページ', command=self.button4_clicked)  
        button4.grid(row=0, column=1)  
        button4.place(x=100, y=55) 

        button5= Button(root_main, text=u'前ページ', command=self.button5_clicked)  
        button5.grid(row=0, column=1)  
        button5.place(x=50, y=55) 


        button8= Button(root_main, text=u'リスト表示削除', command=self.button8_clicked)  
        button8.grid(row=0, column=1)  
        button8.place(x=200, y=5) 

        button9= Button(root_main, text=u'テキスト表示削除', command=self.button9_clicked)  
        button9.grid(row=0, column=1)  
        button9.place(x=200, y=30) 



        #文字色、背景色、サイズ、フォントを指定。
        font1 = font.Font(family='Helvetica', size=12, weight='bold')

        label4 = tkinter.Label(root_main, text="Fontサイズ", fg="red", bg="white", font=font1)
        label4.pack(side="top")
        label4.place(x=200, y=100) 

        label5 = tkinter.Label(root_main, text="PDFページ", fg="red", bg="white", font=font1)
        label5.pack(side="top")
        label5.place(x=200, y=120) 

        self.txt4 = tkinter.Entry(width=10)
        self.txt4.place(x=50, y=120)
        self.txt4.insert(tkinter.END,self.pdf_page)


        self.combo1 = ttk.Combobox(root_main, state='readonly')
        # リストの値を設定
        self.combo1["values"] = (8,9,10,11,12,14,16,18,20)
        # デフォルトの値を食費(index=0)に設定
        self.combo1.current(0)
        # コンボボックスの配置
        self.combo1.place(x=50, y=100)
        #combo1.pack()



    def key_handler(self,e):
    
        print(e.keycode)
        if(e.keycode==38):
            pass
        if(e.keycode==40):
            pass

    def button1_clicked(self):  

        self.font_size=self.combo1.get()
        self.pdf_page=self.txt4.get()

        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        #filenames = []
        self.filenames = glob.glob('*.pdf')
        print(self.filenames)
        self.list_disp()
        #self.quit()

    def button3_clicked(self):  

        self.font_size=self.combo1.get()
        self.pdf_page=self.txt4.get()
        
        #self.sizerate = txt4.get();


        fTyp = [('', '*.pdf')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("All file", ".pdf")], initialdir=iDir)
        print(self.filenames)
        self.list_disp()
        #self.quit()

    def button4_clicked(self):  
        value = tkinter.StringVar()
        
        print("*************")
        print(self.n)
        value.set(self.n)

        self.pdf_page=int(self.pdf_page) + 1
        self.txt4.delete(0, tkinter.END)
        self.txt4.insert(tkinter.END,int(self.pdf_page))

        thread1 = threading.Thread(target=self.select_one_image,args=(self.n,))
        thread1.start()

    def button5_clicked(self):  
        value = tkinter.StringVar()
        
        print("*************")
        print(self.n)
        value.set(self.n)
        if(self.pdf_page > 0):
            self.pdf_page=int(self.pdf_page) - 1

        self.txt4.delete(0, tkinter.END)
        self.txt4.insert(tkinter.END,int(self.pdf_page))

        thread1 = threading.Thread(target=self.select_one_image,args=(self.n,))
        thread1.start()



    def button8_clicked(self):  
        self.listbox.destroy()
    def button9_clicked(self):  
        self.text_box.destroy()

    def quit(self):
        root_main.destroy()

 
    def get_index(self,event):

        value = tkinter.StringVar()

        self.txt4 = tkinter.Entry(width=10)
        self.txt4.place(x=50, y=120)
        self.pdf_page=0
        self.txt4.insert(tkinter.END,self.pdf_page)

 
        index = event.widget.curselection()
        if (self.index_before==index):
            self.angle += 90
        self.index_before=index

        n = event.widget.get(index)
        self.n=n
        self.n_old = n
        value.set(n)
        #self.select_one_image(n)
        print("get_index=" + n)

        thread1 = threading.Thread(target=self.select_one_image,args=(n,))
        thread1.start()

    def list_disp(self):
    
        frame = tkinter.Frame(master=None)
        scrollbar = tkinter.Scrollbar(master=frame, orient="vertical")
        self.listbox = tkinter.Listbox(master=frame,  bg="pink", width=80,height=25, yscrollcommand=scrollbar.set)
        for name in self.filenames:
            self.listbox.insert(tkinter.END, name)
        scrollbar.config(command=self.listbox.yview)
        frame.pack(side=RIGHT, anchor=NW)
        scrollbar.pack(side=tkinter.RIGHT, fill="y")
        self.listbox.pack(side=tk.LEFT)
        self.listbox.bind("<<ListboxSelect>>", self.get_index)




    def select_one_image(self,n):


        #root_one = tkinter.Tk()
        #root_one.title("root_oneです")  
        #root_one.geometry("1x1")
        
        #frame2 = ttk.Frame(root_one, padding=10)
        #frame2.grid()



        self.txt2 = tk.Entry(width=50)
        self.txt2.place(x=20, y=500)


        self.font_size=self.combo1.get()
        #self.pdf_page=self.txt4.get()

 

        self.text_box = tk.Text(bg="#000", fg="#fff", insertbackground="#fff",
                   height=40)
        self.text_box.pack()
        self.text_box.place(x=20, y=200)
        fontExample = tkFont.Font(family="Courier", size=self.font_size, weight="normal", slant="roman")

        self.text_box.configure(font=fontExample)

        #f = open(n, encoding="utf-8")
        #text_data = f.read()

        with open(n, 'rb') as f:  # バイナリファイルとしてファイルをオープン
            b = f.read()  # ファイルの内容を全て読み込む

        enc = detect(b)
    
        try:
        # pdf2txt.py の呼び出し
            pdf_page=self.pdf_page
            while(1):
                with open(n, "rb") as f:
                    reader = PyPDF2.PdfFileReader(f)
                    page = reader.getPage(int(pdf_page))
                    print(page.extractText())
                    self.text_box.insert(END, page.extractText())
                    pdf_page=pdf_page+1

        except:
                self.text_box.insert(END, "ページがありません")
            
            


        #root_one.after(10, lambda: root_one.destroy())
        #root_one.mainloop()


 

    def testend(self):

        self.sub.destroy()
        
        
    

root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("pdf　text変換")  
root_main.geometry("850x600") 



# ボタンの作成（コールバックコマンドには、コンボボックスの値を取得しprintする処理を定義）
#button = tk.Button(text="表示",command=lambda:print(combo.get()))

#button10 = Button(root_main, text=u'エンコードセット', command=button10_clicked)  
#button10.place(x=50, y=50) 



# ボタンの配置
#button.pack()


root_main.mainloop()


#thread1 = threading.Thread(target=c.view_image)
#thread1.start()

    
