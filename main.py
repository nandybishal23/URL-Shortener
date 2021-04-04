from tkinter import*
from typing import final
import pyshorteners
import clipboard

Canvas=Tk()
Canvas.geometry('350x220')
Canvas.resizable(False,False)
Canvas.title("URL Shortener")

url_input=Entry( font=("Hervetica","24"),justify='center', width = 20,borderwidth=2, relief="groove")
url_input.grid(row=1,column=2,pady=6)

str_url=StringVar()
shortened_url=Label(textvariable=str_url,font=("Hervetica","16"),fg="#fff",bg="#1abc9c")
shortened_url.grid(row=3,column=2,pady=6)


def copy_short_url():
    try:
        clipboard.copy(str_url.get())
        print("URL copied successfully !!")
    except:
        str_url.set("Something wrong try again !!")  

copy_btn=Button(text="Copy",bg="#34495e",fg="#fff",font=("helvetica","12"),activebackground="coral",command=copy_short_url)
copy_btn.grid(row=4,column=2,pady=6,padx=10)


def  short_url():
    try:
        s=pyshorteners.Shortener()
        url=url_input.get()
        final_result=s.tinyurl.short(url)
        str_url.set(final_result)
        url_input.delete(0,END)
    except:
        str_url.set("Enter url please !!")    


btn=Button(text="Short the URL",padx=8,pady=10,bg="#2ecc71",fg="#fff",font=("Helvetica","16"),activebackground="coral",command=short_url)
btn.grid(row=2,column=2,pady=6)

Canvas.mainloop()

