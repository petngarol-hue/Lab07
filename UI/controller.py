import flet as ft

from UI import view
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # todo
    def fill_biblioteca(self):
        self.biblioteca=[]

        for n in self._model.get_biblioteche():

            self.biblioteca.append(
                ft.DropdownOption(key=str(n.id) ,text=str(n.nome))
            )
        return self.biblioteca
    def fill_genere(self):
        self.genere=[]

        for n in self._model.get_generi():
            self.genere.append(
                ft.DropdownOption(key=str(n) ,text=str(n))
            )
        return self.genere





    # CALLBACKS DROPDOWN
    # TODO
    def select_biblioteca(self,e):
        self.biblioteca_selezionata=e.control.value
    def select_genere(self,e):
        self.genere_selezionato =e.control.value



    # AZIONE: MOSTRA LIBRI
    # TODO
    def mosta_libri(self):
        self._view.lista.controls.clear()

        for n in self._model.get_libri_filtrati(self.biblioteca_selezionata,self.genere_selezionato):
            self._view.lista.controls.append(ft.Text(f"{n}"))








