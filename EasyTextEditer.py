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
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO





encode_type="utf-8"

#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.index_before = 0
        self.sizerate=10
        self.n_old=[]
        self.angle=0
        self.filenames =[]
        

        button3= Button(root_main, text=u'ファイル   選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=100, y=30) 






    def button3_clicked(self):  
        global encode_type
        
        #self.sizerate = txt4.get();


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("PDF", ".pdf")], initialdir=iDir)
        print(self.filenames)
        
        root = Tk()
        root.title('Text 1')
        root.minsize(100, 100)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

# Frame
        frame1 = ttk.Frame(root, padding=10)
        frame1.rowconfigure(1, weight=1)
        frame1.columnconfigure(0, weight=1)
        frame1.grid(sticky=(N, W, S, E))
        
        

        for name in self.filenames:
    

            pdf = open(name, 'rb')

        # テキスト抽出のための準備
            outpdf = StringIO()
            rmgr = PDFResourceManager()
            lprms = LAParams()
            device = TextConverter(rmgr, outpdf, laparams=lprms)
            iprtr = PDFPageInterpreter(rmgr, device)

        # ページを読み込む




# Text
            f = Font(family='Helvetica', size=16)
            v1 = StringVar()
            txt = Text(frame1, height=30, width=120)
            txt.configure(font=f)
            txt.grid(row=1, column=0, sticky=(N, W, S, E))

            for page in PDFPage.get_pages(pdf):
                iprtr.process_page(page)

        # テキストを抽出して出力
                text = outpdf.getvalue()
                print(text)
                txt.insert(END, text)



# Scrollbar
            scrollbar = ttk.Scrollbar(
                frame1,
                orient=VERTICAL,
                command=txt.yview)
            txt['yscrollcommand'] = scrollbar.set
            scrollbar.grid(row=1, column=1, sticky=(N, S))

    def quit(self):
        root_main.destroy()

 



    def textwrite(self):
        get_data=self.text_box.get("1.0", "end")
        print(get_data)
        
        for name in self.filenames:

            out_file=name
            fout_utf = open(out_file, 'w', encoding=self.encode_type)
 
            for row in get_data:
                fout_utf.write(row)
 
        fout_utf.close()



root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("600x300") 







root_main.mainloop()


    
