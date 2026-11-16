from conexionBD import conexion, cursor


# =====================================
# ESTUDIANTES
# =====================================

class Estudiantes:

    def __init__(self, nombre, nota):

        self._nombre = nombre
        self._nota = nota

    @property
    def Nombre(self):
        return self._nombre

    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def Nota(self):
        return self._nota

    @Nota.setter
    def Nota(self, nota):
        self._nota = nota

    # ------------------------
    # INSERTAR
    # ------------------------

    def insertar(self):

        try:

            cursor.execute(
                """
                INSERT INTO estudiantes
                VALUES(NULL, %s, %s)
                """,
                (
                    self._nombre,
                    self._nota
                )
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al insertar:", e)

            return False

    # ------------------------
    # CONSULTAR
    # ------------------------

    @staticmethod
    def consultar():

        try:

            cursor.execute(
                "SELECT * FROM estudiantes"
            )

            return cursor.fetchall()

        except Exception as e:

            print("Error al consultar:", e)

            return []

    # ------------------------
    # BUSCAR
    # ------------------------

    @staticmethod
    def buscar(id):

        try:

            cursor.execute(
                "SELECT * FROM estudiantes WHERE id=%s",
                (id,)
            )

            return cursor.fetchall()

        except Exception as e:

            print("Error al buscar:", e)

            return []

    # ------------------------
    # ELIMINAR
    # ------------------------

    @staticmethod
    def eliminar(id):

        try:

            cursor.execute(
                "DELETE FROM estudiantes WHERE id=%s",
                (id,)
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al eliminar:", e)

            return False

    # ------------------------
    # ACTUALIZAR
    # ------------------------

    def actualizar(self, id):

        try:

            cursor.execute(
                """
                UPDATE estudiantes
                SET nombre=%s,
                    nota=%s
                WHERE id=%s
                """,
                (
                    self._nombre,
                    self._nota,
                    id
                )
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al actualizar:", e)

            return False


# =====================================
# DOCENTES
# =====================================

class Docentes:

    def __init__(
        self,
        nombre,
        materia,
        salario
    ):

        self._nombre = nombre
        self._materia = materia
        self._salario = salario

    @property
    def Nombre(self):
        return self._nombre

    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def Materia(self):
        return self._materia

    @Materia.setter
    def Materia(self, materia):
        self._materia = materia

    @property
    def Salario(self):
        return self._salario

    @Salario.setter
    def Salario(self, salario):
        self._salario = salario

    # ------------------------
    # INSERTAR
    # ------------------------

    def insertar(self):

        try:

            cursor.execute(
                """
                INSERT INTO docentes
                VALUES(NULL, %s, %s, %s)
                """,
                (
                    self._nombre,
                    self._materia,
                    self._salario
                )
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al insertar:", e)

            return False

    # ------------------------
    # CONSULTAR
    # ------------------------

    @staticmethod
    def consultar():

        try:

            cursor.execute(
                "SELECT * FROM docentes"
            )

            return cursor.fetchall()

        except Exception as e:

            print("Error al consultar:", e)

            return []

    # ------------------------
    # BUSCAR
    # ------------------------

    @staticmethod
    def buscar(id):

        try:

            cursor.execute(
                "SELECT * FROM docentes WHERE id=%s",
                (id,)
            )

            return cursor.fetchall()

        except Exception as e:

            print("Error al buscar:", e)

            return []

    # ------------------------
    # ELIMINAR
    # ------------------------

    @staticmethod
    def eliminar(id):

        try:

            cursor.execute(
                "DELETE FROM docentes WHERE id=%s",
                (id,)
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al eliminar:", e)

            return False

    # ------------------------
    # ACTUALIZAR
    # ------------------------

    def actualizar(self, id):

        try:

            cursor.execute(
                """
                UPDATE docentes
                SET nombre=%s,
                    materia=%s,
                    salario=%s
                WHERE id=%s
                """,
                (
                    self._nombre,
                    self._materia,
                    self._salario,
                    id
                )
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al actualizar:", e)

            return False