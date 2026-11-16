from conexionBD import conexion, cursor


class Coches:

    def __init__(self, marca, color, modelo, velocidad, potencia, plazas):

        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._plazas = plazas

    # MÉTODOS

    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1

    # PROPIEDADES

    @property
    def Marca(self):
        return self._marca

    @Marca.setter
    def Marca(self, marca):
        self._marca = marca

    @property
    def Color(self):
        return self._color

    @Color.setter
    def Color(self, color):
        self._color = color

    @property
    def Modelo(self):
        return self._modelo

    @Modelo.setter
    def Modelo(self, modelo):
        self._modelo = modelo

    @property
    def Velocidad(self):
        return self._velocidad

    @Velocidad.setter
    def Velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def Potencia(self):
        return self._potencia

    @Potencia.setter
    def Potencia(self, potencia):
        self._potencia = potencia

    @property
    def Plazas(self):
        return self._plazas

    @Plazas.setter
    def Plazas(self, plazas):
        self._plazas = plazas

    # CRUD

    def insertar(self):

        try:

            cursor.execute(
                """
                INSERT INTO coches
                VALUES(NULL,%s,%s,%s,%s,%s,%s)
                """,
                (
                    self._marca,
                    self._color,
                    self._modelo,
                    self._velocidad,
                    self._potencia,
                    self._plazas
                )
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al insertar:", e)

            return False

    @staticmethod
    def consultar():

        try:

            cursor.execute(
                "SELECT * FROM coches"
            )

            return cursor.fetchall()

        except Exception as e:

            print("Error al consultar:", e)

            return []

    @staticmethod
    def buscar(id):

        try:

            cursor.execute(
                "SELECT * FROM coches WHERE id=%s",
                (id,)
            )

            return cursor.fetchall()

        except Exception as e:

            print("Error al buscar:", e)

            return []

    @staticmethod
    def eliminar(id):

        try:

            cursor.execute(
                "DELETE FROM coches WHERE id=%s",
                (id,)
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al eliminar:", e)

            return False

    def actualizar(self, id):

        try:

            cursor.execute(
                """
                UPDATE coches
                SET marca=%s,
                    color=%s,
                    modelo=%s,
                    velocidad=%s,
                    potencia=%s,
                    plazas=%s
                WHERE id=%s
                """,
                (
                    self._marca,
                    self._color,
                    self._modelo,
                    self._velocidad,
                    self._potencia,
                    self._plazas,
                    id
                )
            )

            conexion.commit()

            return True

        except Exception as e:

            print("Error al actualizar:", e)

            return False


# ==========================================
# CAMIONETAS
# ==========================================

class Camionetas(Coches):

    def __init__(
        self,
        marca,
        color,
        modelo,
        velocidad,
        potencia,
        plazas,
        traccion,
        cerrada
    ):

        super().__init__(
            marca,
            color,
            modelo,
            velocidad,
            potencia,
            plazas
        )

        self._traccion = traccion
        self._cerrada = cerrada

    def acelerar(self):

        self._velocidad += 1

        print("Acelerando camioneta")

    def frenar(self):

        self._velocidad -= 1

        print("Frenando camioneta")

    def transportar(self, personas):

        print(
            f"Transportando {personas} pasajeros"
        )

    @property
    def Traccion(self):
        return self._traccion

    @Traccion.setter
    def Traccion(self, traccion):
        self._traccion = traccion

    @property
    def Cerrada(self):
        return self._cerrada

    @Cerrada.setter
    def Cerrada(self, cerrada):
        self._cerrada = cerrada


# ==========================================
# CAMIONES
# ==========================================

class Camiones(Coches):

    def __init__(
        self,
        marca,
        color,
        modelo,
        velocidad,
        potencia,
        plazas,
        carga,
        ejes
    ):

        super().__init__(
            marca,
            color,
            modelo,
            velocidad,
            potencia,
            plazas
        )

        self._carga = carga
        self._ejes = ejes

    def acelerar(self):

        self._velocidad += 1

        print("Acelerando camión")

    def frenar(self):

        self._velocidad -= 1

        print("Frenando camión")

    def transportar_carga(self):

        print(
            f"Transportando {self._carga} kg"
        )

    @property
    def Carga(self):
        return self._carga

    @Carga.setter
    def Carga(self, carga):
        self._carga = carga

    @property
    def Ejes(self):
        return self._ejes

    @Ejes.setter
    def Ejes(self, ejes):
        self._ejes = ejes