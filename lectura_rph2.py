import pandas as pd

# LECTURA
class Lectura_rph2:
    def __init__(self, filename):

        # --LECTURA DE ARCHIVO .CSV
        rph2_data = pd.read_csv(filename, sep=";", header=[1])
        columns = [
            "ArchiveRecord",
            "Date",
            "Time",
            "Direction",
            "Neutral",
            "Sw.Program",
            "Comp.Voltage",
            "Comp.Pressure",
            "Comp.Temp.",
            "Comm.OutTime_L1",
            "Comm.OutTime_L2",
            "Comm.OutTime_L3",
            "Calc.Op.Time_L1",
            "Calc.Op.Time_L2",
            "Calc.Op.Time_L3",
            "Meas.Op.Time_L1",
            "Meas.Op.Time_L2",
            "Meas.Op.Time_L3",
            "Current max._L1",
            "Current max._L2",
            "Current max._L3",
            "Voltage",
            "Temp.",
            "Pressure_L1",
            "Pressure_L2",
            "Pressure_L3",
            "Frequency",
            "Alarm",
            "CS-Error",
            "Invalid",
            "Status",
            "Adaptiv_L1",
            "Adaptiv_L2",
            "Adaptiv_L3",
        ]
        try:
            rph2_data.columns = columns
        except:
            pass
        rph2_data = rph2_data.drop(0)
        for x in columns:
            try:
                rph2_data[x] = rph2_data[x].astype(float)
            except:
                pass

        # SE DEVUELVE EL DATAFRAME PARA ANALIZAR
        self.data = rph2_data
