class DiagnosticoControlAdaptable:
    def diagnostico_control_adaptable(
        self,
        tree,
        rph2_close,
        rph2_open,
    ):  # ULTIMAS MANIOBRAS

        # FECHA
        fecha_close_1 = list(rph2_close["Date"])[0]  # ULTIMA FECHA
        fecha_close_2 = list(rph2_close["Date"])[1]
        fecha_close_3 = list(rph2_close["Date"])[2]
        fecha_close_4 = list(rph2_close["Date"])[3]
        fecha_open_1 = list(rph2_open["Date"])[0]  # ULTIMA FECHA
        fecha_open_2 = list(rph2_open["Date"])[1]
        fecha_open_3 = list(rph2_open["Date"])[2]
        fecha_open_4 = list(rph2_open["Date"])[3]

        # HORA
        hora_close_1 = list(rph2_close["Time"])[0]  # ULTIMA FECHA
        hora_close_2 = list(rph2_close["Time"])[1]
        hora_close_3 = list(rph2_close["Time"])[2]
        hora_close_4 = list(rph2_close["Time"])[3]
        hora_open_1 = list(rph2_open["Time"])[0]  # ULTIMA FECHA
        hora_open_2 = list(rph2_open["Time"])[1]
        hora_open_3 = list(rph2_open["Time"])[2]
        hora_open_4 = list(rph2_open["Time"])[3]

        # TENSION
        tension_close_1 = list(rph2_close["Voltage"])[0]  # ULTIMA FECHA
        tension_close_2 = list(rph2_close["Voltage"])[1]
        tension_close_3 = list(rph2_close["Voltage"])[2]
        tension_close_4 = list(rph2_close["Voltage"])[3]
        tension_open_1 = list(rph2_open["Voltage"])[0]  # ULTIMA FECHA
        tension_open_2 = list(rph2_open["Voltage"])[1]
        tension_open_3 = list(rph2_open["Voltage"])[2]
        tension_open_4 = list(rph2_open["Voltage"])[3]

        # TEMPERATURA
        temp_close_1 = list(rph2_close["Temp."])[0]  # ULTIMA FECHA
        temp_close_2 = list(rph2_close["Temp."])[1]
        temp_close_3 = list(rph2_close["Temp."])[2]
        temp_close_4 = list(rph2_close["Temp."])[3]
        temp_open_1 = list(rph2_open["Temp."])[0]  # ULTIMA FECHA
        temp_open_2 = list(rph2_open["Temp."])[1]
        temp_open_3 = list(rph2_open["Temp."])[2]
        temp_open_4 = list(rph2_open["Temp."])[3]

        # FRECUENCIA
        feq_close_1 = list(rph2_close["Frequency"])[0]  # ULTIMA FECHA
        feq_close_2 = list(rph2_close["Frequency"])[1]
        feq_close_3 = list(rph2_close["Frequency"])[2]
        feq_close_4 = list(rph2_close["Frequency"])[3]
        feq_open_1 = list(rph2_open["Frequency"])[0]  # ULTIMA FECHA
        feq_open_2 = list(rph2_open["Frequency"])[1]
        feq_open_3 = list(rph2_open["Frequency"])[2]
        feq_open_4 = list(rph2_open["Frequency"])[3]

        # ADAPTATIVO
        adp_close_1_l1 = list(rph2_close["Adaptiv_L1"])[0]  # ULTIMA FECHA
        adp_close_1_l2 = list(rph2_close["Adaptiv_L2"])[0]  # ULTIMA FECHA
        adp_close_1_l3 = list(rph2_close["Adaptiv_L3"])[0]  # ULTIMA FECHA

        adp_close_2_l1 = list(rph2_close["Adaptiv_L1"])[1]
        adp_close_2_l2 = list(rph2_close["Adaptiv_L2"])[1]
        adp_close_2_l3 = list(rph2_close["Adaptiv_L3"])[1]

        adp_close_3_l1 = list(rph2_close["Adaptiv_L1"])[2]
        adp_close_3_l2 = list(rph2_close["Adaptiv_L2"])[2]
        adp_close_3_l3 = list(rph2_close["Adaptiv_L3"])[2]

        adp_close_4_l1 = list(rph2_close["Adaptiv_L1"])[3]
        adp_close_4_l2 = list(rph2_close["Adaptiv_L2"])[3]
        adp_close_4_l3 = list(rph2_close["Adaptiv_L3"])[3]

        adp_open_1_l1 = list(rph2_open["Adaptiv_L1"])[0]  # ULTIMA FECHA
        adp_open_1_l2 = list(rph2_open["Adaptiv_L2"])[0]  # ULTIMA FECHA
        adp_open_1_l3 = list(rph2_open["Adaptiv_L3"])[0]  # ULTIMA FECHA

        adp_open_2_l1 = list(rph2_open["Adaptiv_L1"])[1]
        adp_open_2_l2 = list(rph2_open["Adaptiv_L2"])[1]
        adp_open_2_l3 = list(rph2_open["Adaptiv_L3"])[1]

        adp_open_3_l1 = list(rph2_open["Adaptiv_L1"])[2]
        adp_open_3_l2 = list(rph2_open["Adaptiv_L2"])[2]
        adp_open_3_l3 = list(rph2_open["Adaptiv_L3"])[2]

        adp_open_4_l1 = list(rph2_open["Adaptiv_L1"])[3]
        adp_open_4_l2 = list(rph2_open["Adaptiv_L2"])[3]
        adp_open_4_l3 = list(rph2_open["Adaptiv_L3"])[3]

        # TIEMPO MEDIDO
        tm_close_1_l1 = list(rph2_close["Meas.Op.Time_L1"])[0]  # ULTIMA FECHA
        tm_close_1_l2 = list(rph2_close["Meas.Op.Time_L2"])[0]  # ULTIMA FECHA
        tm_close_1_l3 = list(rph2_close["Meas.Op.Time_L3"])[0]  # ULTIMA FECHA

        tm_close_2_l1 = list(rph2_close["Meas.Op.Time_L1"])[1]
        tm_close_2_l2 = list(rph2_close["Meas.Op.Time_L2"])[1]
        tm_close_2_l3 = list(rph2_close["Meas.Op.Time_L3"])[1]

        tm_close_3_l1 = list(rph2_close["Meas.Op.Time_L1"])[2]
        tm_close_3_l2 = list(rph2_close["Meas.Op.Time_L2"])[2]
        tm_close_3_l3 = list(rph2_close["Meas.Op.Time_L3"])[2]

        tm_close_4_l1 = list(rph2_close["Meas.Op.Time_L1"])[3]
        tm_close_4_l2 = list(rph2_close["Meas.Op.Time_L2"])[3]
        tm_close_4_l3 = list(rph2_close["Meas.Op.Time_L3"])[3]

        tm_open_1_l1 = list(rph2_open["Meas.Op.Time_L1"])[0]  # ULTIMA FECHA
        tm_open_1_l2 = list(rph2_open["Meas.Op.Time_L2"])[0]  # ULTIMA FECHA
        tm_open_1_l3 = list(rph2_open["Meas.Op.Time_L3"])[0]  # ULTIMA FECHA

        tm_open_2_l1 = list(rph2_open["Meas.Op.Time_L1"])[1]
        tm_open_2_l2 = list(rph2_open["Meas.Op.Time_L2"])[1]
        tm_open_2_l3 = list(rph2_open["Meas.Op.Time_L3"])[1]

        tm_open_3_l1 = list(rph2_open["Meas.Op.Time_L1"])[2]
        tm_open_3_l2 = list(rph2_open["Meas.Op.Time_L2"])[2]
        tm_open_3_l3 = list(rph2_open["Meas.Op.Time_L3"])[2]

        tm_open_4_l1 = list(rph2_open["Meas.Op.Time_L1"])[3]
        tm_open_4_l2 = list(rph2_open["Meas.Op.Time_L2"])[3]
        tm_open_4_l3 = list(rph2_open["Meas.Op.Time_L3"])[3]

        datos = [
            [
                "",
                "Closing",
                fecha_close_1,
                hora_close_1,
                tension_close_1,
                temp_close_1,
                feq_close_1,
                adp_close_1_l1,
                adp_close_1_l2,
                adp_close_1_l3,
                tm_close_1_l1,
                tm_close_1_l2,
                tm_close_1_l3,
            ],
            [
                "",
                "Closing",
                fecha_close_2,
                hora_close_2,
                tension_close_2,
                temp_close_2,
                feq_close_2,
                adp_close_2_l1,
                adp_close_2_l2,
                adp_close_2_l3,
                tm_close_2_l1,
                tm_close_2_l2,
                tm_close_2_l3,
            ],
            [
                "",
                "Closing",
                fecha_close_3,
                hora_close_3,
                tension_close_3,
                temp_close_3,
                feq_close_3,
                adp_close_3_l1,
                adp_close_3_l2,
                adp_close_3_l3,
                tm_close_3_l1,
                tm_close_3_l2,
                tm_close_3_l3,
            ],
            [
                "",
                "Closing",
                fecha_close_4,
                hora_close_4,
                tension_close_4,
                temp_close_4,
                feq_close_4,
                adp_close_4_l1,
                adp_close_4_l2,
                adp_close_4_l3,
                tm_close_4_l1,
                tm_close_4_l2,
                tm_close_4_l3,
            ],
            [
                "",
                "Opening",
                fecha_open_1,
                hora_open_1,
                tension_open_1,
                temp_open_1,
                feq_open_1,
                adp_open_1_l1,
                adp_open_1_l2,
                adp_open_1_l3,
                tm_open_1_l1,
                tm_open_1_l2,
                tm_open_1_l3,
            ],
            [
                "",
                "Opening",
                fecha_open_2,
                hora_open_2,
                tension_open_2,
                temp_open_2,
                feq_open_2,
                adp_open_2_l1,
                adp_open_2_l2,
                adp_open_2_l3,
                tm_open_2_l1,
                tm_open_2_l2,
                tm_open_2_l3,
            ],
            [
                "",
                "Opening",
                fecha_open_3,
                hora_open_3,
                tension_open_3,
                temp_open_3,
                feq_open_3,
                adp_open_3_l1,
                adp_open_3_l2,
                adp_open_3_l3,
                tm_open_3_l1,
                tm_open_3_l2,
                tm_open_3_l3,
            ],
            [
                "",
                "Opening",
                fecha_open_4,
                hora_open_4,
                tension_open_4,
                temp_open_4,
                feq_open_4,
                adp_open_4_l1,
                adp_open_4_l2,
                adp_open_4_l3,
                tm_open_4_l1,
                tm_open_4_l2,
                tm_open_4_l3,
            ],
        ]

        # ESTADO
        for x in range(8):
            if datos[x][1] == "Closing":
                if (
                    abs(datos[x][7]) > 10
                    or abs(datos[x][8]) > 10
                    or abs(datos[x][9]) > 10
                ):
                    datos[x][0] = "BAD"
                else:
                    datos[x][0] = "OK"
            elif datos[x][1] == "Opening":
                if abs(datos[x][7]) > 5 or abs(datos[x][8]) > 5 or abs(datos[x][9]) > 5:
                    datos[x][0] = "BAD"
                else:
                    datos[x][0] = "OK"

        # INSERTAR DATOS EN EL TREEVIEW
        for element in datos:
            tree.insert(
                "",
                0,
                text=element[0],
                values=(element[1:]),
            )
