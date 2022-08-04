# install pillow,pypdf,pypdfium2,pytesseract
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import os
import PyPDF2
import pypdfium2 as pdfium
import PIL.Image
from pytesseract import pytesseract
from tkinter import *

te=Tk()
te.title("Text Extractor")
te.geometry('500x500')
te.resizable(0,0)
te.config(bg="#081923",highlightcolor='white', highlightthickness=5)

frame=LabelFrame(te,width=450,height=450,text='TEXT EXTRACTOR',bg='#087587',font=("Times New Roman",28,"bold"),highlightcolor='white', highlightthickness=3)
frame.place(x=20,y=20)
message=Label(frame,width=46,font=("Times New Roman",12,"bold"),text='Welcome to Text Extractor Tool...\nThe Text extractor will allow you to extract text from any\nPDF  /  IMAGE  /  WEBSITE\nYou may upload any document(.pdf,.png) or Site address \nand the tool will pull text from the image \nand will save it in a text file :)',highlightcolor='black')
message.place(x=11,y=35)
browse=Button(frame,text='CLICK TO SELECT PDF',font=("Segoe Script",10,"bold"),width=25,height=1,bd=2,fg='white',bg='black',activebackground='pink',highlightbackground='black', highlightcolor='white', highlightthickness=3,cursor='hand2',command=lambda: open_pdf())
browse.place(x=95,y=180)
browse=Button(frame,text='CLICK TO SELECT IMAGE',font=("Segoe Script",10,"bold"),width=25,height=1,bd=2,fg='white',bg='black',activebackground='pink',highlightbackground='black', highlightcolor='white', highlightthickness=3,cursor='hand2',command=lambda: open_image())
browse.place(x=95,y=240)
browse=Button(frame,text='CLICK TO SELECT WEBSITE',font=("Segoe Script",10,"bold"),width=25,height=1,bd=2,fg='white',bg='black',activebackground='pink',highlightbackground='black', highlightcolor='white', highlightthickness=3,cursor='hand2',command=lambda: open_site())
browse.place(x=95,y=300)
def open_pdf():
    file = askopenfile(parent=te, mode='rb', filetype=[("Pdf file", "*.pdf")])
    readpdf=PyPDF2.PdfFileReader(file)
    pdf = pdfium.PdfDocument(file)
    fileinfo=PyPDF2.PdfFileReader.getDocumentInfo(readpdf)

    title = fileinfo.title
    number_of_pages = len(pdf)

    def extract_file():
        text = ""
        for i in range(extp):
            page = pdf.get_page(i)
            textpage = page.get_textpage()
            text += textpage.get_text()
            text += "\n"
            [g.close() for g in (textpage, page)]
        pdf.close()
        with open(f"{title}.txt","w",encoding='utf-8') as f:
            f.write(text)
        text_file=(f"{title}.txt")
        messagebox.showinfo('INFO',f'Your File has been saved at location: {os.path.abspath(text_file)}') 

    op=Tk()
    op.title("PDF Text Extractor")
    op.geometry('500x500')
    op.resizable(0,0)
    op.config(bg="#081923",highlightcolor='white', highlightthickness=5)

    frame1=LabelFrame(op,width=450,height=230,text='DETAILS!!!',bg='#087587',font=("Times New Roman",25,"bold"),highlightcolor='white', highlightthickness=3)
    frame1.place(x=20,y=20)

    label_title=Label(frame1,text='Title',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_title.place(x=30,y=20)
    entry_title=Label(frame1,text='NOT AVAILABLE',width=30,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2,justify='left')
    entry_title.configure(text=fileinfo.title)
    entry_title.place(x=190,y=20)

    label_author=Label(frame1,text='Author',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_author.place(x=30,y=50)
    entry_author=Label(frame1,text='NOT AVAILABLE',width=30,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    entry_author.configure(text=fileinfo.author)
    entry_author.place(x=190,y=50)

    label_creator=Label(frame1,text='Creator',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_creator.place(x=30,y=80)
    entry_creator=Label(frame1,text='NOT AVAILABLE',width=30,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    entry_creator.configure(text=fileinfo.creator)
    entry_creator.place(x=190,y=80)

    label_producer=Label(frame1,text='Producer',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_producer.place(x=30,y=110)
    entry_producer=Label(frame1,text='NOT AVAILABLE',width=30,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    entry_producer.configure(text=fileinfo.producer)
    entry_producer.place(x=190,y=110)

    label_nop=Label(frame1,text='Number of pages',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_nop.place(x=30,y=140)
    display_nop=Label(frame1,text=number_of_pages,width=30,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    display_nop.place(x=190,y=140)


    frame2=LabelFrame(op,width=450,height=210,text='Extract Text',bg='#087587',font=("Times New Roman",25,"bold"),highlightcolor='white', highlightthickness=3)
    frame2.place(x=20,y=260)

    label_nop=Label(frame2,text='No. of pages',font=('sans-serif',16),width=11,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_nop.place(x=30,y=30)

    var = IntVar()
    var.set(number_of_pages)
    entry_nop=Spinbox(frame2,textvariable=var,from_=1,to=number_of_pages,font=('sans-serif',16),width=15,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    entry_nop.place(x=200,y=30)
    done=Button(frame2,text="Start Extraction",font=("Times New Roman",18,"bold"),fg='white',width=20,height=2,bd=2,bg='black',highlightcolor='white',highlightthickness=5,cursor='hand2',command=lambda: extract_file())
    done.place(x=70,y=70)
    extp=int(entry_nop.get())

    op.mainloop()

def open_image():
    file =askopenfile(parent=te, mode='rb', filetype=[("Image file", "*.png *.jpeg *jpg")]) 
    # Opening the image & storing it in an image object
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract
    #Open image with PIL
    img = PIL.Image.open(file)
    def extract_image():
        #Extract text from image
        text = pytesseract.image_to_string(img)
        with open(f"{img.width}.txt","w",encoding='utf-8') as f:
            f.write(text)
        text_file=(f"{img.width}.txt")
        messagebox.showinfo('INFO',f'Your File has been saved at location: {os.path.abspath(text_file)}\nPlease note down the location of your file') 

    oi=Tk()
    oi.title("IMAGE Text Extractor")
    oi.geometry('500x500')
    oi.resizable(0,0)
    oi.config(bg="#081923",highlightcolor='white', highlightthickness=5)

    frame1=LabelFrame(oi,width=450,height=450,text='DETAILS!!!',bg='#087587',font=("Times New Roman",25,"bold"),highlightcolor='white', highlightthickness=3)
    frame1.place(x=20,y=20)

    label_size=Label(frame1,text='Size',font=("Times New Roman",10,"bold"),width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_size.place(x=30,y=40)
    entry_size=Label(frame1,text=img.size,font=("Times New Roman",10,"bold"),width=25,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2,justify='left')
    entry_size.place(x=200,y=40)

    label_height=Label(frame1,text='Height',font=("Times New Roman",10,"bold"),width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_height.place(x=30,y=90)
    entry_height=Label(frame1,text=img.height,font=("Times New Roman",10,"bold"),width=25,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    entry_height.place(x=200,y=90)

    label_width=Label(frame1,text='Width',font=("Times New Roman",10,"bold"),width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_width.place(x=30,y=140)
    entry_width=Label(frame1,text=img.width,font=("Times New Roman",10,"bold"),width=25,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    entry_width.place(x=200,y=140)

    label_format=Label(frame1,text='Format',font=("Times New Roman",10,"bold"),width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_format.place(x=30,y=190)
    entry_format=Label(frame1,text=img.format,font=("Times New Roman",10,"bold"),width=25,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    entry_format.place(x=200,y=190)

    label_mode=Label(frame1,text='Mode',font=("Times New Roman",10,"bold"),width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    label_mode.place(x=30,y=240)
    display_mode=Label(frame1,text=img.mode,font=("Times New Roman",10,"bold"),width=25,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=2)
    display_mode.place(x=200,y=240)

    done=Button(frame1,text="Start Extraction",font=("Times New Roman",18,"bold"),fg='white',width=20,height=2,bd=2,bg='black',highlightcolor='white',highlightthickness=3,cursor='hand2',command=lambda: extract_image())
    done.place(x=70,y=300)
    oi.mainloop()

te.mainloop()