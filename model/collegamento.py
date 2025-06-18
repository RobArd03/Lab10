from dataclasses import dataclass

from model.stato import Stato


@dataclass
class Collegamento:
    stato1 : Stato
    stato2 : Stato


    def __hash__(self):
        return hash( (self.stato1, self.stato2) )
    def __eq__(self, other):
        return (self.stato1, self.stato2) == (other.stato1, other.stato2)
    def __str__(self):
        return self.stato1.strState + " - " + self.stato2.strState

