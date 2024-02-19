import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Luciano
apellido:Oviedo
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        precio = 800
        marca = self.combobox_marca
        cantidad_str = self.combobox_cantidad.get()
        cantidad = int(cantidad_str)
        descuento = 0
        precio_sin_descuento = precio * cantidad_str
        precio_sin_descuento = int(precio_sin_descuento)


        if cantidad >= 6:
            descuento = (precio_sin_descuento * 50) / 100
        elif cantidad == 5 and marca == "ArgentinaLuz":
            descuento = (precio_sin_descuento * 40 ) / 100
        else:
            descuento = (precio_sin_descuento * 30) / 100

        if cantidad == 4 and marca == "ArgentinaLuz" or "FelipeLamparas":
            descuento = (precio_sin_descuento * 25) / 100
        else:
            descuento = (precio_sin_descuento * 20) / 100

        if cantidad == 3 and marca == "ArgentinaLuz":
            descuento = (precio_sin_descuento * 15) / 100
        elif marca == "FelipeLamparas": 
            descuento == (precio_sin_descuento * 10) / 100
        else:
            descuento == (precio_sin_descuento * 5) / 100

        subtotal == precio_sin_descuento - descuento

        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()