class DiagnosticoTargetFuncionamiento:
    def diagnostico_target_funcionamiento(
        self, tree, rph2_close, rph2_open, programa_de_maniobra, neutro_carga
    ):  # TARGET DE FUNCIONAMIENTO

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

        # TARGET CALCULADO
        target_l1_close_1 = round(
            (
                (list(rph2_close["Comm.OutTime_L1"])[0])
                + (list(rph2_close["Meas.Op.Time_L1"])[0])
                - self.tiempo_arc_l1_ch1
            )
            % 20,
            2,
        )
        target_l2_close_1 = round(
            (
                (list(rph2_close["Comm.OutTime_L2"])[0])
                + (list(rph2_close["Meas.Op.Time_L2"])[0])
                - self.tiempo_arc_l2_ch1
            )
            % 20,
            2,
        )
        target_l3_close_1 = round(
            (
                (list(rph2_close["Comm.OutTime_L3"])[0])
                + (list(rph2_close["Meas.Op.Time_L3"])[0])
                - self.tiempo_arc_l3_ch1
            )
            % 20,
            2,
        )

        target_l1_close_2 = round(
            (
                (list(rph2_close["Comm.OutTime_L1"])[1])
                + (list(rph2_close["Meas.Op.Time_L1"])[1])
                - self.tiempo_arc_l1_ch1
            )
            % 20,
            2,
        )
        target_l2_close_2 = round(
            (
                (list(rph2_close["Comm.OutTime_L2"])[1])
                + (list(rph2_close["Meas.Op.Time_L2"])[1])
                - self.tiempo_arc_l2_ch1
            )
            % 20,
            2,
        )
        target_l3_close_2 = round(
            (
                (list(rph2_close["Comm.OutTime_L3"])[1])
                + (list(rph2_close["Meas.Op.Time_L3"])[1])
                - self.tiempo_arc_l3_ch1
            )
            % 20,
            2,
        )

        target_l1_close_3 = round(
            (
                (list(rph2_close["Comm.OutTime_L1"])[2])
                + (list(rph2_close["Meas.Op.Time_L1"])[2])
                - self.tiempo_arc_l1_ch1
            )
            % 20,
            2,
        )
        target_l2_close_3 = round(
            (
                (list(rph2_close["Comm.OutTime_L2"])[2])
                + (list(rph2_close["Meas.Op.Time_L2"])[2])
                - self.tiempo_arc_l2_ch1
            )
            % 20,
            2,
        )
        target_l3_close_3 = round(
            (
                (list(rph2_close["Comm.OutTime_L3"])[2])
                + (list(rph2_close["Meas.Op.Time_L3"])[2])
                - self.tiempo_arc_l3_ch1
            )
            % 20,
            2,
        )

        target_l1_close_4 = round(
            (
                (list(rph2_close["Comm.OutTime_L1"])[3])
                + (list(rph2_close["Meas.Op.Time_L1"])[3])
                - self.tiempo_arc_l1_ch1
            )
            % 20,
            2,
        )
        target_l2_close_4 = round(
            (
                (list(rph2_close["Comm.OutTime_L2"])[3])
                + (list(rph2_close["Meas.Op.Time_L2"])[3])
                - self.tiempo_arc_l2_ch1
            )
            % 20,
            2,
        )
        target_l3_close_4 = round(
            (
                (list(rph2_close["Comm.OutTime_L3"])[3])
                + (list(rph2_close["Meas.Op.Time_L3"])[3])
                - self.tiempo_arc_l3_ch1
            )
            % 20,
            2,
        )

        target_l1_open_1 = round(
            (
                (list(rph2_open["Comm.OutTime_L1"])[0])
                + (list(rph2_open["Meas.Op.Time_L1"])[0])
                + self.tiempo_arc_l1_ch2
            )
            % 20,
            2,
        )
        target_l2_open_1 = round(
            (
                (list(rph2_open["Comm.OutTime_L2"])[0])
                + (list(rph2_open["Meas.Op.Time_L2"])[0])
                + self.tiempo_arc_l2_ch2
            )
            % 20,
            2,
        )
        target_l3_open_1 = round(
            (
                (list(rph2_open["Comm.OutTime_L3"])[0])
                + (list(rph2_open["Meas.Op.Time_L3"])[0])
                + self.tiempo_arc_l3_ch2
            )
            % 20,
            2,
        )

        target_l1_open_2 = round(
            (
                (list(rph2_open["Comm.OutTime_L1"])[1])
                + (list(rph2_open["Meas.Op.Time_L1"])[1])
                + self.tiempo_arc_l1_ch2
            )
            % 20,
            2,
        )
        target_l2_open_2 = round(
            (
                (list(rph2_open["Comm.OutTime_L2"])[1])
                + (list(rph2_open["Meas.Op.Time_L2"])[1])
                + self.tiempo_arc_l2_ch2
            )
            % 20,
            2,
        )
        target_l3_open_2 = round(
            (
                (list(rph2_open["Comm.OutTime_L3"])[1])
                + (list(rph2_open["Meas.Op.Time_L3"])[1])
                + self.tiempo_arc_l3_ch2
            )
            % 20,
            2,
        )

        target_l1_open_3 = round(
            (
                (list(rph2_open["Comm.OutTime_L1"])[2])
                + (list(rph2_open["Meas.Op.Time_L1"])[2])
                + self.tiempo_arc_l1_ch2
            )
            % 20,
            2,
        )
        target_l2_open_3 = round(
            (
                (list(rph2_open["Comm.OutTime_L2"])[2])
                + (list(rph2_open["Meas.Op.Time_L2"])[2])
                + self.tiempo_arc_l2_ch2
            )
            % 20,
            2,
        )
        target_l3_open_3 = round(
            (
                (list(rph2_open["Comm.OutTime_L3"])[2])
                + (list(rph2_open["Meas.Op.Time_L3"])[2])
                + self.tiempo_arc_l3_ch2
            )
            % 20,
            2,
        )

        target_l1_open_4 = round(
            (
                (list(rph2_open["Comm.OutTime_L1"])[3])
                + (list(rph2_open["Meas.Op.Time_L1"])[3])
                + self.tiempo_arc_l1_ch2
            )
            % 20,
            2,
        )
        target_l2_open_4 = round(
            (
                (list(rph2_open["Comm.OutTime_L2"])[3])
                + (list(rph2_open["Meas.Op.Time_L2"])[3])
                + self.tiempo_arc_l2_ch2
            )
            % 20,
            2,
        )
        target_l3_open_4 = round(
            (
                (list(rph2_open["Comm.OutTime_L3"])[3])
                + (list(rph2_open["Meas.Op.Time_L3"])[3])
                + self.tiempo_arc_l3_ch2
            )
            % 20,
            2,
        )

        # TARGET ESPERADO Y TOLERANCIA
        if str(programa_de_maniobra) == "TRANSFORMER":
            # TOLERANCIA
            tol_close = 2
            tol_open = 1.5
            if str(neutro_carga) == "Grounded":
                target_esperado_l1_close = 5
                target_esperado_l2_close = 10
                target_esperado_l3_close = 10
                target_esperado_l1_open = 5
                target_esperado_l2_open = 1.7
                target_esperado_l3_open = 8.3
            if str(neutro_carga) == "Isolated":
                target_esperado_l1_close = 5
                target_esperado_l2_close = 0
                target_esperado_l3_close = 0
                target_esperado_l1_open = 5
                target_esperado_l2_open = 10
                target_esperado_l3_open = 10
        elif str(programa_de_maniobra) == "SHUNTREACTOR":
            # TOLERANCIA
            tol_close = 2
            tol_open = 1.5
            if str(neutro_carga) == "Grounded":
                target_esperado_l1_close = 5
                target_esperado_l2_close = 1.7
                target_esperado_l3_close = 8.3
                target_esperado_l1_open = 5
                target_esperado_l2_open = 1.7
                target_esperado_l3_open = 8.3
            if str(neutro_carga) == "Isolated":
                target_esperado_l1_close = 5
                target_esperado_l2_close = 0
                target_esperado_l3_close = 0
                target_esperado_l1_open = 5
                target_esperado_l2_open = 10
                target_esperado_l3_open = 10
        elif str(programa_de_maniobra) == "CAPACITORBANK":
            # TOLERANCIA
            tol_close = 1
            tol_open = 1.5
            if str(neutro_carga) == "Grounded":
                target_esperado_l1_close = 0
                target_esperado_l2_close = 6.7
                target_esperado_l3_close = 3.3
                target_esperado_l1_open = 5
                target_esperado_l2_open = 1.7
                target_esperado_l3_open = 8.3
            if str(neutro_carga) == "Isolated":
                target_esperado_l1_close = 10
                target_esperado_l2_close = 5
                target_esperado_l3_close = 5
                target_esperado_l1_open = 5
                target_esperado_l2_open = 10
                target_esperado_l3_open = 10

        # DIFERENCIA
        def diferencia(n1, n2):
            return round(abs(n1 - n2), 1)

        dif_l1_close_1 = diferencia(target_esperado_l1_close, target_l1_close_1)
        dif_l2_close_1 = diferencia(target_esperado_l2_close, target_l2_close_1)
        dif_l3_close_1 = diferencia(target_esperado_l3_close, target_l3_close_1)

        dif_l1_close_2 = diferencia(target_esperado_l1_close, target_l1_close_2)
        dif_l2_close_2 = diferencia(target_esperado_l2_close, target_l2_close_2)
        dif_l3_close_2 = diferencia(target_esperado_l3_close, target_l3_close_2)

        dif_l1_close_3 = diferencia(target_esperado_l1_close, target_l1_close_3)
        dif_l2_close_3 = diferencia(target_esperado_l2_close, target_l2_close_3)
        dif_l3_close_3 = diferencia(target_esperado_l3_close, target_l3_close_3)

        dif_l1_close_4 = diferencia(target_esperado_l1_close, target_l1_close_4)
        dif_l2_close_4 = diferencia(target_esperado_l2_close, target_l2_close_4)
        dif_l3_close_4 = diferencia(target_esperado_l3_close, target_l3_close_4)

        dif_l1_open_1 = diferencia(target_esperado_l1_open, target_l1_open_1)
        dif_l2_open_1 = diferencia(target_esperado_l2_open, target_l2_open_1)
        dif_l3_open_1 = diferencia(target_esperado_l3_open, target_l3_open_1)

        dif_l1_open_2 = diferencia(target_esperado_l1_open, target_l1_open_2)
        dif_l2_open_2 = diferencia(target_esperado_l2_open, target_l2_open_2)
        dif_l3_open_2 = diferencia(target_esperado_l3_open, target_l3_open_2)

        dif_l1_open_3 = diferencia(target_esperado_l1_open, target_l1_open_3)
        dif_l2_open_3 = diferencia(target_esperado_l2_open, target_l2_open_3)
        dif_l3_open_3 = diferencia(target_esperado_l3_open, target_l3_open_3)

        dif_l1_open_4 = diferencia(target_esperado_l1_open, target_l1_open_4)
        dif_l2_open_4 = diferencia(target_esperado_l2_open, target_l2_open_4)
        dif_l3_open_4 = diferencia(target_esperado_l3_open, target_l3_open_4)

        datos = [
            [
                "",
                "Closing",
                fecha_close_1,
                hora_close_1,
                target_l1_close_1,
                target_l2_close_1,
                target_l3_close_1,
                target_esperado_l1_close,
                target_esperado_l2_close,
                target_esperado_l3_close,
                dif_l1_close_1,
                dif_l2_close_1,
                dif_l3_close_1,
                tol_close,
            ],
            [
                "",
                "Closing",
                fecha_close_2,
                hora_close_2,
                target_l1_close_2,
                target_l2_close_2,
                target_l3_close_2,
                target_esperado_l1_close,
                target_esperado_l2_close,
                target_esperado_l3_close,
                dif_l1_close_2,
                dif_l2_close_2,
                dif_l3_close_2,
                tol_close,
            ],
            [
                "",
                "Closing",
                fecha_close_3,
                hora_close_3,
                target_l1_close_3,
                target_l2_close_3,
                target_l3_close_3,
                target_esperado_l1_close,
                target_esperado_l2_close,
                target_esperado_l3_close,
                dif_l1_close_3,
                dif_l2_close_3,
                dif_l3_close_3,
                tol_close,
            ],
            [
                "",
                "Closing",
                fecha_close_4,
                hora_close_4,
                target_l1_close_4,
                target_l2_close_4,
                target_l3_close_4,
                target_esperado_l1_close,
                target_esperado_l2_close,
                target_esperado_l3_close,
                dif_l1_close_4,
                dif_l2_close_4,
                dif_l3_close_4,
                tol_close,
            ],
            [
                "",
                "Opening",
                fecha_open_1,
                hora_open_1,
                target_l1_open_1,
                target_l2_open_1,
                target_l3_open_1,
                target_esperado_l1_open,
                target_esperado_l2_open,
                target_esperado_l3_open,
                dif_l1_open_1,
                dif_l2_open_1,
                dif_l3_open_1,
                tol_open,
            ],
            [
                "",
                "Opening",
                fecha_open_2,
                hora_open_2,
                target_l1_open_2,
                target_l2_open_2,
                target_l3_open_2,
                target_esperado_l1_open,
                target_esperado_l2_open,
                target_esperado_l3_open,
                dif_l1_open_2,
                dif_l2_open_2,
                dif_l3_open_2,
                tol_open,
            ],
            [
                "",
                "Opening",
                fecha_open_3,
                hora_open_3,
                target_l1_open_3,
                target_l2_open_3,
                target_l3_open_3,
                target_esperado_l1_open,
                target_esperado_l2_open,
                target_esperado_l3_open,
                dif_l1_open_3,
                dif_l2_open_3,
                dif_l3_open_3,
                tol_open,
            ],
            [
                "",
                "Opening",
                fecha_open_4,
                hora_open_4,
                target_l1_open_4,
                target_l2_open_4,
                target_l3_open_4,
                target_esperado_l1_open,
                target_esperado_l2_open,
                target_esperado_l3_open,
                dif_l1_open_4,
                dif_l2_open_4,
                dif_l3_open_4,
                tol_open,
            ],
        ]

        # ESTADO
        for x in range(8):
            if (
                datos[x][10] > datos[x][13]
                and datos[x][11] > datos[x][13]
                and datos[x][11] > datos[x][13]
            ):
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
