from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.card import MDCard
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation


# ---------- Fondo personalizado ----------
class Fondo(Widget):
    def __init__(self, color=(0.9, 0.9, 1, 1), **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# ---------- Pantalla base con animación ----------
class PantallaBase(MDScreen):
    def on_enter(self, *args):
        # Animación de aparición para todos los elementos de la pantalla
        for child in self.children:
            anim = Animation(opacity=1, d=0.8, t="out_quad")
            child.opacity = 0
            anim.start(child)


# ---------- Pantalla de Menú ----------
class MenuScreen(PantallaBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Fondo(color=(0.95, 0.95, 1, 1)))

        card = MDCard(orientation="vertical", padding=40, spacing=25,
                      size_hint=(0.9, 0.7), pos_hint={"center_x": 0.5, "center_y": 0.5},
                      elevation=6, radius=[20])
        card.md_bg_color = (1, 1, 1, 1)

        card.add_widget(MDLabel(
            text="🧠 MiniMind",
            halign="center",
            font_style="H4",
            theme_text_color="Primary"
        ))
        card.add_widget(MDLabel(
            text="Entrena tu mente con diversión",
            halign="center",
            theme_text_color="Secondary"
        ))

        card.add_widget(MDRaisedButton(
            text="🧩 Puzzle Mental",
            md_bg_color=(0.6, 0.5, 1, 1),
            on_release=lambda x: self.cambiar_pantalla("puzzle")
        ))
        card.add_widget(MDRaisedButton(
            text="📝 Memoria Rápida",
            md_bg_color=(0.8, 0.4, 1, 1),
            on_release=lambda x: self.cambiar_pantalla("memoria")
        ))

        self.add_widget(card)

    def cambiar_pantalla(self, nombre_pantalla):
        self.manager.transition.direction = "left"
        self.manager.current = nombre_pantalla


# ---------- Pantalla de Puzzle ----------
class PuzzleScreen(PantallaBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Fondo(color=(0.9, 1, 0.95, 1)))

        card = MDCard(orientation="vertical", padding=40, spacing=25,
                      size_hint=(0.9, 0.6), pos_hint={"center_x": 0.5, "center_y": 0.5},
                      elevation=6, radius=[20])
        card.md_bg_color = (1, 1, 1, 1)

        card.add_widget(MDLabel(
            text="🧩 Puzzle Mental",
            halign="center",
            font_style="H5"
        ))
        card.add_widget(MDLabel(
            text="Activa tu lógica y resuelve desafíos mentales.",
            halign="center",
            theme_text_color="Secondary"
        ))
        card.add_widget(MDRaisedButton(
            text="Volver al menú",
            md_bg_color=(0.4, 0.6, 1, 1),
            on_release=lambda x: self.volver_menu()
        ))

        self.add_widget(card)

    def volver_menu(self):
        self.manager.transition.direction = "right"
        self.manager.current = "menu"


# ---------- Pantalla de Memoria ----------
class MemoriaScreen(PantallaBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Fondo(color=(1, 0.96, 0.9, 1)))

        card = MDCard(orientation="vertical", padding=40, spacing=25,
                      size_hint=(0.9, 0.6), pos_hint={"center_x": 0.5, "center_y": 0.5},
                      elevation=6, radius=[20])
        card.md_bg_color = (1, 1, 1, 1)

        card.add_widget(MDLabel(
            text="🧠 Memoria Rápida",
            halign="center",
            font_style="H5"
        ))
        card.add_widget(MDLabel(
            text="Recuerda patrones y mejora tu atención.",
            halign="center",
            theme_text_color="Secondary"
        ))
        card.add_widget(MDRaisedButton(
            text="Volver al menú",
            md_bg_color=(1, 0.6, 0.4, 1),
            on_release=lambda x: self.volver_menu()
        ))

        self.add_widget(card)

    def volver_menu(self):
        self.manager.transition.direction = "right"
        self.manager.current = "menu"


# ---------- Aplicación principal ----------
class MiniMindApp(MDApp):
    def build(self):
        self.title = "MiniMind 🧘‍♀️"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"

        sm = MDScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(PuzzleScreen(name="puzzle"))
        sm.add_widget(MemoriaScreen(name="memoria"))

        return sm


if __name__ == "__main__":
    MiniMindApp().run()
