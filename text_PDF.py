from tkinter import messagebox
from tkinter.filedialog import askopenfile
import os
import PyPDF2
import pypdfium2 as pdfium
from tkinter import *

te=Tk()
te.title("Text Extractor")
te.geometry('500x500')
te.resizable(0,0)
te.config(bg="#081923",highlightcolor='white', highlightthickness=5)

frame=LabelFrame(te,width=450,height=450,text='TEXT EXTRACTOR',font=("Times New Roman",28,"bold"),highlightcolor='white', highlightthickness=3)
frame.place(x=20,y=20)
message=Label(frame,width=46,font=("Times New Roman",12,"bold"),text='Welcome to Text Extractor Tool...\nThe Text extractor will allow you to extract text from any\nPDF  /  IMAGE  /  WEBSITE\nYou may upload any document(.pdf,.png) or Site address \nand the tool will pull text from the image \nand will save it in a text file :)')
message.place(x=14,y=35)
browse=Button(frame,text='CLICK TO SELECT PDF',font=("Segoe Script",10,"bold"),width=25,height=1,bd=2,fg='white',bg='black',activebackground='yellow',highlightbackground='black', highlightcolor='white', highlightthickness=3,cursor='hand2',command=lambda: open_pdf())
browse.place(x=95,y=180)
browse=Button(frame,text='CLICK TO SELECT IMAGE',font=("Segoe Script",10,"bold"),width=25,height=1,bd=2,fg='white',bg='black',activebackground='yellow',highlightbackground='black', highlightcolor='white', highlightthickness=3,cursor='hand2',command=lambda: open_image())
browse.place(x=95,y=240)
browse=Button(frame,text='CLICK TO SELECT WEBSITE',font=("Segoe Script",10,"bold"),width=25,height=1,bd=2,fg='white',bg='black',activebackground='yellow',highlightbackground='black', highlightcolor='white', highlightthickness=3,cursor='hand2',command=lambda: open_site())
browse.place(x=95,y=300)
def open_pdf():
    file = askopenfile(parent=te, mode='rb', filetype=[("Pdf file", "*.pdf")])
    readpdf=PyPDF2.PdfFileReader(file)
    pdf = pdfium.PdfDocument(file)
    fileinfo=PyPDF2.PdfFileReader.getDocumentInfo(readpdf)

    author = fileinfo.author
    creator = fileinfo.creator
    producer = fileinfo.producer
    title = fileinfo.title
    number_of_pages = len(pdf)
    op=Toplevel(te)
    op.title("Text Extractor")
    op.geometry('500x500')
    op.resizable(0,0)
    op.config(bg="#081923",highlightcolor='white', highlightthickness=5)

    frame1=LabelFrame(op,width=490,height=250,text='DETAILS!!!',font=("Times New Roman",25,"bold"),highlightbackground='black', highlightcolor='white', highlightthickness=3)
    frame1.pack()

    label_title=Label(frame1,text='Title',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    label_title.place(x=30,y=30)
    entry_title=Label(frame1,text='NOT AVAILABLE',width=35,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1,justify='left')
    entry_title.configure(text=title)
    entry_title.place(x=190,y=30)

    label_author=Label(frame1,text='Author',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    label_author.place(x=30,y=60)
    entry_author=Label(frame1,text='NOT AVAILABLE',width=35,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    entry_author.configure(text=author)
    entry_author.place(x=190,y=60)

    label_creator=Label(frame1,text='Creator',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    label_creator.place(x=30,y=90)
    entry_creator=Label(frame1,text='NOT AVAILABLE',width=35,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    entry_creator.configure(text=creator)
    entry_creator.place(x=190,y=90)

    label_producer=Label(frame1,text='Producer',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    label_producer.place(x=30,y=120)
    entry_producer=Label(frame1,text='NOT AVAILABLE',width=35,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    entry_producer.configure(text=producer)
    entry_producer.place(x=190,y=120)

    label_nop=Label(frame1,text='Number of pages',width=20,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    label_nop.place(x=30,y=150)
    display_nop=Label(frame1,text=number_of_pages,width=35,height=2,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    display_nop.place(x=190,y=150)


    frame2=LabelFrame(op,width=490,height=250,text='Extract Text',font=("Times New Roman",25,"bold"),highlightbackground='black', highlightcolor='white', highlightthickness=3)
    frame2.pack()

    label_nop=Label(frame2,text='Number of pages',width=20,height=1,bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    label_nop.place(x=30,y=30)

    var = IntVar()
    var.set(number_of_pages)
    entry_nop=Spinbox(frame2,textvariable=var,from_=1,to=number_of_pages,font=('sans-serif'),bg='black',fg='white',highlightcolor='white', highlightthickness=1)
    entry_nop.place(x=190,y=30)
    done=Button(frame2,text="Start Extraction",fg='white',width=30,height=3,bd=2,bg='black',highlightcolor='white',highlightthickness=3,cursor='hand2',command=lambda: extract_file())
    done.place(x=90,y=60)
    extp=int(entry_nop.get())
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
    op.mainloop()


te.mainloop()