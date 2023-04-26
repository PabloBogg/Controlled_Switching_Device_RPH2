class DiagnosticoAlarmas:
    def diagnostico_alarmas(
        self,
        tree,
        rph2_close,
        rph2_open,
    ):  # ALARMAS

        # CANTIDAD
        def contador_de_alarmas(n_alarma, data):
            contador = 0
            if n_alarma == "1":
                posicion = 0
            elif n_alarma == "2":
                posicion = 2
            elif n_alarma == "3":
                posicion = 4
            elif n_alarma == "4":
                posicion = 6
            elif n_alarma == "5":
                posicion = 8
            elif n_alarma == "6":
                posicion = 10
            elif n_alarma == "7":
                posicion = 12

            for x in data.index:
                if str(data["Alarm"][x])[posicion] == "1":
                    contador += 1
                    if contador == 1:
                        fecha_ultima_al = data["Date"][x]
                        hora_ultima_al = data["Time"][x]
                if contador == 0:
                    fecha_ultima_al = "No record"
                    hora_ultima_al = "No record"
            return [contador, fecha_ultima_al, hora_ultima_al]

        (
            cantidad_al_1_close,
            fecha_ultima_al_1_close,
            hora_ultima_al_1_close,
        ) = contador_de_alarmas("1", rph2_close)
        (
            cantidad_al_2_close,
            fecha_ultima_al_2_close,
            hora_ultima_al_2_close,
        ) = contador_de_alarmas("2", rph2_close)
        (
            cantidad_al_3_close,
            fecha_ultima_al_3_close,
            hora_ultima_al_3_close,
        ) = contador_de_alarmas("3", rph2_close)
        (
            cantidad_al_4_close,
            fecha_ultima_al_4_close,
            hora_ultima_al_4_close,
        ) = contador_de_alarmas("4", rph2_close)
        (
            cantidad_al_5_close,
            fecha_ultima_al_5_close,
            hora_ultima_al_5_close,
        ) = contador_de_alarmas("5", rph2_close)
        (
            cantidad_al_6_close,
            fecha_ultima_al_6_close,
            hora_ultima_al_6_close,
        ) = contador_de_alarmas("6", rph2_close)
        (
            cantidad_al_7_close,
            fecha_ultima_al_7_close,
            hora_ultima_al_7_close,
        ) = contador_de_alarmas("7", rph2_close)

        (
            cantidad_al_1_open,
            fecha_ultima_al_1_open,
            hora_ultima_al_1_open,
        ) = contador_de_alarmas("1", rph2_open)
        (
            cantidad_al_2_open,
            fecha_ultima_al_2_open,
            hora_ultima_al_2_open,
        ) = contador_de_alarmas("2", rph2_open)
        (
            cantidad_al_3_open,
            fecha_ultima_al_3_open,
            hora_ultima_al_3_open,
        ) = contador_de_alarmas("3", rph2_open)
        (
            cantidad_al_4_open,
            fecha_ultima_al_4_open,
            hora_ultima_al_4_open,
        ) = contador_de_alarmas("4", rph2_open)
        (
            cantidad_al_5_open,
            fecha_ultima_al_5_open,
            hora_ultima_al_5_open,
        ) = contador_de_alarmas("5", rph2_open)
        (
            cantidad_al_6_open,
            fecha_ultima_al_6_open,
            hora_ultima_al_6_open,
        ) = contador_de_alarmas("6", rph2_open)
        (
            cantidad_al_7_open,
            fecha_ultima_al_7_open,
            hora_ultima_al_7_open,
        ) = contador_de_alarmas("7", rph2_open)

        # ULTIMA FECHA

        datos = [
            [
                "",
                "ALARM 7",
                "CLOSING",
                cantidad_al_7_close,
                fecha_ultima_al_7_close,
                hora_ultima_al_7_close,
            ],
            [
                "",
                "ALARM 6",
                "CLOSING",
                cantidad_al_6_close,
                fecha_ultima_al_6_close,
                hora_ultima_al_6_close,
            ],
            [
                "",
                "ALARM 5",
                "CLOSING",
                cantidad_al_5_close,
                fecha_ultima_al_5_close,
                hora_ultima_al_5_close,
            ],
            [
                "",
                "ALARM 4",
                "CLOSING",
                cantidad_al_4_close,
                fecha_ultima_al_4_close,
                hora_ultima_al_4_close,
            ],
            [
                "",
                "ALARM 3",
                "CLOSING",
                cantidad_al_3_close,
                fecha_ultima_al_3_close,
                hora_ultima_al_3_close,
            ],
            [
                "",
                "ALARM 2",
                "CLOSING",
                cantidad_al_2_close,
                fecha_ultima_al_2_close,
                hora_ultima_al_2_close,
            ],
            [
                "",
                "ALARM 1",
                "CLOSING",
                cantidad_al_1_close,
                fecha_ultima_al_1_close,
                hora_ultima_al_1_close,
            ],
            [
                "",
                "ALARM 7",
                "OPENING",
                cantidad_al_7_open,
                fecha_ultima_al_7_open,
                hora_ultima_al_7_open,
            ],
            [
                "",
                "ALARM 6",
                "OPENING",
                cantidad_al_6_open,
                fecha_ultima_al_6_open,
                hora_ultima_al_6_open,
            ],
            [
                "",
                "ALARM 5",
                "OPENING",
                cantidad_al_5_open,
                fecha_ultima_al_5_open,
                hora_ultima_al_5_open,
            ],
            [
                "",
                "ALARM 4",
                "OPENING",
                cantidad_al_4_open,
                fecha_ultima_al_4_open,
                hora_ultima_al_4_open,
            ],
            [
                "",
                "ALARM 3",
                "OPENING",
                cantidad_al_3_open,
                fecha_ultima_al_3_open,
                hora_ultima_al_3_open,
            ],
            [
                "",
                "ALARM 2",
                "OPENING",
                cantidad_al_2_open,
                fecha_ultima_al_2_open,
                hora_ultima_al_2_open,
            ],
            [
                "",
                "ALARM 1",
                "OPENING",
                cantidad_al_1_open,
                fecha_ultima_al_1_open,
                hora_ultima_al_1_open,
            ],
        ]

        # ESTADO

        # INSERTAR DATOS EN EL TREEVIEW
        for element in datos:
            tree.insert(
                "",
                0,
                text=element[0],
                values=(element[1:]),
            )
