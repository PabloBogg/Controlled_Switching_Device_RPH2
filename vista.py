from tkcalendar import Calendar
import tkinter as tk
from tkinter import Tk
from tkinter import Menu
from tkinter import Label
from tkinter import IntVar
from tkinter import W
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter import ttk
from tkinter import Frame
from modelo import *
from tkinter import Scrollbar
import customtkinter


class Vista:
    def __init__(self, ventana) -> None:

        # --VISTA--
        self.raiz = ventana

        # --TITULO Y PANTALLA COMPLETA--
        self.raiz.title("SYNCHRONIZERS ANALYSIS")
        self.width = self.raiz.winfo_screenwidth()
        self.height = self.raiz.winfo_screenheight()
        self.raiz.geometry("%dx%d" % (self.width, self.height))

        # --MENU DE OPCIONES
        self.menubar = Menu(self.raiz)

        # MENU OPCIONES
        self.menu_opciones = Menu(self.menubar, tearoff=0)

        def rph2():
            global obj_rph2
            obj_rph2 = BarraAbrir(
                self.vertical_filter_closeEntry,
                self.vertical_filter_openEntry,
                self.fecha_desdeEntry,
                self.fecha_hastaEntry,
                self.close_l1,
                self.close_l2,
                self.close_l3,
                self.open_l1,
                self.open_l2,
                self.open_l3,
            )

            obj_rph2.diagnostico_1()

        abrir = Menu(self.menu_opciones, tearoff=0)
        abrir.add_command(label="File.CSV (graphics)", command=lambda: rph2())
        self.menu_opciones.add_cascade(label="Open", menu=abrir)
        self.menu_opciones.add_separator()
        self.menu_opciones.add_command(
            label="Exit", command=lambda: BarraSalir(self.raiz)
        )
        self.menubar.add_cascade(label="Options", menu=self.menu_opciones)
        self.raiz.config(menu=self.menubar)

        # MENU CONFIGURACION
        #   TEMA
        self.menu_configuracion = Menu(self.menubar, tearoff=0)

        def claro():
            return customtkinter.set_appearance_mode("light")

        def oscuro():
            return customtkinter.set_appearance_mode("dark")

        temas = Menu(self.menu_configuracion, tearoff=0)
        temas.add_command(label="Light", command=lambda: claro())
        temas.add_command(label="Dark", command=lambda: oscuro())
        self.menu_configuracion.add_cascade(label="Aappearance", menu=temas)

        self.menubar.add_cascade(label="Configuration", menu=self.menu_configuracion)
        self.raiz.config(menu=self.menubar)

        # --INGRESAR DATOS Y BOTONES
        customtkinter.CTkLabel(self.raiz, text="Graph Parameters").grid(
            row=0, column=0, columnspan=5
        )

        self.vertical_filter_close = IntVar()
        self.vertical_filter_close = customtkinter.CTkLabel(
            self.raiz, text="Vertical Filter (CLOSING) [%]"
        )
        self.vertical_filter_close.grid(row=1, column=0)
        self.vertical_filter_closeEntry = customtkinter.CTkEntry(
            self.raiz, placeholder_text=self.vertical_filter_close
        )
        self.vertical_filter_closeEntry.grid(row=1, column=1)
        self.vertical_filter_closeEntry.insert(0, 50)

        self.vertical_filter_open = IntVar()
        self.vertical_filter_open = customtkinter.CTkLabel(
            self.raiz, text="Vertical Filter (OPENING) [%]"
        )
        self.vertical_filter_open.grid(row=2, column=0)
        self.vertical_filter_openEntry = customtkinter.CTkEntry(
            self.raiz, placeholder_text=self.vertical_filter_open
        )
        self.vertical_filter_openEntry.grid(row=2, column=1)
        self.vertical_filter_openEntry.insert(0, 50)

        self.fecha_desdeEntry = customtkinter.CTkEntry(self.raiz)
        self.fecha_desdeEntry.grid(row=1, column=3)

        self.fecha_hastaEntry = customtkinter.CTkEntry(self.raiz)
        self.fecha_hastaEntry.grid(row=2, column=3)

        self.boton_actualizar_grafica = customtkinter.CTkButton(
            self.raiz,
            text="Update Graphics",
            command=lambda: ActualizarGraficos(
                self.vertical_filter_closeEntry,
                self.vertical_filter_openEntry,
                self.fecha_desdeEntry,
                self.fecha_hastaEntry,
                self.close_l1,
                self.close_l2,
                self.close_l3,
                self.open_l1,
                self.open_l2,
                self.open_l3,
            ),
        )
        self.boton_actualizar_grafica.grid(row=1, column=4, rowspan=2)

        def fecha_desde(raiz, fecha_desdeEntry):
            def inster_fecha(fecha_desdeEntry, cal):
                fecha_desdeEntry.delete(0, END)
                fecha_desdeEntry.insert(0, cal)

            top = tk.Toplevel(raiz)
            top.title("SELECTION: AS OF DATE")
            cal = Calendar(
                top,
                font="Arial 14",
                selectmode="day",
                cursor="hand1",
                date_pattern="y-mm-dd",
            )
            cal.pack(fill="both", expand=True)
            ttk.Button(
                top,
                text="Select",
                command=lambda: (inster_fecha(fecha_desdeEntry, cal.selection_get())),
            ).pack()

        self.boton_fecha_desde = customtkinter.CTkButton(
            self.raiz,
            text="From",
            command=lambda: fecha_desde(self.raiz, self.fecha_desdeEntry),
        ).grid(row=1, column=2)

        def fecha_hasta(raiz, fecha_hastaEntry):
            def inster_fecha(fecha_hastaEntry, cal):
                fecha_hastaEntry.delete(0, END)
                fecha_hastaEntry.insert(0, cal)

            top = tk.Toplevel(raiz)
            top.title("SELECTION: TO DATE")
            cal = Calendar(
                top,
                font="Arial 14",
                selectmode="day",
                cursor="hand1",
            )
            cal.pack(fill="both", expand=True)
            ttk.Button(
                top,
                text="Select",
                command=lambda: (inster_fecha(fecha_hastaEntry, cal.selection_get())),
            ).pack()

        self.boton_fecha_hasta = customtkinter.CTkButton(
            self.raiz,
            text="To",
            command=lambda: fecha_hasta(self.raiz, self.fecha_hastaEntry),
        ).grid(row=2, column=2)

        # --PESTAÑAS DE LA RAIZ
        self.graficos = customtkinter.CTkTabview(master=self.raiz)
        self.graficos.grid(row=3, column=0, columnspan=5)

        self.graficos_de_cierre = self.graficos.add("CLOSING CHARTS")
        self.pestaña_cierre = customtkinter.CTkFrame(self.graficos_de_cierre)
        self.pestaña_cierre.pack()

        self.graficos_de_apertura = self.graficos.add("OPENING GRAPHS")
        self.pestaña_apertura = customtkinter.CTkFrame(self.graficos_de_apertura)
        self.pestaña_apertura.pack()

        self.diagnostico_1 = self.graficos.add("DIAGNOSIS 1")
        self.pestaña_diagnostico_1 = customtkinter.CTkFrame(self.diagnostico_1)
        self.pestaña_diagnostico_1.pack(fill="both")

        self.diagnostico_2 = self.graficos.add("DIAGNOSIS 2")
        self.pestaña_diagnostico_2 = customtkinter.CTkFrame(self.diagnostico_2)
        self.pestaña_diagnostico_2.pack(fill="both")

        self.diagnostico_3 = self.graficos.add("DIAGNOSIS 3")
        self.pestaña_diagnostico_3 = customtkinter.CTkFrame(self.diagnostico_3)
        self.pestaña_diagnostico_3.pack(fill="both")

        # --VENTANA DE GRAFICO CIERRE L1
        self.close_l1 = customtkinter.CTkFrame(self.pestaña_cierre)

        self.close_l1.grid(row=3, column=0, padx=5, pady=15)

        # --VENTANA DE GRAFICO CIERRE L2
        self.close_l2 = customtkinter.CTkFrame(self.pestaña_cierre)

        self.close_l2.grid(row=3, column=1, padx=5, pady=15)

        # --VENTANA DE GRAFICO CIERRE L3
        self.close_l3 = customtkinter.CTkFrame(self.pestaña_cierre)

        self.close_l3.grid(row=3, column=2, padx=5, pady=15)

        # --VENTANA DE GRAFICO APERTURA L1
        self.open_l1 = customtkinter.CTkFrame(self.pestaña_apertura)

        self.open_l1.grid(row=4, column=0, padx=5, pady=15)

        # --VENTANA DE GRAFICO APERTURA L2
        self.open_l2 = customtkinter.CTkFrame(self.pestaña_apertura)

        self.open_l2.grid(row=4, column=1, padx=5, pady=15)

        # --VENTANA DE GRAFICO APERTURA L3
        self.open_l3 = customtkinter.CTkFrame(self.pestaña_apertura)

        self.open_l3.grid(row=4, column=2, padx=5, pady=15)

        # --VENTANA DE DIAGNOSTICO_1
        self.diagnostico_1 = customtkinter.CTkFrame(
            self.pestaña_diagnostico_1,
        )
        self.diagnostico_1.grid(row=4, column=0, padx=5, pady=15)

        # --INFORMACION DE DIAGNOSTICO
        def mostrar_diagnostico_1(obj_config):

            # TITULO: DATOS DEL SISTEMA
            customtkinter.CTkLabel(self.diagnostico_1, text="System Data").grid(
                row=0, column=0, sticky="ew", columnspan=2
            )

            #       PROGRAMA DE MANIOBRA
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tSwitching Program: ",
            ).grid(row=1, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_config.programa_de_maniobra),
            ).grid(row=1, column=1)

            #       NEUTRO DE LA CARGA
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tNeutral of the load: ",
            ).grid(row=2, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_rph2.neutro_carga),
            ).grid(row=2, column=1)

            # TITULO: COMPENSACION
            customtkinter.CTkLabel(
                self.diagnostico_1, text="Circuit Breaker Data - Compensation"
            ).grid(row=4, column=0, sticky="ew", columnspan=2)

            #       PRESION CH1
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tPressure CH1: ",
            ).grid(row=5, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_config.compensacion_p_ch1),
            ).grid(row=5, column=1)

            #       PRESION CH2
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tPressure CH2: ",
            ).grid(row=6, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_config.compensacion_p_ch2),
            ).grid(row=6, column=1)

            #       TENSION CH1
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tVoltage CH1: ",
            ).grid(row=7, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_config.compensacion_v_ch1),
            ).grid(row=7, column=1)

            #       TENSION CH2
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tVoltage CH2: ",
            ).grid(row=8, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_config.compensacion_v_ch2),
            ).grid(row=8, column=1)

            #       TEMPERATURA CH1
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tTemperature CH1: ",
            ).grid(row=9, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_config.compensacion_t_ch1),
            ).grid(row=9, column=1)

            #       TEMPERATURA CH2
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tTemperature CH2: ",
            ).grid(row=10, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_config.compensacion_t_ch2),
            ).grid(row=10, column=1)

            #       CONTROL AUTOADAPTATIVO
            customtkinter.CTkLabel(
                self.diagnostico_1,
                text="\tAutoadaptive Control: ",
            ).grid(row=11, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_1,
                text=str(obj_config.compensacion_adp),
            ).grid(row=11, column=1)

            # ----------VISUALIZACIÓN DE DATOS------------------------------

            self.vista_1 = customtkinter.CTkFrame(self.diagnostico_1)

            customtkinter.CTkLabel(
                self.vista_1,
                text="PERFORMANCE",
            ).grid(row=0, column=0, sticky="ew", columnspan=2)

            self.vista_1.grid(row=13, columnspan=2)

            self.tree_1 = ttk.Treeview(self.vista_1)
            self.tree_1.grid(row=1, column=0, columnspan=2)

            self.tree_1["columns"] = (
                "col1",
                "col2",
                "col3",
                "col4",
                "col5",
                "col6",
                "col7",
                "col8",
                "col9",
                "col10",
                "col11",
                "col12",
                "col13",
            )
            self.tree_1.column("#0", width=10, minwidth=50, anchor="center")
            self.tree_1.column("col1", width=80, minwidth=50, anchor="center")
            self.tree_1.column("col2", width=80, minwidth=50, anchor="center")
            self.tree_1.column("col3", width=80, minwidth=50, anchor="center")
            self.tree_1.column("col4", width=120, minwidth=50, anchor="center")
            self.tree_1.column("col5", width=120, minwidth=50, anchor="center")
            self.tree_1.column("col6", width=120, minwidth=50, anchor="center")
            self.tree_1.column("col7", width=120, minwidth=50, anchor="center")
            self.tree_1.column("col8", width=120, minwidth=50, anchor="center")
            self.tree_1.column("col9", width=120, minwidth=50, anchor="center")
            self.tree_1.column("col10", width=80, minwidth=50, anchor="center")
            self.tree_1.column("col11", width=80, minwidth=50, anchor="center")
            self.tree_1.column("col12", width=85, minwidth=50, anchor="center")
            self.tree_1.column("col13", width=105, minwidth=50, anchor="center")

            self.tree_1.heading("#0", text="Status")
            self.tree_1.heading("col1", text="Operation")
            self.tree_1.heading("col2", text="Date a-m-d")
            self.tree_1.heading("col3", text="Time")
            self.tree_1.heading("col4", text="Target Calc. L1 [ms]")
            self.tree_1.heading("col5", text="Target Calc. L2 [ms]")
            self.tree_1.heading("col6", text="Target Calc. L3 [ms]")
            self.tree_1.heading("col7", text="Target Exp. L1 [ms]")
            self.tree_1.heading("col8", text="Target Exp. L2 [ms]")
            self.tree_1.heading("col9", text="Target Exp. L3 [ms]")
            self.tree_1.heading("col10", text="Dif. L1 [ms]")
            self.tree_1.heading("col11", text="Dif. L2 [ms]")
            self.tree_1.heading("col12", text="Dif. L3 [ms]")
            self.tree_1.heading("col13", text="Tol. [ms]")

            # INSERTAR DATOS EN EL TREEVIEW
            obj_config.diagnostico_target_funcionamiento(
                self.tree_1,
                obj_rph2.rph2_close_date.rph2_data,
                obj_rph2.rph2_open_date.rph2_data,
                obj_config.programa_de_maniobra,
                obj_rph2.neutro_carga,
            )
            # -----------------------------------------------------------------------

        def objeto_configuracion():
            global obj_config
            obj_config = AbriArchivoConfiguracion()
            mostrar_diagnostico_1(obj_config)
            mostrar_diagnostico_2(obj_config)
            mostrar_diagnostico_3(obj_config)

            return obj_config

        abrir.add_command(
            label="File.RPH (diagnosis)", command=lambda: objeto_configuracion()
        )

        # --VENTANA DE DIAGNOSTICO_2
        self.diagnostico_2 = customtkinter.CTkFrame(self.pestaña_diagnostico_2)
        self.diagnostico_2.grid(row=4, column=0, padx=5, pady=15)

        # --INFORMACION DE DIAGNOSTICO
        def mostrar_diagnostico_2(obj_config):

            # TITULO: DATOS DEL INTERRUPTOR
            customtkinter.CTkLabel(
                self.diagnostico_2,
                text="Circuit Breaker Data",
            ).grid(row=0, column=0, columnspan=2)

            #       AJUSTE DE TIEMPOS CIERRE
            customtkinter.CTkLabel(
                self.diagnostico_2,
                text="\tCLOSING TIMES L1-L2-L3 [ms]: ",
            ).grid(row=1, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_2,
                text=str(obj_config.tiempo_config_l1_ch1)
                + " - "
                + str(obj_config.tiempo_config_l2_ch1)
                + " - "
                + str(obj_config.tiempo_config_l3_ch1),
            ).grid(row=1, column=1)

            #       AJUSTE DE TIEMPOS APERTURA
            customtkinter.CTkLabel(
                self.diagnostico_2,
                text="\tOPENING TIMES L1-L2-L3 [ms]: ",
            ).grid(row=2, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_2,
                text=str(obj_config.tiempo_config_l1_ch2)
                + " - "
                + str(obj_config.tiempo_config_l2_ch2)
                + " - "
                + str(obj_config.tiempo_config_l3_ch2),
            ).grid(row=2, column=1)

            # ----------VISUALIZACIÓN DE DATOS------------------------------

            self.vista_2 = customtkinter.CTkFrame(self.diagnostico_2)

            customtkinter.CTkLabel(
                self.vista_2,
                text="LAST OPERATIONS",
            ).grid(row=0, column=0, sticky="ew", columnspan=2)

            self.vista_2.grid(row=13, columnspan=2)

            self.tree_2 = ttk.Treeview(self.vista_2)
            self.tree_2.grid(row=1, column=0, columnspan=2)

            self.tree_2["columns"] = (
                "col1",
                "col2",
                "col3",
                "col4",
                "col5",
                "col6",
                "col7",
                "col8",
                "col9",
                "col10",
                "col11",
                "col12",
            )
            self.tree_2.column(
                "#0", width=10, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col1", width=80, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col2", width=80, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col3", width=80, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col4", width=100, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col5", width=100, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col6", width=100, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col7", width=100, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col8", width=100, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col9", width=100, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col10", width=150, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col11", width=150, minwidth=50, anchor="center", stretch=True
            )
            self.tree_2.column(
                "col12", width=150, minwidth=50, anchor="center", stretch=True
            )

            self.tree_2.heading("#0", text="Status")
            self.tree_2.heading("col1", text="Operation")
            self.tree_2.heading("col2", text="Date a-m-d")
            self.tree_2.heading("col3", text="Time")
            self.tree_2.heading("col4", text="Voltage [V]")
            self.tree_2.heading("col5", text="Temp. [°C]")
            self.tree_2.heading("col6", text="Freq. [Hz]")
            self.tree_2.heading("col7", text="Adap. L1 [ms]")
            self.tree_2.heading("col8", text="Adap. L2 [ms]")
            self.tree_2.heading("col9", text="Adap. L3 [ms]")
            self.tree_2.heading("col10", text="Time Meas. L1 [ms]")
            self.tree_2.heading("col11", text="Time Meas. L2 [ms]")
            self.tree_2.heading("col12", text="Time Meas. L3 [ms]")

            # INSERTAR DATOS EN EL TREEVIEW
            obj_config.diagnostico_control_adaptable(
                self.tree_2,
                obj_rph2.rph2_close_date.rph2_data,
                obj_rph2.rph2_open_date.rph2_data,
            )
            # -----------------------------------------------------------------------

        # --VENTANA DE DIAGNOSTICO_3
        self.diagnostico_3 = customtkinter.CTkFrame(
            self.pestaña_diagnostico_3,
        )
        self.diagnostico_3.grid(row=4, column=0, padx=5, pady=15)

        # --INFORMACION DE DIAGNOSTICO
        def mostrar_diagnostico_3(obj_config):

            # TITULO: CONFIGURACION DE ALARMAS
            customtkinter.CTkLabel(
                self.diagnostico_3,
                text="Alarms configuration",
            ).grid(row=0, column=0, columnspan=2)

            #       ALARMA_1
            customtkinter.CTkLabel(
                self.diagnostico_3,
                text="\tALARM 1: ",
            ).grid(row=1, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_3,
                text=str(obj_config.alarma_1),
            ).grid(row=1, column=1)

            #       ALARMA_2
            customtkinter.CTkLabel(
                self.diagnostico_3,
                text="\tALARM 2: ",
            ).grid(row=2, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_3,
                text=str(obj_config.alarma_2),
            ).grid(row=2, column=1)

            #       ALARMA_3
            customtkinter.CTkLabel(
                self.diagnostico_3,
                text="\tALARM 3: ",
            ).grid(row=3, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_3,
                text=str(obj_config.alarma_3),
            ).grid(row=3, column=1)

            #       ALARMA_4
            customtkinter.CTkLabel(
                self.diagnostico_3,
                text="\tALARM 4: ",
            ).grid(row=4, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_3,
                text=str(obj_config.alarma_4),
            ).grid(row=4, column=1)

            #       ALARMA_5
            customtkinter.CTkLabel(
                self.diagnostico_3,
                text="\tALARM 5: ",
            ).grid(row=5, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_3,
                text=str(obj_config.alarma_5),
            ).grid(row=5, column=1)

            #       ALARMA_6
            customtkinter.CTkLabel(
                self.diagnostico_3,
                text="\tALARM 6: ",
            ).grid(row=6, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_3,
                text=str(obj_config.alarma_6),
            ).grid(row=6, column=1)

            #       ALARMA_7
            customtkinter.CTkLabel(
                self.diagnostico_3,
                text="\tALARM 7: ",
            ).grid(row=7, column=0)

            customtkinter.CTkLabel(
                self.diagnostico_3,
                text=str(obj_config.alarma_7),
            ).grid(row=7, column=1)

            # ----------VISUALIZACIÓN DE DATOS------------------------------

            self.vista_3 = customtkinter.CTkFrame(self.diagnostico_3)

            customtkinter.CTkLabel(
                self.vista_3,
                text="DISPLAY OF ALARMS",
            ).grid(row=0, column=0, sticky="ew")

            self.vista_3.grid(row=13, columnspan=2)

            self.tree_3 = ttk.Treeview(self.vista_3)
            self.tree_3.grid(row=1, column=0)
            self.scrollvertical = customtkinter.CTkScrollbar(
                self.vista_3, command=self.tree_3.yview
            )
            self.scrollvertical.grid(row=1, column=1, sticky="nsew")
            self.tree_3.config(yscrollcommand=self.scrollvertical.set)

            self.tree_3["columns"] = (
                "col1",
                "col2",
                "col3",
                "col4",
                "col5",
            )
            self.tree_3.column("#0", width=1, minwidth=1, anchor="center")
            self.tree_3.column("col1", width=80, minwidth=50, anchor="center")
            self.tree_3.column("col2", width=80, minwidth=50, anchor="center")
            self.tree_3.column("col3", width=200, minwidth=50, anchor="center")
            self.tree_3.column("col4", width=200, minwidth=50, anchor="center")
            self.tree_3.column("col5", width=200, minwidth=50, anchor="center")

            self.tree_3.heading("#0", text="")
            self.tree_3.heading("col1", text="Alarm")
            self.tree_3.heading("col2", text="Operation")
            self.tree_3.heading("col3", text="Number of appearances")
            self.tree_3.heading("col4", text="Last alarm date")
            self.tree_3.heading("col5", text="Last alarm time")

            # INSERTAR DATOS EN EL TREEVIEW
            obj_config.diagnostico_alarmas(
                self.tree_3,
                obj_rph2.rph2_close_date.rph2_data,
                obj_rph2.rph2_open_date.rph2_data,
            )
            # -----------------------------------------------------------------------

        self.raiz.mainloop()
