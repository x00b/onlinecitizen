from onctz.api.model.models import *


class Model:
    def __init__(self, db):
        """
        :type db: SQLAlchemy
        :type ma: Marshmallow
        """
        self.db = db

    def Arpenp(self, cartorioRegistro, numeroCns, uf, nomeConjuge1, novoNomeConjuge1, nomeConjuge2, novoNomeConjuge2, dataCasamento, matricula, dataEntrada, dataRegistro):
        self.data = Arpenp(cartorioRegistro, numeroCns, uf, nomeConjuge1, novoNomeConjuge1, nomeConjuge2, novoNomeConjuge2, dataCasamento, matricula, dataEntrada, dataRegistro)
