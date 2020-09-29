from main import Job
from tkinter import *
root=Tk()

class Aplicacao():
    def __init__(self):
        self.root=root
        self.Tela()
        self.Frame()
        self.BT()
        root.mainloop()
    def Tela(self):
        self.root.title('Alerta BTL')
        self.root.configure(background='black')
        self.root.geometry('300x200')
        self.root.maxsize(width=1280,height=1024)
    def Frame(self):
        self.Main=Frame(self.root,bg= 'white',highlightbackground='black')
        self.Main.place(relx= 0.01, rely=0.01, relwidth= 0.98, relheight=0.98)
    def BT(self):
        self.btaction=Button(self.Main,text='Disparar',command=Job)
        self.btaction.place(relx=0.25,rely=0.2,relwidth=0.5,relheight=0.2)

        def Quit(): self.root.destroy()
        self.btpara=Button(self.Main,text='Parar',command=Quit)
        self.btpara.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.2)

Aplicacao()
