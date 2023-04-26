from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# GRAFICOS
class Graficar_rph2:
    def __init__(self, t, rph2_data, l1, l2, frame, fase):
        """
        GENERA 2 GRAFICOS (y1 e y2) SUPERPUESTOS EN FUNCION DEL EJE X (x)
        EN EL FRAME (frame de tkinter), CON:
        - LEYENDA (l1,l2)
        - TITULO (t)
        - TITULO EJE X (tx)
        - TITULO EJE Y (ty)
        """

        def clear_frame(frame):
            for widgets in frame.winfo_children():
                widgets.destroy()

        clear_frame(frame)

        tx = "DateTime"
        ty = "Time [ms]"
        y1 = rph2_data["Meas.Op.Time_" + fase]
        y2 = rph2_data["Calc.Op.Time_" + fase]
        x = rph2_data["DateTime"]

        figure = Figure(figsize=(4.3, 5), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, frame)
        NavigationToolbar2Tk(figure_canvas, frame)
        axes = figure.add_subplot()
        axes.plot(
            x,
            y1,
            label=l1,
        )
        axes.plot(
            x,
            y2,
            label=l2,
        )
        # Configurar la rotación para el eje X a 90°
        axes.tick_params(axis="x", labelrotation=90)
        axes.legend()
        axes.set_title(t)
        axes.set_ylabel(ty)
        axes.set_xlabel(tx)
        # Configurar la vision completa de los datos de los ejes
        figure.set_tight_layout(True)
        figure_canvas.get_tk_widget().pack()
