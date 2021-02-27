import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Conversor de Temperatura")

        #cantidad
        self.label=tk.Label(self.ventana,text="Cantidad:")
        self.label.grid(column=0, row=0)

        #introducir
        self.dato=tk.StringVar(value="0.0")
        self.entry_cantidad=tk.Entry(self.ventana, width=10, textvariable=self.dato)
        self.entry_cantidad.grid(column=1, row=0)

        #radiobutton
        self.seleccion=tk.IntVar()
        self.seleccion.set(3)

        self.radio1=tk.Radiobutton(self.ventana,text="Kelvin", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.ventana,text="Celsius", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=1)
        self.radio3=tk.Radiobutton(self.ventana,text="Farenheit", variable=self.seleccion, value=3)
        self.radio3.grid(column=2, row=1)


        #button
        self.boton=tk.Button(self.ventana, text="Convertir a:", command=self.convertir)
        self.boton.grid(column=1,row=2)


        #checkbutton
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana,text="Kelvin", variable=self.seleccion1)
        self.check1.grid(column=0, row=3)

        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana,text="Celsius", variable=self.seleccion2)
        self.check2.grid(column=1, row=3)

        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana,text="Farenheit", variable=self.seleccion3)
        self.check3.grid(column=2, row=3)

        #label final

        #kelvins
        self.labelKelvin=tk.Label(text="Kelvin:")
        self.labelKelvin.grid(column=0, row=4)

        self.labelResulKelvin=tk.Label()
        self.labelResulKelvin.grid(column=1, row=4)

        #celsius
        self.labelCelsius=tk.Label(text="Celsius:")
        self.labelCelsius.grid(column=0, row=5)

        self.labelResulCelsius=tk.Label()
        self.labelResulCelsius.grid(column=1, row=5)

        #farenheit
        self.labelFahrenheit=tk.Label(text="Fahrenheit:")
        self.labelFahrenheit.grid(column=0, row=6)

        self.labelResulFahrenheit=tk.Label()
        self.labelResulFahrenheit.grid(column=1, row=6)

        #llamar a la ventana
        self.ventana.mainloop()

    def convertir(self):
        if self.seleccion.get()==1:
            self.convertir_desde_kelvin()
        elif self.seleccion.get()==2:
            self.convertir_desde_celsius()  
        elif self.seleccion.get()==3:
            self.convertir_desde_farenheit()       
        pass        

    def convertir_desde_kelvin(self):        
        if self.seleccion1.get()==1:
            self.labelResulKelvin.configure(text=self.dato.get(), foreground="blue")
        else:
            self.labelResulKelvin.configure(text="-", foreground="red")

        if self.seleccion2.get()==1:    # kelvin a celsius
            self.labelResulCelsius.configure(text=float(self.dato.get())-273.15, foreground="blue")
        else:
            self.labelResulCelsius.configure(text="-", foreground="red")

        if self.seleccion3.get()==1:    # kelvin a fahrenheit
            self.labelResulFahrenheit.configure(text=float(self.dato.get())*9/5-459.67, foreground="blue")
        else:
            self.labelResulFahrenheit.configure(text="-", foreground="red")

    def convertir_desde_celsius(self):        
        if self.seleccion1.get()==1:    #celsius a kelvin
            self.labelResulKelvin.configure(text=float(self.dato.get())+273.15, foreground="blue")
        else:
            self.labelResulKelvin.configure(text="-", foreground="red")

        if self.seleccion2.get()==1:    
            self.labelResulCelsius.configure(text=(self.dato.get()), foreground="blue")
        else:
            self.labelResulCelsius.configure(text="-", foreground="red")

        if self.seleccion3.get()==1:    # celsius a fahrenheit
            self.labelResulFahrenheit.configure(text=float(self.dato.get())*9/5+32, foreground="blue")
        else:
            self.labelResulFahrenheit.configure(text="-", foreground="red")

    def convertir_desde_farenheit(self):        
        if self.seleccion1.get()==1:    #farenheit a kelvin
            self.labelResulKelvin.configure(text=(float(self.dato.get())-32)*5/9+273.15, foreground="blue")
        else:
            self.labelResulKelvin.configure(text="-", foreground="red")

        if self.seleccion2.get()==1:    #fahrenheit a celsius
            self.labelResulCelsius.configure(text=(float(self.dato.get())-32)*5/9, foreground="blue")
        else:
            self.labelResulCelsius.configure(text="-", foreground="red")

        if self.seleccion3.get()==1:    
            self.labelResulFahrenheit.configure(text=(self.dato.get()), foreground="blue")
        else:
            self.labelResulFahrenheit.configure(text="-", foreground="red")



aplicacion1=Aplicacion()