from dataclasses import dataclass, field


@dataclass
class Stato:

    diState: int
    strState: str
    collegamenti: list = field(default_factory=list)



    def __hash__(self):
        return hash( self.diState )

    def __eq__(self, other):
        return self.diState == other.diState

    def __str__(self):
        return f"Lo Stato è {self.strState}, in suo numero identificativo {self.diState}"

    def setCollegamenti(self, collegamenti: int):
        self.collegamenti.append(collegamenti)

    def getCollegamenti(self):
        return self.collegamenti