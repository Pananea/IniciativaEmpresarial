
class RegisterScreen(PantallaBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Fondo(color=(1, 0.97, 0.9, 1)))

        card = MDCard(
            orientation="vertical",
            padding=40,
            spacing=20,
            size_hint=(0.9, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            elevation=8,
            radius=[25]
        )
        card.md_bg_color = (1, 1, 1, 1)

        card.add_widget(MDLabel(
            text="📝 Registro",
            halign="center",
            font_style="H5"
        ))

        self.nombre = MDTextField(
            hint_text="Nombre completo",
            mode="rectangle",
            size_hint_x=0.85,
            pos_hint={"center_x": 0.5},
        )
        card.add_widget(self.nombre)

        self.usuario = MDTextField(
            hint_text="Nombre de usuario",
            mode="rectangle",
            size_hint_x=0.85,
            pos_hint={"center_x": 0.5},
        )
        card.add_widget(self.usuario)

        self.correo = MDTextField(
            hint_text="Correo electrónico",
            mode="rectangle",
            size_hint_x=0.85,
            pos_hint={"center_x": 0.5},
        )
        card.add_widget(self.correo)

        self.contra = MDTextField(
            hint_text="Contraseña",
            mode="rectangle",
            password=True,
            size_hint_x=0.85,
            pos_hint={"center_x": 0.5},
        )
        card.add_widget(self.contra)

        card.add_widget(MDButton(
            MDButtonText(text="Registrar"),
            style="filled",
            md_bg_color=(1, 0.6, 0.4, 1),
            on_release=lambda x: self.registrar()
        ))

        # Volver
        card.add_widget(MDButton(
            MDButtonText(text="⬅ Volver"),
            style="outlined",
            on_release=lambda x: self.volver()
        ))

        self.add_widget(card)

    def registrar(self):
        if (self.nombre.text == "" or
            self.usuario.text == "" or
            self.correo.text == "" or
            self.contra.text == ""):

            self.mostrar_alerta("❌ Todos los campos son obligatorios.")
        else:
            self.mostrar_alerta("✔ Registro exitoso.")

    def volver(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login"

    def mostrar_alerta(self, mensaje):
        dialog = MDDialog(
            title="Mensaje",
            text=mensaje,
            buttons=[
                MDButton(MDButtonText(text="OK"),
                         on_release=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()
