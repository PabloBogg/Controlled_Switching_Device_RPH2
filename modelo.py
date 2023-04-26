from tkinter import filedialog as fd
from tkinter import END
import pandas as pd
import re
from tkinter.messagebox import showwarning
from datetime import datetime, timedelta
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from diagnostico_target_funcionamiento import DiagnosticoTargetFuncionamiento
from diagnostico_control_adaptable import DiagnosticoControlAdaptable
from diagnostico_alarmas import DiagnosticoAlarmas
from lectura_rph2 import Lectura_rph2
from limpiar_datos_rph2_close_or_open import Limpiar_datos_rph2_close_or_open
from limpiar_datos_rph2_datetime import Limpiar_datos_rph2_datetime
from graficar_rph2 import Graficar_rph2


# DIAGNOSTICO
class AbriArchivoConfiguracion(
    DiagnosticoTargetFuncionamiento, DiagnosticoControlAdaptable, DiagnosticoAlarmas
):
    def __init__(
        self,
    ):
        # OPEN FILE
        global filename_config
        filetypes = (
            ("RPH2 Files", "*.rph"),
            ("Text Files", "*.txt"),
            ("Comma Separated Value", "*.csv"),
            ("All Files", "*.*"),
        )

        filename_config = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )

        # --LECTURA DE ARCHIVO .TXT
        rph2_configuration = pd.read_csv(filename_config, sep="=", header=[0])
        columns = ["Values"]
        rph2_configuration.columns = columns

        def lista(_str):
            numero = ""
            lista = []
            contador = 0

            for x in _str:
                contador += 1
                if x != "," and x != " ":
                    numero += x
                    if contador == len(_str):
                        lista.append(float(numero))
                    else:
                        pass
                elif x == ",":
                    lista.append(float(numero))
                    numero = ""
                else:
                    pass
            return lista

        # PROGRAMA DE MANIOBRA
        self.programa_de_maniobra = rph2_configuration.loc["SwitchingProgram", "Values"]

        # TIEMPO AJUSTADO PARA CIERRE (CH1) Y APERTURA (CH2)
        self.tiempo_config_l1_ch1 = lista(
            rph2_configuration.loc["TimingOpTime", "Values"]
        )[0]
        self.tiempo_config_l2_ch1 = lista(
            rph2_configuration.loc["TimingOpTime", "Values"]
        )[1]
        self.tiempo_config_l3_ch1 = lista(
            rph2_configuration.loc["TimingOpTime", "Values"]
        )[2]

        self.tiempo_config_l1_ch2 = lista(
            rph2_configuration.loc["TimingOpTime", "Values"]
        )[3]
        self.tiempo_config_l2_ch2 = lista(
            rph2_configuration.loc["TimingOpTime", "Values"]
        )[4]
        self.tiempo_config_l3_ch2 = lista(
            rph2_configuration.loc["TimingOpTime", "Values"]
        )[5]

        # TIEMPO AJUSTADO DE ARCO PARA CIERRE (CH1) Y APERTURA (CH2)
        self.tiempo_arc_l1_ch1 = lista(
            rph2_configuration.loc["TimingArcTime", "Values"]
        )[0]
        self.tiempo_arc_l2_ch1 = lista(
            rph2_configuration.loc["TimingArcTime", "Values"]
        )[1]
        self.tiempo_arc_l3_ch1 = lista(
            rph2_configuration.loc["TimingArcTime", "Values"]
        )[2]

        self.tiempo_arc_l1_ch2 = lista(
            rph2_configuration.loc["TimingArcTime", "Values"]
        )[3]
        self.tiempo_arc_l2_ch2 = lista(
            rph2_configuration.loc["TimingArcTime", "Values"]
        )[4]
        self.tiempo_arc_l3_ch2 = lista(
            rph2_configuration.loc["TimingArcTime", "Values"]
        )[5]

        # COMPENSACION (p--> presion, t-->temperatura, v-->tension, adp-->control adaptativo)

        def compensacion_on_off(compensacion, temp=0):
            on_off = ""
            if compensacion == 0:
                on_off = "Off"
            else:
                if temp == 0:
                    on_off = "On" + " (factor: " + str(compensacion) + ")"
                elif temp == 1:
                    on_off = "On"
            return on_off

        self.compensacion_p_ch1 = compensacion_on_off(
            lista(rph2_configuration.loc["Compensation", "Values"])[0]
        )
        self.compensacion_p_ch2 = compensacion_on_off(
            lista(rph2_configuration.loc["Compensation", "Values"])[1]
        )
        self.compensacion_v_ch1 = compensacion_on_off(
            lista(rph2_configuration.loc["Compensation", "Values"])[2]
        )
        self.compensacion_v_ch2 = compensacion_on_off(
            lista(rph2_configuration.loc["Compensation", "Values"])[3]
        )
        self.compensacion_t_ch1 = compensacion_on_off(
            lista(rph2_configuration.loc["Compensation", "Values"])[4], 1
        )
        self.compensacion_t_ch2 = compensacion_on_off(
            lista(rph2_configuration.loc["Compensation", "Values"])[5], 1
        )
        self.compensacion_adp = compensacion_on_off(
            lista(rph2_configuration.loc["Compensation", "Values"])[6]
        )

        # ALARMAS
        alarmas = [
            "Lock-out",
            "Frequency min",
            "Frequency max",
            "Ref.Voltage Failure",
            "RTC Impulse Failure",
            "Neutral intermediate",
            "Neutral grounded",
            "Neutral isolated",
            "Selftest ERROR",
            "Selftest CH1 ERROR",
            "Selftest CH2 ERROR",
            "Comm. Time CH1 min",
            "Comm. Time CH2 min",
            "Op. Time min",
            "Op. Time max",
            "Drive Mech. Failure",
            "Archive Full",
            "Archive Failure",
            "Control Voltage min",
            "Control Voltage max",
            "Temperature min",
            "Temperature max",
            "Temp.Transducer Fault",
            "Pressure min",
            "Pressure max",
            "Pres. Transducer Fault",
            "Current max",
        ]

        def alarmas_config(data, n_alarma, lista_alarmas):

            alarma = []
            for x in range(4, 31):

                if data.loc[n_alarma, "Values"][x] == "1":

                    alarma.append(lista_alarmas[x - 4])
            return alarma

        self.alarma_1 = alarmas_config(rph2_configuration, "Alarm1", alarmas)

        self.alarma_2 = alarmas_config(rph2_configuration, "Alarm2", alarmas)

        self.alarma_3 = alarmas_config(rph2_configuration, "Alarm3", alarmas)

        self.alarma_4 = alarmas_config(rph2_configuration, "Alarm4", alarmas)

        self.alarma_5 = alarmas_config(rph2_configuration, "Alarm5", alarmas)

        self.alarma_6 = alarmas_config(rph2_configuration, "Alarm6", alarmas)

        self.alarma_7 = alarmas_config(rph2_configuration, "Alarm7", alarmas)


