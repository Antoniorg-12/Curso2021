import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.valor = 0
        self.label=tk.Label(self.ventana,text=self.valor)
        self.color()

        self.btn_inc=tk.Button(self.ventana, text="Incrementar", command=self.inc)
        self.btn_dec=tk.Button(self.ventana, text="Decrementar", command=self.dec)

        self.label.pack()
        self.btn_inc.pack()
        self.btn_dec.pack()
        self.ventana.mainloop()

    def color(self):
        if self.valor < 0:
            self.label.configure(foreground="blue")
        else:
            self.label.configure(foreground="red")   

    def inc(self):
        self.valor+=1
        self.color()
        self.label.config(text=self.valor)

    def dec(self):
        self.valor-=1
        self.color()
        self.label.config(text=self.valor)

aplicacion1=Aplicacion()
