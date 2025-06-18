from sys import excepthook

import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self._view._dbState.value = ""

        year = self._view._txtAnno.value

        if year == "":
            self._view._txt_result.controls.append( ft.Text("Inserire un anno", color = "red"))
            self._view.update_page()
            return

        try:
            anno = int(year)
        except ValueError:
            self._view._txt_result.controls.append( ft.Text("Valore inserito non valido", color = "red"))
            self._view.update_page()
            return

        if not self._model.hasAnno(anno):
            self._view._txt_result.controls.append( ft.Text("Anno non presente. Scegliere un anno tra il 1816 e il 2016", color = "red"))
            self._view.update_page()
            return

        self._model.buildGraph(anno)
        self._view._txt_result.controls.append( ft.Text( f"Il grafo è stato creato con successo" ) )
        self._view._txt_result.controls.append( ft.Text( f"Il grafo ha {self._model.numeroCompConnesse()} componenti connesse" ) )
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi"))
        for n in self._model.getIdMap().values():
            self._view._txt_result.controls.append(ft.Text(f"{n.strState} -- {n.collegamenti[0]}"))


        self._view._dbState.options = [ft.dropdown.Option(key=state, text=state) for state in self.getOption()]
        self._view._dbState.disabled = False
        self._view._btnRicerca.disabled = False
        self._view._dbState.update()

        # Aggiorna il dropdown per riflettere i cambiamenti
        self._view.update_page()


    def handleRicerca(self, e):
        self._view._txt_result.controls.clear()

        self._view._txt_result.controls.append( ft.Text( f"Ricerca del nodo {self._view._dbState.value}" ) )
        self._view._txt_result.controls.append(ft.Text(f"I nodi collegati sono: "))
        try:
            for n in self._model.getNodesConn(str(self._view._dbState.value)):
                self._view._txt_result.controls.append( ft.Text( f"{n.getIdState()} - {n.getStrState()}" ) )
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view._txt_result.controls.append( ft.Text( f"Selezionare uno stato" , color="red") )
        self._view.update_page()

    def getOption(self):
        l = []
        for n in self._model.getNodes():
            l.append(n.strState)
        return l



