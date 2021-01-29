from tkinter import *
import tkinter.filedialog
from tkinter import messagebox

from corrector import correctFile

file ={
    'inputFile':'',
    'outputFile':''
}


window = Tk()
window.geometry("500x300")
window.title("CSV Corrector")
lb = Label(window, text="Mercurial Labs")
lb.config(font=("Courier", 44))
lb.config(fg="#0000FF")
lb.place(x=60,y=10)

Label(window, text="Delimiter").place(x=120, y=70)
delimiter=StringVar()
Entry(window, textvariable=delimiter, width=10).place(x=190, y=70)
inpL=Label(window, text=file['inputFile'])
outL=Label(window, text=file['outputFile'])

def getInpFilePath():
    file['inputFile'] = tkinter.filedialog.askopenfilename()
    inpL.config(text= file['inputFile'])


def getOutFilePath():
    files = [('CSV', '*.csv')]
    file['outputFile'] = tkinter.filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
    outL.config(text= file['outputFile'])

def correct():
    response = correctFile(file['inputFile'], file['outputFile'], delimiter.get())
    if 'error' in response:
        messagebox.showerror("Error", response['error'])
    else:
        messagebox.showinfo("MRC Labs", "Conversion complete.")
    print('correction done')

Button(window, text='Input file', command=getInpFilePath, width=8).place(x=130,y=120)
inpL.place(x=215,y=120)
Button(window, text='Output file', command=getOutFilePath, width=8).place(x=130,y=150)
outL.place(x=215,y=150)
Button(window, text='Correct', command=correct, width=10).place(x=140, y=190)


window.mainloop()
