from tkinter import END
import re
from tkinter.messagebox import showwarning
from datetime import datetime, timedelta

# LIMPIEZA DE DATOS
class Limpiar_datos_rph2_close_or_open:
    def __init__(self, rph2_data, vertical_filter_Entry, operation):

        # --GENERACION DE TIEMPOS DE CIERRE
        # Validadcion de datos numericos. Se pretende solo numeros enteros o decimales con ','.
        patron = "^\d+(?:,\d+)?$"
        cadena = [vertical_filter_Entry.get()]

        if re.match(patron, cadena[0]):
            # EL DATO ES CORRECTO
            vertical_filter = int(vertical_filter_Entry.get())

        else:
            showwarning(
                "Mensaje de advertencia.",
                "Introducir valores correctos en campo de 'Filtro Vertical (CIERRE) [%]'. \nLos datos ingresados deben ser numericos o decimales con ,. \nPor favor volver a reintentar.",
            )

        # FILTRADO EJE VERTICAL
        def filter_cb_time(rph2_data, operation, fase, vertical_filter):

            rph2 = rph2_data.loc[
                (rph2_data["Direction"] == operation)
                & (rph2_data["Meas.Op.Time_" + fase] != 0)
                & (rph2_data["Meas.Op.Time_" + fase] != 999.9)
                & (rph2_data["Meas.Op.Time_" + fase] > 0)
            ]

            # ELIMINAR MANIOBRAS ESPURIAS
            # Se eliminan las maniobras generadas por un pulso demasiado largo de cierre/apertura
            maniobras_a_borrar = []
            for x in rph2.index:
                if x + 1 < rph2.index.max():
                    try:
                        fecha_1 = rph2["Date"][x] + " " + rph2["Time"][x]
                        fecha_1 = datetime.strptime(fecha_1, "%y-%m-%d %H:%M:%S")
                        fecha_2 = rph2["Date"][x + 1] + " " + rph2["Time"][x + 1]
                        fecha_2 = datetime.strptime(fecha_2, "%y-%m-%d %H:%M:%S")
                        if fecha_2 - fecha_1 < timedelta(seconds=5):
                            maniobras_a_borrar.append(x + 1)
                    except ValueError:
                        maniobras_a_borrar.append(x)
                    except KeyError:
                        pass

            rph2 = rph2.drop(maniobras_a_borrar)

            average_time = rph2["Meas.Op.Time_" + fase].mean()
            rph2 = rph2.loc[
                (
                    rph2["Meas.Op.Time_" + fase]
                    < average_time * (1 + vertical_filter / 100)
                )
                & (
                    rph2["Meas.Op.Time_" + fase]
                    > average_time * (1 - vertical_filter / 100)
                )
            ]

            average_time = rph2["Calc.Op.Time_" + fase].mean()
            rph2 = rph2.loc[
                (
                    rph2["Calc.Op.Time_" + fase]
                    < average_time * (1 + vertical_filter / 100)
                )
                & (
                    rph2["Calc.Op.Time_" + fase]
                    > average_time * (1 - vertical_filter / 100)
                )
            ]

            return rph2

        rph2_data_l1 = filter_cb_time(rph2_data, operation, "L1", vertical_filter)
        rph2_data_l2 = filter_cb_time(rph2_data_l1, operation, "L2", vertical_filter)
        rph2_data_l3 = filter_cb_time(rph2_data_l2, operation, "L3", vertical_filter)

        if operation == 1.0:
            self.rph2_close = rph2_data_l3

        elif operation == 0.0:
            self.rph2_open = rph2_data_l3
