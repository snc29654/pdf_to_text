from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO




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

# Button
button1 = ttk.Button(
    frame1, text='OK',
    command=lambda: print('%s' % txt.get(1.0, END)))
button1.grid(
    row=0, column=0, columnspan=2, sticky=(N, E))





        # PDFを読み込む
filename = "sample.pdf"
pdf = open(filename, 'rb')

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
txt = Text(frame1, height=15, width=70)
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

root.mainloop()