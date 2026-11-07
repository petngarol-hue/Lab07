import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO

        self.drop_biblio=ft.Dropdown(key="Biblio",
                              label="Biblioteca",
                              width=300,
                              options=self.controller.fill_biblioteca(),
                              on_select=self.controller.select_biblioteca)
        self.drop_libri=ft.Dropdown(key="Libri",
                                    label="Libri",
                                    options=self.controller.fill_genere(),
                                    on_select=self.controller.select_genere,
                                    )



        # Sezione 3: Libri
        # TODO
        self.btn_libri=ft.Button(content="Mostra Libri", align=ft.Alignment.CENTER,on_click=self.controller.mosta_libri)
        self.lista=ft.ListView(expand=True,spacing=10, padding=5 , auto_scroll=True)



        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row(spacing=50,
                   alignment=ft.MainAxisAlignment.CENTER,
                   controls=[self.drop_biblio,self.drop_libri]
                   ),


            # Sezione 3: Libri
            # TODO
            ft.Divider(),
            self.btn_libri,
            self.lista,

        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
