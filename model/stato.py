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
        return self.strState,"-", self.diState

    def setCollegamenti(self, collegamenti: int):
        self.collegamenti.append(collegamenti)

    def getCollegamenti(self):
        return self.collegamenti

    def getStrState(self):
        return self.strState

    def getIdState(self):
        return self.diState