from tkinter import *
from tkinter import messagebox

from CarpetaCoches import coches


class App:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Gestión de Vehículos")
        self.ventana.geometry("700x750")
        self.ventana.resizable(False, False)

        self.tipo = ""

        self.main()

    def borrarPantalla(self):

        for widget in self.ventana.winfo_children():
            widget.destroy()

    def obtener_clase(self):

        if self.tipo == "coche":
            return coches.Coches

        elif self.tipo == "camioneta":
            return coches.Camionetas

        elif self.tipo == "camion":
            return coches.Camiones

    def respuesta_sql(self, respuesta):

        if respuesta:

            messagebox.showinfo(
                "Correcto",
                "Operación realizada correctamente"
            )

        else:

            messagebox.showerror(
                "Error",
                "Ha ocurrido un error"
            )

    # ========================
    # MENÚ PRINCIPAL
    # ========================

    def main(self):

        self.borrarPantalla()

        Label(
            self.ventana,
            text="GESTIÓN DE VEHÍCULOS",
            font=("Arial", 18)
        ).pack(pady=20)

        Button(
            self.ventana,
            text="Coches",
            width=25,
            command=lambda: self.menu_acciones("coche")
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Camionetas",
            width=25,
            command=lambda: self.menu_acciones("camioneta")
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Camiones",
            width=25,
            command=lambda: self.menu_acciones("camion")
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Salir",
            width=25,
            command=self.ventana.quit
        ).pack(pady=20)

    # ========================
    # MENÚ CRUD
    # ========================

    def menu_acciones(self, tipo):

        self.tipo = tipo

        self.borrarPantalla()

        Label(
            self.ventana,
            text=f"GESTIÓN DE {tipo.upper()}",
            font=("Arial", 16)
        ).pack(pady=20)

        Button(
            self.ventana,
            text="Agregar",
            width=20,
            command=self.insertar_view
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Modificar",
            width=20,
            command=self.modificar_view
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Eliminar",
            width=20,
            command=self.eliminar_view
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Consultar",
            width=20,
            command=self.consultar_view
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Regresar",
            width=20,
            command=self.main
        ).pack(pady=10)

    # ========================
    # INSERTAR
    # ========================

    def insertar_view(self):

        self.borrarPantalla()

        Label(
            self.ventana,
            text=f"Agregar {self.tipo}"
        ).pack(pady=10)

        Label(self.ventana, text="Marca").pack()
        self.marca = Entry(self.ventana)
        self.marca.pack()

        Label(self.ventana, text="Color").pack()
        self.color = Entry(self.ventana)
        self.color.pack()

        Label(self.ventana, text="Modelo").pack()
        self.modelo = Entry(self.ventana)
        self.modelo.pack()

        Label(self.ventana, text="Velocidad").pack()
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack()

        Label(self.ventana, text="Potencia").pack()
        self.potencia = Entry(self.ventana)
        self.potencia.pack()

        Label(self.ventana, text="Plazas").pack()
        self.plazas = Entry(self.ventana)
        self.plazas.pack()

        # CAMPOS CAMIONETA

        if self.tipo == "camioneta":

            Label(self.ventana, text="Tracción").pack()
            self.traccion = Entry(self.ventana)
            self.traccion.pack()

            Label(self.ventana, text="Cerrada (1/0)").pack()
            self.cerrada = Entry(self.ventana)
            self.cerrada.pack()

        # CAMPOS CAMIÓN

        elif self.tipo == "camion":

            Label(self.ventana, text="Carga").pack()
            self.carga = Entry(self.ventana)
            self.carga.pack()

            Label(self.ventana, text="Número de ejes").pack()
            self.ejes = Entry(self.ventana)
            self.ejes.pack()

        Button(
            self.ventana,
            text="Guardar",
            command=self.insertar_controller
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Regresar",
            command=lambda: self.menu_acciones(self.tipo)
        ).pack()

    def insertar_controller(self):

        if self.tipo == "coche":

            vehiculo = coches.Coches(
                self.marca.get().upper(),
                self.color.get().upper(),
                self.modelo.get().upper(),
                self.velocidad.get(),
                self.potencia.get(),
                self.plazas.get()
            )

        elif self.tipo == "camioneta":

            vehiculo = coches.Camionetas(
                self.marca.get().upper(),
                self.color.get().upper(),
                self.modelo.get().upper(),
                self.velocidad.get(),
                self.potencia.get(),
                self.plazas.get(),
                self.traccion.get().upper(),
                self.cerrada.get()
            )

        else:

            vehiculo = coches.Camiones(
                self.marca.get().upper(),
                self.color.get().upper(),
                self.modelo.get().upper(),
                self.velocidad.get(),
                self.potencia.get(),
                self.plazas.get(),
                self.carga.get(),
                self.ejes.get()
            )

        self.respuesta_sql(
            vehiculo.insertar()
        )

    # ========================
    # MODIFICAR
    # ========================

    def modificar_view(self):

        self.borrarPantalla()

        Label(
            self.ventana,
            text="ID"
        ).pack()

        self.id = Entry(self.ventana)
        self.id.pack()

        Button(
            self.ventana,
            text="Buscar",
            command=self.buscar_modificar
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Regresar",
            command=lambda: self.menu_acciones(self.tipo)
        ).pack()

    def buscar_modificar(self):

        registros = self.obtener_clase().buscar(
            self.id.get()
        )

        if registros:

            messagebox.showinfo(
                "Encontrado",
                "Registro encontrado. Modifica desde SQL o amplia esta pantalla."
            )

        else:

            messagebox.showerror(
                "Error",
                "Registro no encontrado"
            )

    # ========================
    # ELIMINAR
    # ========================

    def eliminar_view(self):

        self.borrarPantalla()

        Label(
            self.ventana,
            text="ID"
        ).pack()

        self.id = Entry(self.ventana)
        self.id.pack()

        Button(
            self.ventana,
            text="Eliminar",
            command=self.eliminar_controller
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Regresar",
            command=lambda: self.menu_acciones(self.tipo)
        ).pack()

    def eliminar_controller(self):

        respuesta = self.obtener_clase().eliminar(
            self.id.get()
        )

        self.respuesta_sql(respuesta)

    # ========================
    # CONSULTAR
    # ========================

    def consultar_view(self):

        self.borrarPantalla()

        datos = self.obtener_clase().consultar()

        texto = ""

        for fila in datos:

            texto += f"{fila}\n"
            texto += "-" * 70 + "\n"

        if texto == "":
            texto = "No existen registros"

        Label(
            self.ventana,
            text=texto,
            justify=LEFT
        ).pack()

        Button(
            self.ventana,
            text="Regresar",
            command=lambda: self.menu_acciones(self.tipo)
        ).pack(pady=10)


if __name__ == "__main__":

    ventana = Tk()

    App(ventana)

    ventana.mainloop()