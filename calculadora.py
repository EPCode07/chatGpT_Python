import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Creamos la entrada de texto
        self.display = tk.Entry(master, width=30, justify="right", font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Creamos los botones
        botones = [
        "7", "8", "9", "/", "C",
        "4", "5", "6", "*", "CE",
        "1", "2", "3", "-", "±",
        "0", ".", "%", "+", "="
        ]

        # Creamos los botones en un bucle y los ubicamos en la interfaz
        row = 1
        col = 0
        for boton in botones:
            command = lambda x=boton: self.click_boton(x)
            tk.Button(master, text=boton, width=5, height=2, font=('Arial', 16), command=command).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Creamos la variable que guardará el valor a calcular
        self.operacion = ""

    def click_boton(self, key):
        if key == "C":
            self.operacion = ""
            self.display.delete(0, tk.END)
        elif key == "CE":
            self.display.delete(0, tk.END)
        elif key == "±":
            if self.display.get()[0] == "-":
                self.display.delete(0)
            else:
                self.display.insert(0, "-")
        elif key == "=":
            try:
                resultado = str(eval(self.operacion))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
                self.operacion = resultado
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "ERROR")
        else:
            if self.display.get() == "ERROR":
                self.display.delete(0, tk.END)
            self.display.insert(tk.END, key)
            self.operacion += key

# Creamos la ventana
root = tk.Tk()
root.resizable(0, 0)

# Creamos la calculadora
mi_calculadora = Calculadora(root)

# Iniciamos el bucle de la aplicación
root.mainloop()