# MENU
class BarraAbrir:
    def __init__(
        self,
        vertical_filter_closeEntry,
        vertical_filter_openEntry,
        fecha_desdeEntry,
        fecha_hastaEntry,
        close_l1,
        close_l2,
        close_l3,
        open_l1,
        open_l2,
        open_l3,
    ):  # OPEN FILE

        global filename_data

        filetypes = (
            ("Comma Separated Value", "*.csv"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*"),
        )

        filename_data = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )

        # RESETEAR LOS FILTRO Y FECHAS EN TKINTER
        fecha_desdeEntry.delete(0, END)
        fecha_hastaEntry.delete(0, END)

        vertical_filter_closeEntry.delete(0, END)
        vertical_filter_openEntry.delete(0, END)

        vertical_filter_closeEntry.insert(0, 50)
        vertical_filter_openEntry.insert(0, 50)

        # LECTURA DE DATOS SEGUN RELE

        self.rph2_data = Lectura_rph2(filename_data)

        self.rph2_close = Limpiar_datos_rph2_close_or_open(
            self.rph2_data.data, vertical_filter_closeEntry, 1.0
        )

        self.rph2_open = Limpiar_datos_rph2_close_or_open(
            self.rph2_data.data, vertical_filter_openEntry, 0.0
        )

        self.rph2_close_date = Limpiar_datos_rph2_datetime(
            self.rph2_close.rph2_close, fecha_desdeEntry, fecha_hastaEntry
        )
        self.rph2_open_date = Limpiar_datos_rph2_datetime(
            self.rph2_open.rph2_open, fecha_desdeEntry, fecha_hastaEntry
        )

        Graficar_rph2(
            "CLOSING TIME - L1",
            self.rph2_close_date.rph2_data,
            "Measured time L1",
            "Calculated time L1",
            close_l1,
            "L1",
        )
        Graficar_rph2(
            "CLOSING TIME - L2",
            self.rph2_close_date.rph2_data,
            "Measured time L2",
            "Calculated time L2",
            close_l2,
            "L2",
        )
        Graficar_rph2(
            "CLOSING TIME - L3",
            self.rph2_close_date.rph2_data,
            "Measured time L3",
            "Calculated time L3",
            close_l3,
            "L3",
        )

        Graficar_rph2(
            "OPENING TIME - L1",
            self.rph2_open_date.rph2_data,
            "Measured time L1",
            "Calculated time L1",
            open_l1,
            "L1",
        )
        Graficar_rph2(
            "OPENING TIME - L2",
            self.rph2_open_date.rph2_data,
            "Measured time L2",
            "Calculated time L2",
            open_l2,
            "L2",
        )
        Graficar_rph2(
            "OPENING TIME - L3",
            self.rph2_open_date.rph2_data,
            "Measured time L3",
            "Calculated time L3",
            open_l3,
            "L3",
        )

    def diagnostico_1(self):
        # NEUTRO DE LA CARGA
        # Se toma la mayoria de 0 (aislado) o 1 (a tierra) en la columna "Neutral"

        numero_mas_aparece = (
            self.rph2_close_date.rph2_data["Neutral"].value_counts().idxmax()
        )

        if str(numero_mas_aparece) == "1.0":
            self.neutro_carga = "Grounded"
        elif str(numero_mas_aparece) == "0.0":
            self.neutro_carga = "Isolated"
        else:
            self.neutro_carga = "Undefined"


