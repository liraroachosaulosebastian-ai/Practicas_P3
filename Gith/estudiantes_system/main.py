from tkinter import *
from tkinter import messagebox
from CarpetaEstudiantes import estudiantes


class App:

    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title("Sistema Escolar")

        self.ventana.geometry("700x700")

        self.ventana.resizable(False, False)

        self.tipo = ""

        self.main()

    def borrarPantalla(self):

        for widget in self.ventana.winfo_children():
            widget.destroy()

    def respuesta_sql(self, respuesta):

        if respuesta:

            messagebox.showinfo(
                "Correcto",
                "Operación realizada correctamente"
            )

        else:

            messagebox.showerror(
                "Error",
                "No fue posible realizar la operación"
            )

    def obtener_clase(self):

        if self.tipo == "estudiante":
            return estudiantes.Estudiantes

        elif self.tipo == "docente":
            return estudiantes.Docentes

    # =====================
    # MENÚ PRINCIPAL
    # =====================

    def main(self):

        self.borrarPantalla()

        Label(
            self.ventana,
            text="SISTEMA ESCOLAR",
            font=("Arial", 18)
        ).pack(pady=20)

        Button(
            self.ventana,
            text="Estudiantes",
            width=25,
            command=lambda:
            self.menu_acciones("estudiante")
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Docentes",
            width=25,
            command=lambda:
            self.menu_acciones("docente")
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Salir",
            width=25,
            command=self.ventana.quit
        ).pack(pady=20)

    # =====================
    # MENÚ CRUD
    # =====================

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

    # =====================
    # INSERTAR
    # =====================

    def insertar_view(self):

        self.borrarPantalla()

        Label(
            self.ventana,
            text=f"Agregar {self.tipo}"
        ).pack(pady=10)

        Label(self.ventana, text="Nombre").pack()

        self.nombre = Entry(self.ventana)

        self.nombre.pack()

        if self.tipo == "estudiante":

            Label(
                self.ventana,
                text="Nota"
            ).pack()

            self.nota = Entry(self.ventana)

            self.nota.pack()

        else:

            Label(
                self.ventana,
                text="Materia"
            ).pack()

            self.materia = Entry(self.ventana)

            self.materia.pack()

            Label(
                self.ventana,
                text="Salario"
            ).pack()

            self.salario = Entry(self.ventana)

            self.salario.pack()

        Button(
            self.ventana,
            text="Guardar",
            command=self.insertar_controller
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Regresar",
            command=lambda:
            self.menu_acciones(self.tipo)
        ).pack()

    def insertar_controller(self):

        nombre = self.nombre.get().strip()

        if nombre == "":

            messagebox.showwarning(
                "Advertencia",
                "El nombre es obligatorio"
            )

            return

        if self.tipo == "estudiante":

            nota = self.nota.get().strip()

            try:
                float(nota)
            except:

                messagebox.showwarning(
                    "Advertencia",
                    "La nota debe ser numérica"
                )

                return

            obj = estudiantes.Estudiantes(
                nombre,
                nota
            )

        else:

            materia = self.materia.get().strip()

            salario = self.salario.get().strip()

            if materia == "":

                messagebox.showwarning(
                    "Advertencia",
                    "La materia es obligatoria"
                )

                return

            try:
                float(salario)
            except:

                messagebox.showwarning(
                    "Advertencia",
                    "El salario debe ser numérico"
                )

                return

            obj = estudiantes.Docentes(
                nombre,
                materia,
                salario
            )

        self.respuesta_sql(
            obj.insertar()
        )

    # =====================
    # ELIMINAR
    # =====================

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
            command=lambda:
            self.menu_acciones(self.tipo)
        ).pack()

    def eliminar_controller(self):

        id = self.id.get()

        if not id.isdigit():

            messagebox.showwarning(
                "Advertencia",
                "El ID debe ser numérico"
            )

            return

        resp = messagebox.askyesno(
            "Confirmación",
            "¿Desea eliminar el registro?"
        )

        if resp:

            respuesta = self.obtener_clase().eliminar(
                id
            )

            self.respuesta_sql(respuesta)

    # =====================
    # MODIFICAR
    # =====================

    def modificar_view(self):

        self.borrarPantalla()

        Label(
            self.ventana,
            text="ID"
        ).pack()

        self.id = Entry(self.ventana)

        self.id.pack()

        Label(
            self.ventana,
            text="Nombre"
        ).pack()

        self.nombre = Entry(self.ventana)

        self.nombre.pack()

        if self.tipo == "estudiante":

            Label(
                self.ventana,
                text="Nota"
            ).pack()

            self.nota = Entry(self.ventana)

            self.nota.pack()

        else:

            Label(
                self.ventana,
                text="Materia"
            ).pack()

            self.materia = Entry(self.ventana)

            self.materia.pack()

            Label(
                self.ventana,
                text="Salario"
            ).pack()

            self.salario = Entry(self.ventana)

            self.salario.pack()

        Button(
            self.ventana,
            text="Actualizar",
            command=self.modificar_controller
        ).pack(pady=10)

        Button(
            self.ventana,
            text="Regresar",
            command=lambda:
            self.menu_acciones(self.tipo)
        ).pack()

    def modificar_controller(self):

        id = self.id.get()

        if self.tipo == "estudiante":

            obj = estudiantes.Estudiantes(
                self.nombre.get(),
                self.nota.get()
            )

        else:

            obj = estudiantes.Docentes(
                self.nombre.get(),
                self.materia.get(),
                self.salario.get()
            )

        respuesta = obj.actualizar(id)

        self.respuesta_sql(respuesta)

    # =====================
    # CONSULTAR
    # =====================

    def consultar_view(self):

        self.borrarPantalla()

        registros = self.obtener_clase().consultar()

        texto = ""

        if registros:

            for fila in registros:

                texto += f"{fila}\n"
                texto += "-" * 60 + "\n"

        else:

            texto = "No existen registros"

        Label(
            self.ventana,
            text=texto,
            justify=LEFT
        ).pack()

        Button(
            self.ventana,
            text="Regresar",
            command=lambda:
            self.menu_acciones(self.tipo)
        ).pack(pady=10)


if __name__ == "__main__":

    ventana = Tk()

    App(ventana)

    ventana.mainloop()