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
Todas las lámparas están al mismo precio de $800 pesos final.
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
        precio = float(800)
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        cantidad = int(cantidad)
    #A
        if cantidad >= 6:
            descuento = (precio * 50) / 100
            precio_final = cantidad * (precio - descuento)
            alert("UTN", "EL precio final con descuento es de: " + str(precio_final))
    #B
        elif cantidad == 5 and marca == "ArgentinaLuz":
            descuento = (precio * 40) / 100
            precio_final = cantidad * (precio - descuento)
            alert("UTN", "El precio final con descuento es de: " + str(precio_final))
    
        elif cantidad == 5:
                descuento = (precio * 30) / 100
                precio_final = cantidad * (precio - descuento)
                alert("UTN", "EL precio final con descuento es de: " + str(precio_final))
    #C
        elif cantidad == 4 and (marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
                descuento = (precio * 25) / 100
                precio_final = cantidad * (precio - descuento)
                alert("UTN", "EL precio final con descuento es de: " + str(precio_final))
            
        elif cantidad == 4:
            descuento = (precio * 20) / 100
            precio_final = cantidad * (precio - descuento)
            alert("UTN", "EL precio final con descuento es de: " + str(precio_final))
    #D 
        elif cantidad == 3 and marca == "ArgentinaLuz":
            descuento = (precio * 15) / 100
            precio_final = cantidad * (precio - descuento)
            alert("UTN", "EL precio final con descuento es de: " + str(precio_final))

        elif cantidad == 3 and marca == "FelipeLamparas":
            descuento = (precio * 10) / 100
            precio_final = cantidad * (precio - descuento)
            alert("UTN", "EL precio final con descuento es de: " + str(precio_final))

        elif cantidad == 3:
                descuento = (precio * 5) / 100
                precio_final = cantidad * (precio - descuento)
                alert("UTN", "EL precio final con descuento es de: " + str(precio_final))

        elif precio_final >= 4000:
            descuento_adicional = (precio_final * 5)/100
            precio_final_descuento_adicional = precio_final - descuento_adicional
            alert("UTN", "EL precio final con descuento es de: " + str(precio_final_descuento_adicional))
        
''' '''  
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()