from tkinter import END
import pandas as pd
from datetime import datetime


class Limpiar_datos_rph2_datetime:
    def __init__(self, rph2_data, fecha_desdeEntry, fecha_hastaEntry):

        # --GENERACION DE COLUMNA FECHA Y FILTRADO DE FECHA

        fecha_limite_inferior = "00-01-01"
        rph2_data = rph2_data.loc[(rph2_data["Date"] > fecha_limite_inferior)]
        rph2_data["DateTime"] = rph2_data["Date"] + " " + rph2_data["Time"]

        def date_valid(row):
            try:
                return pd.to_datetime(row, format="%y-%m-%d %H:%M:%S")
            except:
                pass

        rph2_data.DateTime = rph2_data.DateTime.apply(date_valid)

        # FILTRADO DE FECHA

        fecha_inicio = str(rph2_data["DateTime"].min())
        fecha_inicio = fecha_inicio.split()[0]
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()

        fecha_fin = str(rph2_data["DateTime"].max())
        fecha_fin = fecha_fin.split()[0]
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()

        if fecha_desdeEntry.get() == "" and fecha_hastaEntry.get() == "":

            fecha_desdeEntry.delete(0, END)
            fecha_hastaEntry.delete(0, END)
            fecha_desdeEntry.insert(0, fecha_inicio)
            fecha_hastaEntry.insert(0, fecha_fin)
        else:
            pass

        desde = str(fecha_desdeEntry.get())
        hasta = str(fecha_hastaEntry.get())
        single_quote = "'"
        condition = f"DateTime >= {single_quote}{desde}{single_quote} and DateTime < {single_quote}{hasta}{single_quote}"
        rph2_data = rph2_data.query(condition)

        self.rph2_data = rph2_data