class BarraSalir:
    def __init__(self, raiz):
        raiz.destroy()


class ActualizarGraficos:
    def __init__(
        self,
        vertical_filter_closeEntry,
        vertical_filter_openEntry,
        fecha_desdeEntry,
        fecha_hastaEntry,
        close_l1,
        close_l2,
        close_l3,
        open_l1,
        open_l2,
        open_l3,
    ):

        rph2_data = Lectura_rph2(filename_data)

        rph2_close = Limpiar_datos_rph2_close_or_open(
            rph2_data.data, vertical_filter_closeEntry, 1.0
        )
        rph2_open = Limpiar_datos_rph2_close_or_open(
            rph2_data.data, vertical_filter_openEntry, 0.0
        )

        rph2_close_date = Limpiar_datos_rph2_datetime(
            rph2_close.rph2_close, fecha_desdeEntry, fecha_hastaEntry
        )
        rph2_open_date = Limpiar_datos_rph2_datetime(
            rph2_open.rph2_open, fecha_desdeEntry, fecha_hastaEntry
        )

        Graficar_rph2(
            "CLOSING TIME - L1",
            rph2_close_date.rph2_data,
            "Measured time L1",
            "Calculated time L1",
            close_l1,
            "L1",
        )
        Graficar_rph2(
            "CLOSING TIME - L2",
            rph2_close_date.rph2_data,
            "Measured time L2",
            "Calculated time L2",
            close_l2,
            "L2",
        )
        Graficar_rph2(
            "CLOSING TIME - L3",
            rph2_close_date.rph2_data,
            "Measured time L3",
            "Calculated time L3",
            close_l3,
            "L3",
        )

        Graficar_rph2(
            "OPENING TIME - L1",
            rph2_open_date.rph2_data,
            "Measured time L1",
            "Calculated time L1",
            open_l1,
            "L1",
        )
        Graficar_rph2(
            "OPENING TIME - L2",
            rph2_open_date.rph2_data,
            "Measured time L2",
            "Calculated time L2",
            open_l2,
            "L2",
        )
        Graficar_rph2(
            "OPENING TIME - L3",
            rph2_open_date.rph2_data,
            "Measured time L3",
            "Calculated time L3",
            open_l3,
            "L3",
        )
