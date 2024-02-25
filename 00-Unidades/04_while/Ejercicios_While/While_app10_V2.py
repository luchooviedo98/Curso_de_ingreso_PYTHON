import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Luciano
apellido:Oviedo
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    G. El máximo valor. 
    H. El mínimo valor (incluyendo en que iteracion se encontro, solo la primera)
    Informar los resultados mediante alert()


'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        minimo = 0
        maximo = 0
        bandera = True

        while True:
            numero = prompt("UTN","Ingrese numero")

            #prompt
            if numero == None:
                break
            
            while numero == "":
                numero = prompt("UTN","Ingrese numero")

            numero = int(numero)
            numero_ingresado = 0

            #contador
            if numero < numero_ingresado:
                acumulador_negativos += numero
                contador_negativos += 1
                minimo == numero
            elif numero > numero_ingresado: 
                acumulador_positivos += numero
                contador_positivos += 1
                maximo == numero
            else:
                if numero == 0:
                    contador_ceros += 1
            
        if bandera == True or numero < numero_minimo:
            numero_minimo = numero
            
        elif bandera == True or numero > numero_maximo:
            numero_maximo = numero

        diferencia_positivos_negativos = contador_positivos - contador_negativos

        mensaje = f"acumulador negativos: {acumulador_negativos}\n acumulador positivos: {acumulador_positivos}\n contador positivos: {contador_positivos} \n contador negativos: {contador_negativos}\n contador ceros: {contador_ceros}\n diferencia entre positivos y negativos: {diferencia_positivos_negativos}\n Máximo: {numero_maximo} \n Mínimo: {numero_minimo}"
        alert("Informe", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
